e-cienciaDatos: "readme" form 

-------------------
GENERAL INFORMATION
-------------------
1. Title of dataset

The Financial Document Causality Detection Shared Task (FinCausal 2026): Dataset

2. Contact

   Principal Investigator Contact Information
        Name: Antonio Moreno Sandoval
        Institution: Universidad Autónoma de Madrid (Laboratorio de Lingüística Informática)
        Email: antonio.msandoval@uam.es
	ORCID: 0000-0002-9029-2216

3. Description of the project

The Financial Document Causality Detection Shared Task (FinCausal 2026) aims to improve causality identification in the financial domain through its texts. This shared task focuses on determining the causality associated with both events and quantified facts. For this task, a cause can be the justification of a statement or the reason explaining an outcome; therefore, it is a relation detection task.
The changes introduced in the 2026 edition compared to the 2025 edition are numerous. These improvements include an exhaustive review of the datasets to eliminate ambiguities, the expansion of the corpus with more than 500 new fragments for each language featuring complex causal structures—such as chains of three or more elements—and the reformulation of abstractive questions in 10% of the cases to require advanced reasoning. Additionally, a new evaluation metric based on "LLM-as-a-judge" has been implemented to assess the adequacy of the answers, aligning with current state-of-the-art practices. Using an "LLM-as-a-judge" consists of employing a language model specifically instructed to generate ratings from 1 to 5 following a specific set of criteria, which somewhat mimics human evaluation.
Participants, given the context and the abstractive question, must extract the literal answer from the context that responds to that question. The questions seek causal-type relationships, whether they are the cause or the effect. The dataset for the Spanish subtask has been extracted from a corpus of Spanish annual financial reports from 2014 to 2018 (FinT-esp), while the English subtask uses the English version of the 2018 bilingual Spanish-English corpus of these reports, along with several annual financial reports from the Lancaster UCREL research team corpus.
Participants receive a CSV file with the following fields: ID; Text; Question; Answer. The conventional way to participate is to fine-tune a model using data annotated by linguists (including Inter-Annotator Agreement, IAA) and subsequently use the fine-tuned model to predict the "ANSWER" field of the test set. This publication refers to the competition dataset, specifically the training split with its answers and the test split without answers (since it needs to be evaluated). There are 2,000 samples per language for training, 500 for the English test set, and 503 for the Spanish test set.

4. Description of the dataset

This is a dataset from the FinCausal 2026 competition. It is designed for participants to use it to fine-tune their models and complete the task with the highest possible similarity to the gold standard, according to the established metrics.
It consists of texts annotated by linguists, where a context, an abstractive question, and its corresponding extractive answer—which addresses the causal nature of the question—are provided.
There are two versions available: one in English and one in Spanish.

5. Notes


6. Deposit date

January 23rd 2025.

7. Date

January 6th 2024.

8. Language

English and Spanish.

--------------------------
AUTHOR INFORMATION
--------------------------
1. Author

        Name: Antonio
        Last name  : Moreno Sandoval
        Institution: Universidad Autónoma de Madrid (Laboratorio de Lingüística Informática)
        Email: antonio.msandoval@uam.es
    ORCID: 0000-0002-9029-2216

        Name: Yanco Amor
        Last name  : Torterolo Orta
        Institution: Universidad Autónoma de Madrid (Laboratorio de Lingüística Informática)
        Email: yanco.torterolo@estudiante.uam.es
    ORCID: 0000-0002-3688-3293

        Name: Maria Alexia
        Last name  : Stanescu
        Institution: Universidad Autónoma de Madrid (Laboratorio de Lingüística Informática)
        Email: maria.stanescu@estudiante.uam.es
    ORCID: 0009-0001-8307-3023

        Name: Melina
        Last name  : Chatzi
        Institution: Universidad Autónoma de Madrid (Laboratorio de Lingüística Informática)
        Email: melina.chatzi@estudiante.uam.es
    ORCID: 0009-0007-9937-0480

--------------------------
METHODOLOGY
--------------------------
1. Methodology

a) Collection of financial reports.
b) Cleaning of the reports.
c) Linguistic annotation: generation of an abstractive question and its corresponding extractive answer based on the context.
d) Validation through IAA (inter-annotator agreement).

2. Software

Python for the initial extraction.
Pages (Mac), Excel (Windows), Calc (Linux).
 
