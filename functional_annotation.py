#!/usr/bin/env python2

import pandas as pd
import subprocess
import os

#logger

#function for clustering

#functions for ab-initio tools

def signalp(path_to_gpresults):

    #Note: If the tool is not on your path, it needs to be run from the directory where the executable script for the tool is present
	# the variable tool should contain the path to where the executable file is.

	#getting a list of input(.faa) files:
	input_files_command = 'ls '+ path_to_gpresults + '*.faa'
	input_files = subprocess.check_output(input_files_command,shell=True)
	input_files = input_files.split('\n')

	print("Running SignalP ...")

	change_dir = ["cd",tool]
	subprocess.call(change_dir)

	for file_name in input_files:
		output_file = outputPath+"/signalp_"+file_name.split("/")[-1].replace(".faa","")
		sp5_command = "signalp -fasta "+file_name+" -org gram- -format short -prefix "+output_file+" -gff3"
    		subprocess.call(sp5_command.split())

	print("Finished predicting signal peptides!")

    return None

def tmhmm():

    #Note: If the tool is not on your path, it needs to be run from the directory where the executable script for the tool is present
	#the variable tool should contain the path to where the executable file is.

	#getting a list of input(.faa) files:
	path_to_gpresults = "/home/projects/group-a/Team1-GenePrediction/results/dfast_results/" #path to the gene prediction results directory
	input_files_command = 'ls '+ path_to_gpresults + '*.faa'
	input_files = subprocess.check_output(input_files_command,shell=True)
	input_files = input_files.split('\n')

	change_dir = ["cd",tool]
	subprocess.call(change_dir)

	print("Running TMHMM...")

	for file_name in input_files:
		output_file = outputPath+"/tmhmm_"+file_name.split("/")[-1].replace(".faa","")
		tmhmm_command = "tmhmm "+file_name+" | tee "+output_file+".gff3"
	   	os.system(tmhmm_command)

    return None

#homology tools

#processing the data to create gff files

#wrapper function

#main

def main():

    path_to_gpresults = "Contains path to the input files" #path to the gene prediction results directory

    return None

if __name__ == "__main__":
    main()
