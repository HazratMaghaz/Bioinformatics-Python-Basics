"""
FASTQ Quality Summary

Reads a small FASTQ file and calculates average Phred quality score per read.
This is a beginner-friendly FASTQ parser.
"""

def phred_score(quality_character):
    return ord(quality_character) - 33


def average_quality(quality_string):
    scores = []

    for character in quality_string:
        scores.append(phred_score(character))

    if len(scores) == 0:
        return 0

    return sum(scores) / len(scores)


def read_fastq(file_path):
    with open(file_path, "r") as file:
        while True:
            header = file.readline().strip()
            sequence = file.readline().strip()
            plus = file.readline().strip()
            quality = file.readline().strip()

            if not header:
                break

            yield header, sequence, quality


if __name__ == "__main__":
    fastq_file = "examples/example_reads.fastq"

    for header, sequence, quality in read_fastq(fastq_file):
        avg_q = average_quality(quality)

        print("Read:", header)
        print("Sequence:", sequence)
        print("Length:", len(sequence))
        print("Average Quality:", round(avg_q, 2))
        print("-" * 30)
