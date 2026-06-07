# DNA Length and Base Count Calculator

sequence = input("Enter your DNA sequence: ").upper().strip()

valid_bases = {"A", "T", "G", "C"}

if all(base in valid_bases for base in sequence):
    print("\nValid DNA sequence")
    print("Sequence length:", len(sequence))
    print("A count:", sequence.count("A"))
    print("T count:", sequence.count("T"))
    print("G count:", sequence.count("G"))
    print("C count:", sequence.count("C"))
else:
    print("\nInvalid DNA sequence. Please use only A, T, G, and C.")
