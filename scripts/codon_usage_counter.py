"""
Codon Usage Counter

Counts codons in a coding DNA sequence.
The script reads the DNA sequence in groups of three bases.
"""

def count_codons(dna_sequence):
    dna_sequence = dna_sequence.upper().replace(" ", "")
    codon_counts = {}

    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i + 3]

        if len(codon) == 3:
            if codon in codon_counts:
                codon_counts[codon] += 1
            else:
                codon_counts[codon] = 1

    return codon_counts


if __name__ == "__main__":
    dna_sequence = "ATGGCCATGTAA"

    counts = count_codons(dna_sequence)

    print("DNA Sequence:", dna_sequence)
    print("Codon usage:")

    for codon, count in sorted(counts.items()):
        print(codon, ":", count)
