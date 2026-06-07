"""
Simple ORF Finder

Finds open reading frames that start with ATG and end with TAA, TAG, or TGA.
This is a simplified beginner version.
"""

def find_orfs(dna_sequence):
    dna_sequence = dna_sequence.upper()
    stop_codons = ["TAA", "TAG", "TGA"]
    orfs = []

    for start in range(len(dna_sequence) - 2):
        codon = dna_sequence[start:start + 3]

        if codon == "ATG":
            for end in range(start + 3, len(dna_sequence) - 2, 3):
                stop = dna_sequence[end:end + 3]

                if stop in stop_codons:
                    orf_sequence = dna_sequence[start:end + 3]
                    orfs.append((start + 1, end + 3, orf_sequence))
                    break

    return orfs


if __name__ == "__main__":
    dna_sequence = "CCCATGGCCAAATAGGGGATGTTTTAA"

    orfs = find_orfs(dna_sequence)

    print("DNA Sequence:", dna_sequence)
    print("ORFs found:")

    for start, end, sequence in orfs:
        print("Start:", start, "End:", end, "ORF:", sequence)
