# Gene Prediction Pipeline
## Overview:
A Gene Prediction pipeline that predicts coding and non-coding genes from assembled genomes using various ab-initio and homology based programs and tools. For predicting coding genes the pipeline uses GeneMarkS-2 and Prodigal, meanwhile, for predicting non-coding genes it uses ARAGORN, BARRNAP, RNAmmer and Infernal. BLAST is used to validate the results of the coding genes and provides results as false-positive or true-positives in FASTA/.fna format.

## Pipeline Requirements:
## Coding:
1. [PRODIGAL](https://github.com/hyattpd/Prodigal) Alternatively, easier to install through conda: `conda install -c bioconda prodigal`
2. [GeneMarkS-2](http://exon.gatech.edu/GeneMark/license_download.cgi)
3. [BLAST](ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST) Alternatively, easier to install through conda: `install -c bioconda blast` <br />

## Non-coding:
1. [ARAGORN]
2. [BARRNAP]
3. [Infernal]
4. RNAmmer
