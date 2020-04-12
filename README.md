# Gene Prediction Pipeline
## Overview:
A Gene Prediction pipeline that predicts coding and non-coding genes from assembled genomes using various ab-initio and homology based programs and tools. For predicting coding genes the pipeline uses GeneMarkS-2 and Prodigal, meanwhile, for predicting non-coding genes it uses ARAGORN, BARRNAP, RNAmmer and Infernal. BLAST is used to validate the results of the coding genes and provides results as false-positive or true-positives in FASTA/.fna format.

## Pipeline Requirements:
1. [PRODIGAL](https://github.com/hyattpd/Prodigal). Or: `conda install -c bioconda prodigal`
2. [GeneMarkS-2](http://exon.gatech.edu/GeneMark/license_download.cgi).
> NOTE: If GeneMarkS-2 is being ran/downloaded on a MacOS then you would have to download the "64 bit key" along with GeneMarkS-2 and execute the following command once the files have been downloaded: `cp gm_key_64 ~/.gm_key_64`
3. [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download). Or: `install -c bioconda blast` <br />
4. [BEDTools](https://bedtools.readthedocs.io/en/latest/content/installation.html).
5. [ARAGORN](http://130.235.244.92/ARAGORN/Downloads/).
6. [BARRNAP](https://github.com/tseemann/barrnap). Or: `conda install -c bioconda -c conda-forge barrnap`
7. [Infernal](http://eddylab.org/infernal/). Or: `conda install -c bioconda infernal`
8. [RNAmmer](https://services.healthtech.dtu.dk/cgi-bin/sw_request)

NOTE: Once downloaded, all tools are assumed to be installed onto your respective PATH.

## Script execution:
`python3 pipeline.py -i <assembled genome(s)> -org_cds <organism of interest's CDS file> -o <output directory name>`
