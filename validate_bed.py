import sys
import pandas as pd

def validate_bed(file_path):
    try:
        # Load the BED file
        bed = pd.read_csv(file_path, sep='\t', header=None, comment='#')

        # Check for minimum required columns (chrom, start, end)
        if bed.shape[1] < 3:
            raise ValueError("BED file must have at least 3 columns: chrom, start, end")

        # Check if start and end columns are integers
        if not pd.api.types.is_integer_dtype(bed[1]) or not pd.api.types.is_integer_dtype(bed[2]):
            raise ValueError("Start and end columns must be integers")

        # Check if start <= end
        if not (bed[1] <= bed[2]).all():
            raise ValueError("Start positions must be less than or equal to end positions")

        print("BED file is valid.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_bed.py <path_to_bed_file>")
        sys.exit(1)

    bed_file_path = sys.argv[1]
    validate_bed(bed_file_path)

