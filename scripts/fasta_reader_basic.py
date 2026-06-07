# Basic FASTA Reader Without External Libraries

fasta_file = "examples/example_sequence.fasta"

sequence_id = ""
sequence = ""

with open(fasta_file, "r") as file:
    for line in file:
        line = line.strip()

        if line.startswith(">"):
            sequence_id = line[1:]
        else:
            sequence += line

print("Sequence ID:", sequence_id)
print("Sequence:", sequence)
print("Length:", len(sequence))
print("GC count:", sequence.count("G") + sequence.count("C"))
