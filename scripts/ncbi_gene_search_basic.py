"""
NCBI Gene Search using Biopython Entrez

Searches the NCBI Gene database for a gene keyword.
Replace the email with your own email before running.
"""

from Bio import Entrez

Entrez.email = "your_email@example.com"


def search_gene_database(query, max_results=5):
    handle = Entrez.esearch(
        db="gene",
        term=query,
        retmax=max_results
    )

    results = Entrez.read(handle)
    handle.close()

    return results["IdList"]


if __name__ == "__main__":
    query = "BRCA1 Homo sapiens"
    gene_ids = search_gene_database(query)

    print("Query:", query)
    print("Gene IDs found:")

    for gene_id in gene_ids:
        print(gene_id)
