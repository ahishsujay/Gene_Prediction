# Gene Prediction Pipeline
## Overview:
A Gene Prediction pipeline that predicts coding and non-coding genes from assembled genomes using various ab-initio and homology based programs and tools. For predicting coding genes the pipeline uses GeneMarkS-2 and Prodigal, meanwhile, for predicting non-coding genes it uses ARAGORN BARRNAP and Infernal. BLAST is used to validate the results of the coding genes and provides results as false-positive or true-positives in FASTA/.fna format. 
