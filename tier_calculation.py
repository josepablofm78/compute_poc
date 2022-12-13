import os
from pathlib import Path
import json
import glob

INPUTS_PATH = os.environ.get("NEVERMINED_INPUTS_PATH")
OUTPUTS_PATH = os.environ.get("NEVERMINED_OUTPUTS_PATH")

image_weight = 2
vcf_weight = 4
basic_info_weight = 1

def tier_calculation():
    """Calculates the Tier of a user depending on the data provided"""
    print(f"PATH: {INPUTS_PATH}")
    
    basic_info_files = len(glob.glob1(INPUTS_PATH, "*.json"))
    print(f"Found {basic_info_files} json files ")

    vcf_files = len(glob.glob1(INPUTS_PATH, "*.vcf"))
    print(f"Found {vcf_files} vcf files ")

    image_files = len(glob.glob1(INPUTS_PATH, "*.jpeg")) + len(glob.glob1(INPUTS_PATH, "*.jpg")) + len(glob.glob1(INPUTS_PATH, "*.png")) + len(glob.glob1(INPUTS_PATH, "*.gif"))
    print(f"Found {image_files} vcf files ")

    tier = (basic_info_files * basic_info_weight) + (vcf_files * vcf_weight) + (image_files * image_weight)
    print(f"Calculated Tier: {tier}")

    result_json = json.dumps({'tier': tier})
    output_file = Path(OUTPUTS_PATH) / "result.json"
    with output_file.open("w") as f:
         f.write(result_json)

    print(f"Generated output file: {output_file.as_posix()}")

if __name__ == "__main__":
   tier_calculation()