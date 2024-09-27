#!/bin/bash

# Loop through all files with the pattern 1.22_080_psi4*.out
for file in 1.22*.out 1.27*.out 1.28*.out; do
	# Extract the base name without the .out extension
	base_name="${file%.out}"
	# Create the new name by appending _aug_cc_pvqz
	new_name="${base_name}_aug_cc_pvqz.out"
	# Rename the file
	mv "$file" "$new_name"
	done            
