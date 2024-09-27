#!/bin/bash

# Directory containing the input files
input_directory="/home/vance/boese_dimers_calc/sapt2+mp2"

# List of input files
input_files=(
    "1.22_080_psi4.in" "1.22_085_psi4.in" "1.22_090_psi4.in" "1.22_095_psi4.in"
    "1.22_100_psi4.in" "1.22_105_psi4.in" "1.22_110_psi4.in" "1.22_125_psi4.in"
    "1.22_150_psi4.in" "1.22_200_psi4.in" "1.27_080_psi4.in" "1.27_085_psi4.in"
    "1.27_090_psi4.in" "1.27_095_psi4.in" "1.27_100_psi4.in" "1.27_105_psi4.in"
    "1.27_110_psi4.in" "1.27_125_psi4.in" "1.27_150_psi4.in" "1.27_200_psi4.in"
    "1.28_080_psi4.in" "1.28_085_psi4.in" "1.28_090_psi4.in" "1.28_095_psi4.in"
    "1.28_100_psi4.in" "1.28_105_psi4.in" "1.28_110_psi4.in" "1.28_125_psi4.in"
    "1.28_150_psi4.in" "1.28_200_psi4.in" "1.32_080_psi4.in" "1.32_085_psi4.in"
    "1.32_090_psi4.in" "1.32_095_psi4.in" "1.32_100_psi4.in" "1.32_105_psi4.in"
    "1.32_110_psi4.in" "1.32_125_psi4.in" "1.32_150_psi4.in" "1.32_200_psi4.in"
)
# Loop through each input file and launch the calculation
for input_file in "${input_files[@]}"; do
	output_file="${input_file%.in}.out"
        	psi4 -n 8 -i "$input_directory/$input_file" -o "$input_directory/$output_file" &
        	done
# Wait for all background processes to finish
		wait
                    
