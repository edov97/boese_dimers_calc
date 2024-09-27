from AaronTools.geometry import Geometry
from AaronTools.theory import Theory, SAPTMethod, SinglePointJob
import os

# Function to get the basis set based on the file name
def get_basis(file_name):
    if file_name.startswith("1.22") or file_name.startswith("1.27") or file_name.startswith("1.28"):
        return "aug-cc-pVQZ"
    elif file_name.startswith("1.32"):
        return "def2-qzvp"

# Function to get the sapt_dft_grac_shift_a value based on the file name
def get_sapt_dft_grac_shift_a(file_name):
    if file_name.startswith("1.22") or file_name.startswith("1.27"):
        return "0.116251"
    elif file_name.startswith("1.28"):
        return "0.106591"
    elif file_name.startswith("1.32"):
        return "0.094577"

# Function to get the sapt_dft_grac_shift_b value based on the file name
def get_sapt_dft_grac_shift_b(file_name):
    if file_name.startswith("1.22") or file_name.startswith("1.28") or file_name.startswith("1.32"):
        return "0.113162"
    elif file_name.startswith("1.27"):
        return "0.074627"

# Directory containing the .xyz files
input_directory = "/home/vance/NCIAtlas/geometries/NCIA_HB300SPXx10"
# Directory to save the output files
output_directory = "/home/vance/boese_dimers_calc/sapt2+mp2"

# List of .xyz files to process in the input directory
xyz_files = [
    "1.22_080.xyz", "1.22_085.xyz", "1.22_090.xyz", "1.22_095.xyz",
    "1.22_100.xyz", "1.22_105.xyz", "1.22_110.xyz", "1.22_125.xyz",
    "1.22_150.xyz", "1.22_200.xyz", "1.27_080.xyz", "1.27_085.xyz",
    "1.27_090.xyz", "1.27_095.xyz", "1.27_100.xyz", "1.27_105.xyz",
    "1.27_110.xyz", "1.27_125.xyz", "1.27_150.xyz", "1.27_200.xyz",
    "1.28_080.xyz", "1.28_085.xyz", "1.28_090.xyz", "1.28_095.xyz",
    "1.28_100.xyz", "1.28_105.xyz", "1.28_110.xyz", "1.28_125.xyz",
    "1.28_150.xyz", "1.28_200.xyz", "1.32_080.xyz", "1.32_085.xyz",
    "1.32_090.xyz", "1.32_095.xyz", "1.32_100.xyz", "1.32_105.xyz",
    "1.32_110.xyz", "1.32_125.xyz", "1.32_150.xyz", "1.32_200.xyz"
]



for xyz_file in xyz_files:
    input_file = os.path.join(input_directory, xyz_file) # using .os get the .xyz files from the input directory
    combined_structure = Geometry(input_file)
    # Update the structure based on the file name i.e. the system passed
    if xyz_file.startswith("1.27"):
        combined_structure.components = [
            Geometry(combined_structure.find("1-2")),
            Geometry(combined_structure.find("3-13")),
            ]
    else:
        combined_structure.components = [
                Geometry(combined_structure.find("1-2")),
                Geometry(combined_structure.find("3-6")),
                ]
    # Now create the theory object with variable values 
    sapt_theory = Theory(
        method=SAPTMethod("sapt2+dmp2"),
        basis=get_basis(xyz_file), #Different basis set based on the system (we are using def2-qzvpp for Iodine since aug-cc-PVQZ is currently not available for this element)
        job_type="energy",
        charge=[0, 0, 0],  # net charge, and the charge on both monomers
        multiplicity=[1, 1, 1],  # overall multiplicity, and multiplicity of both monomers
        memory=8,
        processors=4,
        settings={
            "scf_type": "DF",
            "freeze_core": "false",
            "do_ind_exch_sinf":   "true",
            "do_disp_exch_sinf":  "true",
        },
    )
    output_filename = f"{os.path.splitext(xyz_file)[0]}_psi4.in"
    output_file = os.path.join(output_directory, output_filename)
    combined_structure.write(
        outfile=output_file,
        style="psi4",
        theory=sapt_theory,
    )
                            
