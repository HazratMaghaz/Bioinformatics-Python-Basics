# GC Content Calculator

sequence = input("Enter your DNA sequence: ").upper().strip()

valid_bases = {"A", "T", "G", "C"}

if len(sequence) == 0:
    print("No sequence entered.")
elif all(base in valid_bases for base in sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    gc_content = ((g_count + c_count) / len(sequence)) * 100

    print("\nSequence length:", len(sequence))
    print("GC content:", round(gc_content, 2), "%")
else:
    print("Invalid DNA sequence. Please use only A, T, G, and C.")