--------------------------
KEYWORDS
--------------------------
1. Keywords

dataset
question answering
FinCausal
shared task
causality
cause-effect
annual reports
financial texts

--------------------------
SPONSORSHIP INFORMATION AND GRANT IDs
--------------------------
1. Grant Information

It was funded by a Spanish national project.

Project name (abbreviation): GRESEL-UAM.

Reference number: PID2023-151280OB-C21.

Project title: GRESEL-UAM: About GRESEL: AI Generation Results Enriched with Simplified Explanations Based on Linguistic Features (Resultados de Generación de IA Enriquecidos con Explicaciones Simplificadas Basadas en Características Lingüísticas).

Entity: Universidad Autónoma de Madrid.

Center: Facultad de Filosofía y Letras.

Financing Institution: Ministerio de Ciencia, Innovación y Universidades. Agencia Estatal de Investigación.

--------------------------
RELATED PUBLICATIONS
--------------------------
1. Related publication

MORENO-SANDOVAL, A., PORTA-ZAMORANO, J., CARBAJO-CORONADO, B., SAMY, D. MARIKO, D., EL-HAJ, M. (2023) 'The Financial Document Causality Detection Shared Task (FinCausal 2023)' in proceedings of the 5th Financial Narrative Processing Workshop (FNP 2023) at the 2023 IEEE International Conference on Big Data (IEEE BigData 2023). Sorrento, diciembre.

MORENO SANDOVAL, A., PORTA, J., CARBAJO-CORONADO, B., TORTEROLO, Y., SAMY, D. (2025)  The Financial Document Causality Detection Shared Task (FinCausal 2025). In Proceedings of the Joint Workshop of the 9th Financial Technology and Natural Language Processing (FinNLP), the 6th Financial Narrative Processing (FNP), and the 1st Workshop on Large Language Models for Finance and Legal (LLMFinLegal), pages 214–221, Abu Dhabi, UAE. Association for Computational Linguistics.

PORTA-ZAMORANO, J., CARBAJO-CORONADO, B., MORENO-SANDOVAL, A. (2024). Extraction and Structuring of Financial Terminology. Procesamiento del Lenguaje Natural, 73, 139-149. DOI 10.26342/2024-73-10

MORENO SANDOVAL, A., A. GISBERT, H. MONTORO (2020) 'Fint-esp: a corpus of financial reports in Spanish' en Miguel Fuster-Márquez, Carmen Gregori-Signes, José Santaemilia Ruiz (eds.): Multiperspectives in Analysis and Corpus Design, Granada: Editorial Comares, pp. 89-102.

MORENO SANDOVAL, A. (2021) 'Financial Narrative Processing in Spanish.' Tirant lo Blanch. ISBN papel: 9788418802423, ISBN ebook: 9788418802430.

2. Related dataset

Moreno-Sandoval, Antonio; Carbajo-Coronado, Blanca; Porta, Jordi, 2025, 'The financial document causality detection shared task (FinCausal 2023): Dataset,' https://doi.org/10.21950/2JOAZJ, e-cienciaDatos, V1.

Carbajo-Coronado, B., Moreno-Sandoval, A., Torterolo Orta, Y. A., & Gozalo, P. (2025). "The Financial Document Causality Detection Shared Task (FinCausal 2025): Dataset", https://doi.org/10.21950/V8VSSO, e-cienciaDatos, V1.

--------------------------
GEOGRAPHIC INFORMATION
--------------------------
1. Spatial coverage

Spain.

--------------------------
TEMPORAL INFORMATION
--------------------------
1. Time period coverage

Development: October 1st, 2025 to January 6th, 2026.

Framing project (duration of GRESEL project): from September 1st, 2024 to August 1st, 2027.

--------------------------
FILES
--------------------------
1. Files 

-Compressed folder 'fincausal_2026,' which contains 'train_en.csv' and 'train_es.csv' (one file per language).

-Compressed folder 'test,' which contains 'test_es_503.csv' y 'test_en_500.csv' (one file per language).

-This file, readme-en.txt.

--------------------------
LICENSES AND PRIVACITY
--------------------------
1. Licenses

LCC BY-NC-SA (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es).

2. Privacity

Does not apply.

--------------------------
OTHERS
--------------------------
1. DOI:  https://doi.org/10.21950/H7RKHH




