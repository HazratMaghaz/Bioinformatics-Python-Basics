# Basic PubMed Search using Biopython Entrez
# Note: Replace the email with your own email before real NCBI usage.

from Bio import Entrez

Entrez.email = "your_email@example.com"

query = input("Enter PubMed search query: ").strip()

handle = Entrez.esearch(
    db="pubmed",
    term=query,
    retmax=5
)

record = Entrez.read(handle)
handle.close()

print("\nPubMed IDs found:")
for pubmed_id in record["IdList"]:
    print(pubmed_id)
