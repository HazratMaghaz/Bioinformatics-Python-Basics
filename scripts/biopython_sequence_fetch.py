# Fetch a sequence record from NCBI using Biopython
# Note: Replace the email with your own email before real NCBI usage.

from Bio import Entrez, SeqIO

Entrez.email = "your_email@example.com"

accession_id = input("Enter accession ID, example: NM_000546: ").strip()

handle = Entrez.efetch(
    db="nucleotide",
    id=accession_id,
    rettype="fasta",
    retmode="text"
)

record = SeqIO.read(handle, "fasta")
handle.close()

print("\nRecord ID:", record.id)
print("Description:", record.description)
print("Sequence length:", len(record.seq))
print("First 100 bases:", record.seq[:100])
