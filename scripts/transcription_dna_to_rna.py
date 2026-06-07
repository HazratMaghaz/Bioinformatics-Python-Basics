# DNA to RNA Transcription

sequence = input("Enter your DNA sequence: ").upper().strip()

valid_bases = {"A", "T", "G", "C"}

if all(base in valid_bases for base in sequence):
    rna_sequence = sequence.replace("T", "U")
    print("\nDNA sequence:", sequence)
    print("RNA sequence:", rna_sequence)
else:
    print("Invalid DNA sequence. Please use only A, T, G, and C.")
