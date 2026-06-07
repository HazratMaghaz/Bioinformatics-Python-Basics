![Python](https://img.shields.io/badge/Python-3.x-blue)
![Bioinformatics](https://img.shields.io/badge/Domain-Bioinformatics-green)
![Biopython](https://img.shields.io/badge/Library-Biopython-yellowgreen)
![NCBI](https://img.shields.io/badge/Data-NCBI-orange)
![Level](https://img.shields.io/badge/Level-Beginner-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)



# Bioinformatics Python Basics

A beginner-friendly collection of small Python scripts for learning basic bioinformatics programming.

This repository focuses on simple DNA/RNA sequence tasks such as sequence length calculation, nucleotide counting, GC content, complement/reverse complement generation, motif searching, transcription, translation, FASTA reading, and beginner-level data retrieval using Biopython.

The code is intentionally written in a simple style so it is easy to read, modify, and learn from.

---

## Repository Structure

```text
.
├── scripts/
│   ├── dna_length_calculator.py
│   ├── gc_content_calculator.py
│   ├── complement_dna_strand.py
│   ├── reverse_complement.py
│   ├── motif_finder.py
│   ├── transcription_dna_to_rna.py
│   ├── translation_rna_to_protein.py
│   ├── fasta_reader_basic.py
│   ├── biopython_sequence_fetch.py
│   └── ncbi_pubmed_search_basic.py
├── examples/
│   └── example_sequence.fasta
├── docs/
│   └── learning_notes.md
├── archive/
│   └── python_practice/
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Scripts Included

| Script | Purpose |
|---|---|
| `dna_length_calculator.py` | Calculates DNA sequence length and nucleotide counts |
| `gc_content_calculator.py` | Calculates GC percentage of a DNA sequence |
| `complement_dna_strand.py` | Generates the complement DNA strand |
| `reverse_complement.py` | Generates the reverse complement DNA strand |
| `motif_finder.py` | Searches for a motif inside a DNA sequence |
| `transcription_dna_to_rna.py` | Converts DNA sequence to RNA sequence |
| `translation_rna_to_protein.py` | Translates a simple RNA sequence into protein sequence |
| `fasta_reader_basic.py` | Reads a FASTA file without external libraries |
| `biopython_sequence_fetch.py` | Fetches a sequence record from NCBI using Biopython |
| `ncbi_pubmed_search_basic.py` | Searches PubMed records using Biopython Entrez |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/HazratMaghaz/Bioinformatics-Python-Basics.git
cd Bioinformatics-Python-Basics
```

Install optional dependencies:

```bash
pip install -r requirements.txt
```

Biopython is only required for the NCBI/Entrez example scripts.

---

## How to Run

Run any script from the repository root. Example:

```bash
python scripts/gc_content_calculator.py
```

For FASTA reading:

```bash
python scripts/fasta_reader_basic.py
```

---

## Skills Demonstrated

- Basic Python syntax
- Functions and conditionals
- Loops and string handling
- DNA/RNA sequence processing
- FASTA file parsing
- Simple bioinformatics logic
- Beginner-level Biopython usage
- Clean GitHub repository organization

---

## Author

**Hazrat Maghaz**  
Bioinformatician | Computational Biologist | Artifical Intelegence

[![Website](https://img.shields.io/badge/Website-hazratmaghaz.tech-blue?style=for-the-badge&logo=google-chrome&logoColor=white)](https://hazratmaghaz.tech)
[![GitHub](https://img.shields.io/badge/GitHub-HazratMaghaz-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HazratMaghaz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Hazrat%20Maghaz-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hazrat-maghaz-6967b9374/)

---

## License

This repository is available under the MIT License. See the `LICENSE` file for details.
