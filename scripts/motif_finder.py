# Simple DNA Motif Finder

sequence = input("Enter your DNA sequence: ").upper().strip()
motif = input("Enter the motif to search: ").upper().strip()

if motif in sequence:
    position = sequence.find(motif) + 1
    count = sequence.count(motif)

    print("\nMotif found!")
    print("First position:", position)
    print("Total occurrences:", count)
else:
    print("\nMotif not found.")
