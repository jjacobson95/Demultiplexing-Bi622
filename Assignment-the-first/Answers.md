# Assignment the First

## Part 1
1. Be sure to upload your Python script.

| File name | label |
|---|---|
| 1294_S1_L008_R1_001.fastq.gz |Read 1 |
| 1294_S1_L008_R2_001.fastq.gz |Index 1 |
| 1294_S1_L008_R3_001.fastq.gz |Index 2 |
| 1294_S1_L008_R4_001.fastq.gz |Read 2 |

2. Per-base NT distribution
    1. Use markdown to insert your 4 histograms here.
    2. ```Your answer here```
    3. ```Your answer here```
    
## Part 2

Problem:
From four files, determine which reads have the correct indexes, swapped indexes, or low-quality indexes. 

Results:
52 output files:
•	26 files – R1 FASTQ files
•	26 files – R2 FASTQ files
•	1 file – R1 Nonmatching index pair FASTQ files
•	1 file – R2 Nonmatching index pair FASTQ files
•	1 file – R1 Low quality index FASTQ files
•	1 file – R2 Low quality index FASTQ files


Pseudocode:

•	Create 4 test files with 12 lines in each of them.

•	Create a function find the reverse complement “reverse_complement_check”
	o	Docstring: “”” This function will take the barcodes from two files. It will determine if the barcode in file 2 is the reverse complement of file 1. If True it will return ‘1’. If false, it will return ‘2’.””””
	o	Input: two strings: (barcode extracted from each read)
	o	Return: 1 or 2
o	Example: input is:  CAGGTTT and AAACCTG
	Return: 1
o	Example: input is: CCTTGGAA and TTCCAANG
	Return: 2

•	Create a function to determine if two reads are mis-matched or if they have non-existing barcodes. This function is called sort_unmatching_barcodes
	o	Docstring: “”” This function will take the barcodes of two files. If either of the barcodes don’t exist, the function will return a ‘4’. If both barcodes exist, the function will return a ‘3’. “””
	o	Input: two strings: (barcode extracted from each read)
	o	Return 3 or 4
o	Example input: CCTAGAA and TTCTAGN
	Return: 4
o	Example input: GTAGCGTA and AACAGCGA
	Return: 3

•	Create a function to match sequences with mismatched / Ns for extra credit
o	This function is called sequence_corrector
	Do this for extra credit maybe. 

•	Create generic output name template
•	Open all 4 files in r mode.
•	For each read, check if the barcodes are the same (reverse complement) using reverse_complement_check function in files 2 and 3. 
	o	If they are the same (return value ‘1’), append the reads from files 1 and 4 to their appropriate output files. Output files are determined by index sequence.
	o	If they have different barcodes (return value ‘2’) run sort_unmatching_barcodes function.
		o	 If they are both existing barcodes (return value ‘3’), append the reads from files 1 and 4 to the nonmatching index pair output files. 
		o	 If either of them is a non-existing barcode return value ‘4’), append the reads from files 1 and 4 to the low-quality index pair files.
		o	 For extra credit, apply the sequence_corrector here.

