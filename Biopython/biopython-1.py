from Bio.SeqUtils import nt_search
from Bio import SeqIO
import re

def read_fasta(file_path):
    # Read the FASTA file and return a dictionary of Seq objects
    records = SeqIO.to_dict(SeqIO.parse(file_path, "fasta"))
    return records

def find_orfs(sequence, frame):
    orfs = []
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    
    seq_str = str(sequence)[frame - 1:]
    start_positions = [m.start() for m in re.finditer(start_codon, seq_str)]

    for start in start_positions:
        end_positions = [m.start() for m in re.finditer("|".join(stop_codons), seq_str[start:])]
        if end_positions:
            end = start + min(end_positions) + 3
            orf_sequence = sequence[start:end]
            if len(orf_sequence) % 3 == 0:
                orfs.append(len(orf_sequence))  # Only store the length of the ORF

    return orfs


def analyze_sequences(records):
    # Question 1: Number of records
    print("Q1")
    num_records = len(records)
    print(f"Number of records in the file: {num_records}")

    # Question 2: Lengths of sequences
    print("\n\n$$$$$$$$$$$ Q2 $$$$$$$$$$$$$$")
    sequence_lengths = [len(record.seq) for record in records.values()]
    print(f"Sequence lengths: {sequence_lengths}")
    
    max_length = max(sequence_lengths)
    min_length = min(sequence_lengths)
    
    longest_sequences = [id for id, seq in records.items() if len(seq) == max_length]
    shortest_sequences = [id for id, seq in records.items() if len(seq) == min_length]
    
    print(f"Longest sequence length: {max_length}")
    print(f"Shortest sequence length: {min_length}")
    
    print(f"Identifiers of longest sequences: {longest_sequences}")
    print(f"Identifiers of shortest sequences: {shortest_sequences}")

    # Question 3: Identify ORFs in frame 2
    longest_orf_length = 0
    longest_orf_sequence = ""
    longest_orf_identifier = ""
    
    for identifier, sequence in records.items():
        for frame in [1, 2, 3]:
            orfs = find_orfs(sequence, frame)
            for start, orf_sequence in orfs:
                if len(orf_sequence) > longest_orf_length:
                    longest_orf_length = len(orf_sequence)
                    longest_orf_sequence = orf_sequence
                    longest_orf_identifier = identifier
    
    print(f"Length of the longest ORF: {longest_orf_length}")
    print(f"Identifier of the sequence containing the longest ORF: {longest_orf_identifier}")
    print(f"Longest ORF sequence: {longest_orf_sequence}")
  
    # Question 4: Identify repeats
    print("\n\n$$$$$$$$$$ Q4 $$$$$$$$$$$$$")
    def find_repeats(sequence, length):
        repeats = {}
        for start in range(len(sequence) - length + 1):
            repeat = sequence[start:start + length]
            if repeat in repeats:
                repeats[repeat] += 1
            else:
                repeats[repeat] = 1
        return repeats

    repeat_length = 3  # Change this to the desired repeat length
    all_repeats = {}
    
    for identifier, sequence in records.items():
        repeats = find_repeats(sequence, repeat_length)
        all_repeats[identifier] = repeats
    
    most_frequent_repeat = max((repeat, count, identifier) for identifier, repeats in all_repeats.items()
                               for repeat, count in repeats.items())
    
    print(f"Most frequent repeat of length {repeat_length}: {most_frequent_repeat[0]}")
    print(f"Number of occurrences: {most_frequent_repeat[1]}")
    print(f"Identifier of the sequence containing the most frequent repeat: {most_frequent_repeat[2]}")

# Replace 'your_file.fasta' with the path to your multi-FASTA file
file_path = 'dna2.fasta'
sequences = read_fasta(file_path)
analyze_sequences(sequences)
