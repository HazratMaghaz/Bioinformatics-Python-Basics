"""
FASTA GC Summary

Reads a FASTA file and prints sequence length and GC content for each record.
This script uses simple Python only, without Biopython.
"""

def read_fasta(file_path):
    records = {}
    current_id = None
    sequence_parts = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if current_id is not None:
                    records[current_id] = "".join(sequence_parts)

                current_id = line[1:]
                sequence_parts = []
            else:
                sequence_parts.append(line.upper())

    if current_id is not None:
        records[current_id] = "".join(sequence_parts)

    return records


def calculate_gc_content(sequence):
    sequence = sequence.upper()
    gc_count = sequence.count("G") + sequence.count("C")

    if len(sequence) == 0:
        return 0

    return (gc_count / len(sequence)) * 100


if __name__ == "__main__":
    fasta_file = "examples/example_sequence.fasta"
    records = read_fasta(fasta_file)

    for record_id, sequence in records.items():
        gc_content = calculate_gc_content(sequence)

        print("Record:", record_id)
        print("Length:", len(sequence))
        print("GC Content:", round(gc_content, 2), "%")
        print("-" * 30)
