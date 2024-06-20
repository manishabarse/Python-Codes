import re
from Bio import SeqIO
from Bio.SeqUtils import nt_search
from Bio.Seq import Seq

def read_fasta(file_path):
    records = SeqIO.to_dict(SeqIO.parse(file_path, "fasta"))
    return records



def find_orfs(sequence):
    orfs = []
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    for frame in range(3):
        seq_str = str(sequence[frame:])
        start_positions = [match + frame for match in nt_search(seq_str, start_codon)]

        for start in start_positions:
            end_positions = [match + frame for match in nt_search(seq_str[start - frame:], "|".join(stop_codons))]
            if end_positions:
                end = start + min(end_positions) + 3
                orf_sequence = sequence[start:end]
                if len(orf_sequence) % 3 == 0:
                    orfs.append((start + 1, len(orf_sequence), str(orf_sequence)))  # Store start position, length, and sequence of the ORF

    return orfs



def analyze_sequences(records):
    # Question 1: Number of records
    num_records = len(records)
    print(f"Number of records in the file: {num_records}")

    # Question 2: Length of the longest sequence
    max_length = max(len(record.seq) for record in records.values())
    print(f"Length of the longest sequence: {max_length}")

    # Question 3: Length of the shortest sequence
    min_length = min(len(record.seq) for record in records.values())
    print(f"Length of the shortest sequence: {min_length}")

    # Question 4: Length of the longest ORF in reading frame 2
    orfs_frame2 = [orf for sequence in records.values() for orf in find_orfs(sequence)]
    print("ORFs in reading frame 2:", orfs_frame2)

    if orfs_frame2:
        longest_orf_start_frame2, longest_orf_length_frame2, longest_orf_sequence_frame2 = max(orfs_frame2, key=lambda x: x[1])
        print(f"Starting position of the longest ORF in reading frame 2: {longest_orf_start_frame2}")
        print(f"Length of the longest ORF in reading frame 2: {longest_orf_length_frame2}")
        print(f"Longest ORF sequence in reading frame 2: {longest_orf_sequence_frame2}")
    else:
        print("No ORFs found in reading frame 2. This could be due to the absence of valid start and stop codons in the frame.")

    # Question 5: Starting position of the longest ORF in reading frame 3
    longest_orf_start_frame3 = max(
        min(start_positions) + 1 for sequence in records.values() for start_positions in nt_search(str(sequence), "ATG", 3)
    )
    print(f"Starting position of the longest ORF in reading frame 3: {longest_orf_start_frame3}")

    # Question 6: Length of the longest ORF in any forward reading frame
    longest_orf_length_any_frame = max(
        len(orf) for sequence in records.values() for frame in range(1, 4) for orf in find_orfs(sequence, frame)
    )
    print(f"Length of the longest ORF in any forward reading frame: {longest_orf_length_any_frame}")

    # Question 7: Length of the longest forward ORF in the sequence with identifier gi|142022655|gb|EQ086233.1|16
    sequence_id = "gi|142022655|gb|EQ086233.1|16"
    longest_orf_length_specific_sequence = max(
        len(orf) for orf in find_orfs(records[sequence_id].seq, frame=1)
    )
    print(f"Length of the longest forward ORF in the specific sequence: {longest_orf_length_specific_sequence}")

    # Question 8: Most frequently occurring repeat of length 6
    repeats_length_6 = {}
    for sequence in records.values():
        seq_str = str(sequence)
        for start in range(len(seq_str) - 6 + 1):
            repeat = seq_str[start:start + 6]
            if repeat in repeats_length_6:
                repeats_length_6[repeat] += 1
            else:
                repeats_length_6[repeat] = 1
    most_frequent_repeat_length_6 = max(repeats_length_6, key=repeats_length_6.get)
    occurrences_most_frequent_repeat_length_6 = repeats_length_6[most_frequent_repeat_length_6]
    print(f"Most frequent repeat of length 6: {most_frequent_repeat_length_6}")
    print(f"Number of occurrences: {occurrences_most_frequent_repeat_length_6}")

    # Question 9: All repeats of length 12 and count different sequences
    repeats_length_12 = {}
    for sequence in records.values():
        seq_str = str(sequence)
        for start in range(len(seq_str) - 12 + 1):
            repeat = seq_str[start:start + 12]
            if repeat in repeats_length_12:
                repeats_length_12[repeat] += 1
            else:
                repeats_length_12[repeat] = 1
    different_sequences_count_length_12 = sum(1 for count in repeats_length_12.values() if count == max(repeats_length_12.values()))
    print(f"Number of different 12-base sequences occurring Max times: {different_sequences_count_length_12}")

    # Question 10: Repeat of length 7 with maximum occurrences
    repeats_length_7 = {}
    for sequence in records.values():
        seq_str = str(sequence)
        for start in range(len(seq_str) - 7 + 1):
            repeat = seq_str[start:start + 7]
            if repeat in repeats_length_7:
                repeats_length_7[repeat] += 1
            else:
                repeats_length_7[repeat] = 1
    most_occurrences_repeat_length_7 = max(repeats_length_7, key=repeats_length_7.get)
    occurrences_most_repeat_length_7 = repeats_length_7[most_occurrences_repeat_length_7]
    print(f"Repeat of length 7 with maximum occurrences: {most_occurrences_repeat_length_7}")
    print(f"Number of occurrences: {occurrences_most_repeat_length_7}")

# Replace 'your_file.fasta' with the path to your multi-FASTA file
file_path = 'dna2.fasta'
sequences = read_fasta(file_path)
analyze_sequences(sequences)
