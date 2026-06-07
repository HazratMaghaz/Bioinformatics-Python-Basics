"""
Pairwise Sequence Identity

Calculates simple percent identity between two aligned DNA/protein sequences.
Both sequences should have the same length.
"""

def calculate_identity(sequence_1, sequence_2):
    sequence_1 = sequence_1.upper()
    sequence_2 = sequence_2.upper()

    if len(sequence_1) != len(sequence_2):
        raise ValueError("Sequences must have the same length for this simple version.")

    matches = 0

    for base_1, base_2 in zip(sequence_1, sequence_2):
        if base_1 == base_2:
            matches += 1

    identity = (matches / len(sequence_1)) * 100
    return identity


if __name__ == "__main__":
    seq1 = "ATGCGTACGT"
    seq2 = "ATGCGTTCGT"

    identity = calculate_identity(seq1, seq2)

    print("Sequence 1:", seq1)
    print("Sequence 2:", seq2)
    print("Percent identity:", round(identity, 2), "%")
