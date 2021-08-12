#!/usr/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --job-name=Demultiplex
#SBATCH --output=/home/jjacobso/bgmp/bioinformatics/Bi622/Demultiplexing-Bi622/Assignment-the-third/Demultiplex%j.out
#SBATCH --time=0-24:00:00
#SBATCH --mail-user=jjacobso@uoregon.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8

/usr/bin/time -v ./demultiplex.py

