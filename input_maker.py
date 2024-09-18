from AaronTools.geometry import Geometry
from AaronTools.theory import Theory, SAPTMethod, SinglePointJob
import os

sapt_theory = Theory(
    method=SAPTMethod("sapt(DFT)"),
    basis="aug-cc-pVQZ",
    job_type="energy",
    charge=[0, 0, 0],  # net charge, and the charge on both monomers
    multiplicity=[1, 1, 1],  # overall multiplicity, and multiplicity of both monomers
    memory=8,
    processors=4,
    settings={
        "sapt_dft_functional" : "PBE0",
        "scf_type": "DF",
        "freeze_core": "true",
        "sapt_dft_grac_shift_a": "0.116251", 
        "sapt_dft_grac_shift_b": "0.113162", 
        "sapt_dft_do_hybrid": "true",
        "do_ind_exch_sinf":   "true",
        "do_disp_exch_sinf":  "true",
    },
)

# Directory containing the .xyz files
input_directory = "/home/vance/NCIAtlas/geometries/NCIA_HB300SPXx10"
# Directory to save the output files
output_directory = "/home/vance/boese_dimers_calc"

# List of .xyz files to process
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
        input_path = os.path.join(input_directory, xyz_file)
        combined_structure = Geometry(input_path)
        combined_structure.components = [
            Geometry(combined_structure.find("1-2")),
            Geometry(combined_structure.find("3-6")),
            ]
        output_filename = f"{os.path.splitext(xyz_file)[0]}_psi4.in"
        output_path = os.path.join(output_directory, output_filename)
        combined_structure.write(
            outfile=output_path,
            style="psi4",
            theory=sapt_theory,
        )
                            
