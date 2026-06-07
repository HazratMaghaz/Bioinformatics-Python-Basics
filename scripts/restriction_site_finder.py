"""
Restriction Site Finder

Finds common restriction enzyme recognition sites in a DNA sequence.
"""

def find_restriction_sites(dna_sequence):
    dna_sequence = dna_sequence.upper()

    enzymes = {
        "EcoRI": "GAATTC",
        "BamHI": "GGATCC",
        "HindIII": "AAGCTT",
        "NotI": "GCGGCCGC"
    }

    results = {}

    for enzyme, site in enzymes.items():
        positions = []

        for i in range(len(dna_sequence) - len(site) + 1):
            if dna_sequence[i:i + len(site)] == site:
                positions.append(i + 1)

        results[enzyme] = positions

    return results


if __name__ == "__main__":
    dna_sequence = "ATCGAATTCGGATCCAAGCTTGCGGCCGC"

    sites = find_restriction_sites(dna_sequence)

    print("DNA Sequence:", dna_sequence)

    for enzyme, positions in sites.items():
        if positions:
            print(enzyme, "found at positions:", positions)
        else:
            print(enzyme, "not found")
