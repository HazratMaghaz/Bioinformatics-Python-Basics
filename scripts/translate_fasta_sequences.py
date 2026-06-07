"""
Translate FASTA Sequences

Reads DNA sequences from a FASTA file and translates them into protein.
This uses a small codon table for beginner learning.
"""

codon_table = {
    "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
    "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
    "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
    "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
    "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
    "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
    "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
    "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
    "TAC": "Y", "TAT": "Y", "TAA": "*", "TAG": "*",
    "TGC": "C", "TGT": "C", "TGA": "*", "TGG": "W"
}


def read_fasta(file_path):
    records = {}
    current_id = None
    sequence_parts = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                if current_id:
                    records[current_id] = "".join(sequence_parts)

                current_id = line[1:]
                sequence_parts = []
            else:
                sequence_parts.append(line.upper())

    if current_id:
        records[current_id] = "".join(sequence_parts)

    return records


def translate_dna(dna_sequence):
    protein = ""

    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i + 3]
        protein += codon_table.get(codon, "X")

    return protein


if __name__ == "__main__":
    records = read_fasta("examples/example_sequence.fasta")

    for record_id, dna_sequence in records.items():
        protein = translate_dna(dna_sequence)

        print("Record:", record_id)
        print("DNA:", dna_sequence)
        print("Protein:", protein)
        print("-" * 30)
