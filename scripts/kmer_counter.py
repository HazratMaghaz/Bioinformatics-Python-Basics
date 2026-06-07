"""
K-mer Counter

Counts all k-length words in a DNA sequence.
Example: for k=3, it counts codon-like patterns such as ATG, TGC, GCG.
"""

def count_kmers(sequence, k):
    sequence = sequence.upper()
    kmer_counts = {}

    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]

        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1

    return kmer_counts


if __name__ == "__main__":
    dna_sequence = "ATGCGATATCGATCGATGCG"
    k = 3

    results = count_kmers(dna_sequence, k)

    print("DNA Sequence:", dna_sequence)
    print("K:", k)
    print("K-mer counts:")

    for kmer, count in sorted(results.items()):
        print(kmer, ":", count)
