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


![Test Image 1](https://github.com/jjacobson95/Demultiplexing-Bi622/blob/master/Assignment-the-first/Demultiplexing_the_first_histograms/histogram_R1.png)


    3. ```Cutoff of 20 seems reasonable. This way we would retain most of the data, but still keep it at high quality (99% or greater)```
    4. ```Using the command: zcat 1294_S1_L008_R2_001.fastq.gz 1294_S1_L008_R3_001.fastq.gz| sed -n '2~4p' | awk '{print FNR, $0}' | grep -E [Nn] | sort | uniq -c | sort | awk '{print NR,$2}' | wc -l
		I got 7304664 indexes. (These are the combined indexes with Ns between the two files, not repetitive)
       ```
    
## Part 2
1. Define the problem
```
From four files, determine which reads have the correct indexes, swapped indexes, or low-quality indexes. 
```
2. Describe output
```
	52 output files:
	•	26 files – R1 FASTQ files
	•	26 files – R2 FASTQ files
	•	1 file – R1 Nonmatching index pair FASTQ files
	•	1 file – R2 Nonmatching index pair FASTQ files
	•	1 file – R1 Low quality index FASTQ files
	•	1 file – R2 Low quality index FASTQ files
```

3. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).
``` 
Done
```
4. Pseudocode including functions:
```
•Create 4 test files with 20,000 lines in each of them for general use.
•Create a function to find the reverse complement & match between files called  “reverse_complement_check”
	o Docstring: “”” This function will take the barcodes from two files. It will determine if the barcode in file 2 is the reverse complement of file 1. If True it will return ‘1’. If false, it will return ‘2’.””””
	o Input: two strings: (barcode extracted from each read)
	o Return: 1 or 2
	o Example: input is:  CAGGTTT and AAACCTG
		Return: 1
	o Example: input is: CCTTGGAA and TTCCAANG
		Return: 2
•Create a function to determine if two reads are mis-matched or if they have non-existing barcodes. This function is called sort_unmatching_barcodes
o	Docstring: “”” This function will take the barcodes of two files. If either of the barcodes don’t exist, the function will return a ‘4’. If both barcodes exist, the function will return a ‘3’. “””
o	Input: two strings: (barcode extracted from each read)
o	Return: 3 or 4
o	Example input: CCTAGAA and TTCTAGN
		Return: 4
o	Example input: GTAGCGTA and AACAGCGA
		Return: 3
•Create a function to match sequences with mismatched / Ns for extra credit
o	This function is called sequence_corrector. 
		This will be done at a later point.
•	Create generic output name template for files
•	Open all 4 files in r mode.
•	For each read, store four consecutive lines of files R1 and R4 in separate lists.
	o Then check if the barcodes are the same (reverse complement) using the reverse_complement_check function on files R2 and R3.  This is done by comparing line 2(+4x) of each file.
		If they are the same (return value ‘1’), append the reads from files R1 and R4 to their appropriate output files. Output files names are determined by index sequence.
		If they have different barcodes (return value ‘2’) run sort_unmatching_barcodes function.
•	For extra credit, apply the sequence_corrector here.
•	If they are both existing barcodes (return value ‘3’), append the reads from files 1 and 4 to the nonmatching index pair output files. 
•	If either of them is a non-existing barcode return value ‘4’), append the reads from files 1 and 4 to the low-quality index pair files.
	o Parse 4 more lines of each file and overwrite the previous read-storing variables. And restart the loop.
```
