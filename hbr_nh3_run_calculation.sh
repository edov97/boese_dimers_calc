#!/bin/bash

# Directory containing the input files
input_directory="/home/vance/boese_dimers_calc"

# List of input files
input_files=(
    "1.28_080_psi4.in" "1.28_085_psi4.in" "1.28_090_psi4.in" "1.28_095_psi4.in"
        "1.28_100_psi4.in" "1.28_105_psi4.in" "1.28_110_psi4.in" "1.28_125_psi4.in"
            "1.28_150_psi4.in" "1.28_200_psi4.in"
            )

            # Loop through each input file and launch the calculation
            for input_file in "${input_files[@]}"; do
                output_file="${input_file%.in}.out"
                    psi4 -n 4 -i "$input_directory/$input_file" -o "$input_directory/$output_file" &
                    done

                    # Wait for all background processes to finish
                    wait
                    
