# DNA Complement Strand Generator

sequence = input("Enter your DNA sequence: ").upper().strip()

complement = ""
valid_sequence = True

for base in sequence:
    if base == "A":
        complement += "T"
    elif base == "T":
        complement += "A"
    elif base == "G":
        complement += "C"
    elif base == "C":
        complement += "G"
    else:
        valid_sequence = False
        break

if valid_sequence:
    print("\nOriginal sequence:  ", sequence)
    print("Complement strand: ", complement)
else:
    print("Invalid DNA sequence. Please use only A, T, G, and C.")
