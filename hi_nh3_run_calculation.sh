#!/bin/bash

# Directory containing the input files
input_directory="/home/vance/boese_dimers_calc"

# List of input files
input_files=(
    "1.32_080_psi4.in" "1.32_085_psi4.in" "1.32_090_psi4.in" "1.32_095_psi4.in"
    "1.32_100_psi4.in" "1.32_105_psi4.in" "1.32_110_psi4.in" "1.32_125_psi4.in"
    "1.32_150_psi4.in" "1.32_200_psi4.in"
)

# Loop through each input file and launch the calculation
for input_file in "${input_files[@]}"; do
    output_file="${input_file%.in}.out"
        psi4 -n 4 -i "$input_directory/$input_file" -o "$input_directory/$output_file" &
        done

        # Wait for all background processes to finish
        wait
        
