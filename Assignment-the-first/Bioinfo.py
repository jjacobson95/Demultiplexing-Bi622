#!/usr/bin/env python

DNA_bases ="GgCcAaTtNn"
RNA_bases ="GgCcAaUuNn"

def init_list(lst: list, value: float=0.0) -> list:
    '''This function takes an empty list and will populate it with
    the value passed in "value". If no value is passed, initializes list
    with 101 values of 0.0.'''
    for i in range(101):
        lst.append(value)
    return lst

def convert_phred(letter):
    """Converts a single character into a phred score"""
    llama =(ord(letter)-33)
    return llama

def validate_base_seq(seq,RNAflag):
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag is True), Gs, Cs. False otherwise. Case insensitive.'''
    seq = seq.upper()
    return len(seq) == seq.count("A") + seq.count("U" if RNAflag else "T") + seq.count("G") + seq.count("C")

def gc_content(DNA):
    '''Returns GC content of a DNA sequence as a decimal between 0 and 1.'''
    assert validate_DNA_seq(DNA), "String contains invalid characters"
    DNA = DNA.upper()
    Gs = DNA.count("G")
    Cs = DNA.count("C")
    return (Gs+Cs)/len(DNA)

def qual_score(phred_score: str) -> float:
    ''' Input a string of phred scores. Output is the average quality score value.
        This function calls the function convert_phred '''
    sum_fred = 0
    fred_counter = 0
    list_of_freds = list(phred_score)
    for fred in list_of_freds:
        sum_fred = (sum_fred + convert_phred(fred))
        fred_counter +=1
    average_fred = (sum_fred/fred_counter)
    return average_fred

def fasta_homogenizer(inputfile_name: str, output_filename: str):
    """import a fasta file with variable seq line length. export fasta file with 2 lines per read."""
    with open (inputfile_name, "r") as fh:
        seq_holder = []
        f = open(output_filename,"a")
        f.truncate(0)
        count = 0
        for line in fh:
            line = line.strip("\n")
            #print(line[0])
            if line.startswith(">"):
                if count > 0:
                    f.write("\n")
                f.write(line)
                f.write("\n")
                count = 1
            if line.startswith(">") != True:
                f.write(line)
                
    f.close()