#!/usr/bin/env python3
"""Run lightweight integrity checks for the FinCausal submission package."""

from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_HASHES = {
    "data/train_en_2000.csv":
        "f90864a68ba217847f96db02d847e2c922b9732cda038f26e461df8f86800857",
    "data/splits/train.csv":
        "f01d96f999125d1db3d281bd44ab23a4d87fbec7733e5ef37ce4fedff38d8ac3",
    "data/splits/validation.csv":
        "fb572e9917560ffa8c2e213d6520105cfb02ac11d9bc1d9bb4dc5dfdd8d4c457",
    "data/splits/test.csv":
        "22e0b03e6d27f3e91a38631c2eca30b8e838cb0286b2e7b85430a9d196e4018f",
    "data/splits/development_decontaminated_196.csv":
        "4227f1a8062d412af4447ef27ec92812e87d9efb618f3649a3fff066c2884705",
    "data/splits/test_decontaminated_391.csv":
        "274adcfb3020a471af7a6698f112d2c9cafdb06de6fd0f9bac80a740215599e2",
    "human_reviews/m1_model_first_v6_screened_acceptance.csv":
        "91b62f5a96a7cb85b29fa272c2f1f784"
        "64f63dbd07692ecb515b98f0cb2d53bb",
    "human_reviews/c1_cross_example_candidate_audit_v7.csv":
        "785c3e746af85c7655da92d354e623168"
        "ad49e73e4794caf6187c205d44d145a",
    "human_reviews/m2_final_test_manual_review_packet_v1.csv":
        "5b377964d28913b18f348d27a85ef25421eaab4bde1e2c8773d5e035bd60850f",
}

EXPECTED_ROWS = {
    "data/train_en_2000.csv": 2000,
    "data/splits/train.csv": 1400,
    "data/splits/validation.csv": 200,
    "data/splits/test.csv": 400,
    "data/splits/development_decontaminated_196.csv": 196,
    "data/splits/test_decontaminated_391.csv": 391,
    "human_reviews/m1_model_first_v6_screened_acceptance.csv": 243,
    "human_reviews/c1_cross_example_candidate_audit_v7.csv": 50,
    "human_reviews/m2_final_test_manual_review_packet_v1.csv": 31,
}

SECRET_PATTERNS = {
    "OpenAI key": re.compile(r"\bsk-[A-Za-z0-9_-]{12,}\b"),
    "GitHub token": re.compile(
        r"\b(?:ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"
    ),
    "Hugging Face token": re.compile(r"\bhf_[A-Za-z0-9]{20,}\b"),
    "private key": re.compile(r"BEGIN (?:RSA|OPENSSH|EC) PRIVATE KEY"),
}


def fail(message: str) -> None:
    raise AssertionError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def check_files_and_rows() -> None:
    for relative_path, expected_rows in EXPECTED_ROWS.items():
        path = ROOT / relative_path
        if not path.exists():
            fail(f"Missing required file: {relative_path}")
        delimiter = ";" if relative_path == "data/train_en_2000.csv" else ","
        actual_rows = len(read_csv(path, delimiter=delimiter))
        if actual_rows != expected_rows:
            fail(
                f"{relative_path}: expected {expected_rows} rows, "
                f"found {actual_rows}"
            )


def check_frozen_hashes() -> None:
    for relative_path, expected_hash in EXPECTED_HASHES.items():
        actual_hash = sha256(ROOT / relative_path)
        if actual_hash != expected_hash:
            fail(
                f"{relative_path}: frozen hash changed\n"
                f"expected {expected_hash}\nactual   {actual_hash}"
            )


def check_manual_review() -> None:
    path = (
        ROOT
        / "human_reviews"
        / "m2_final_test_manual_review_packet_v1.csv"
    )
    rows = read_csv(path)
    if any(row["human_review_status"].strip().lower() != "reviewed" for row in rows):
        fail("The M2 review file contains a row not marked reviewed.")

    regressions = [
        row for row in rows
        if row["M2_vs_B1_strict_state"] == "M2_broke_B1_strict_correct"
    ]
    accepted = [
        row for row in regressions
        if row["human_semantically_correct"].strip().lower() == "yes"
    ]
    rejected = [
        row for row in regressions
        if row["human_semantically_correct"].strip().lower() == "no"
    ]
    if (len(regressions), len(accepted), len(rejected)) != (10, 7, 3):
        fail(
            "Unexpected M2 regression review counts: "
            f"{len(regressions)} total, {len(accepted)} accepted, "
            f"{len(rejected)} rejected"
        )


def check_notebook() -> None:
    path = ROOT / "notebooks" / "NLP_Final_Project_FinCausal_v11.ipynb"
    notebook = json.loads(path.read_text(encoding="utf-8"))
    if notebook.get("nbformat") != 4:
        fail("Notebook is not nbformat 4.")
    cells = notebook.get("cells", [])
    if len(cells) < 82:
        fail("Notebook is missing the completed-review verification cells.")
    first_cell = "".join(cells[0].get("source", []))
    if "v11" not in first_cell:
        fail("Notebook title does not identify v11.")
    full_source = "\n".join(
        "".join(cell.get("source", [])) for cell in cells
    )
    if "COMPLETED M2 HUMAN REVIEW VERIFICATION" not in full_source:
        fail("Notebook does not load and verify the completed M2 review.")
    for cell_number, cell in enumerate(cells, start=1):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        source_without_magics = "\n".join(
            line for line in source.splitlines()
            if not re.match(r"^\s*(?:%[A-Za-z]|![A-Za-z])", line)
        )
        try:
            ast.parse(source_without_magics)
        except SyntaxError as error:
            fail(f"Syntax error in notebook cell {cell_number}: {error}")


def check_for_secrets() -> None:
    suffixes = {".ipynb", ".md", ".py", ".txt", ".csv", ".json"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                fail(f"Possible {label} found in {path.relative_to(ROOT)}")


def main() -> int:
    checks = [
        ("required files and row counts", check_files_and_rows),
        ("frozen review hashes", check_frozen_hashes),
        ("completed M2 review counts", check_manual_review),
        ("notebook structure", check_notebook),
        ("secret scan", check_for_secrets),
    ]
    for label, check in checks:
        check()
        print(f"PASS: {label}")
    print("Repository validation complete.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
