#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH	--job-name=demultiplex_histogram_R4
#SBATCH --time=0-24:00:00
#SBATCH --mail-user=jjacobso@uoregon.edu
#SBATCH	--mail-type=ALL
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8


/usr/bin/time -v ./demultiplex_qul_score.py -r /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz
