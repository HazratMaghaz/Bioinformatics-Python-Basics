"""
Basic GenBank Parser using Biopython

Downloads and parses a GenBank record from NCBI.
Replace the email with your own email before running.
"""

from Bio import Entrez, SeqIO

Entrez.email = "your_email@example.com"


def fetch_genbank_record(accession):
    handle = Entrez.efetch(
        db="nucleotide",
        id=accession,
        rettype="gb",
        retmode="text"
    )

    record = SeqIO.read(handle, "genbank")
    handle.close()

    return record


if __name__ == "__main__":
    accession_id = "NM_001301717"

    record = fetch_genbank_record(accession_id)

    print("Accession:", record.id)
    print("Name:", record.name)
    print("Description:", record.description)
    print("Sequence length:", len(record.seq))
    print("Number of features:", len(record.features))
