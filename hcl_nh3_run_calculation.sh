#!/bin/bash

# Directory containing the input files
input_directory="/home/vance/boese_dimers_calc"

# List of input files
input_files=(
    "1.22_080_psi4.in" "1.22_085_psi4.in" "1.22_090_psi4.in" "1.22_095_psi4.in"
    "1.22_100_psi4.in" "1.22_105_psi4.in" "1.22_110_psi4.in" "1.22_125_psi4.in"
    "1.22_150_psi4.in" "1.22_200_psi4.in"
)
# Loop through each input file and launch the calculation
for input_file in "${input_files[@]}"; do
	output_file="${input_file%.in}.out"
        	psi4 -n 4 -i "$input_directory/$input_file" -o "$input_directory/$output_file" &
        	done
# Wait for all background processes to finish
		wait
                    
