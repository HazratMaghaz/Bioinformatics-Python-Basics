# Reverse Complement DNA Generator

sequence = input("Enter your DNA sequence: ").upper().strip()

base_pair = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

reverse_complement = ""
valid_sequence = True

for base in reversed(sequence):
    if base in base_pair:
        reverse_complement += base_pair[base]
    else:
        valid_sequence = False
        break

if valid_sequence:
    print("\nOriginal sequence:       ", sequence)
    print("Reverse complement:     ", reverse_complement)
else:
    print("Invalid DNA sequence. Please use only A, T, G, and C.")
