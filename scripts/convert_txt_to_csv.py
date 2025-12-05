import pandas as pd
import sys
from pathlib import Path

def convert_txt_to_csv(input_path, delimiter='\t'):
    """
    Convert a text file to CSV.
    
    Args:
        input_path (str): Path to input .txt file
        delimiter (str): Delimiter used in the text file
    """
    input_path = Path(input_path)
    
    # Read the text file
    df = pd.read_csv(input_path, delimiter=delimiter)
    
    # Create output path
    output_path = input_path.parent / f"{input_path.stem}.csv"
    
    # Save as CSV
    df.to_csv(output_path, index=False)
    
    print(f"Conversion complete.")
    print(f"Input: {input_path} ({len(df)} rows, {len(df.columns)} columns)")
    print(f"Output: {output_path}")
    
    return df, output_path

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        delimiter = sys.argv[2] if len(sys.argv) > 2 else '\t'
    else:
        input_file = 'data/MachineLearningRating_v3.txt'
        delimiter = '|'  
    
    df, output_path = convert_txt_to_csv(input_file, delimiter)
    print("\nFirst 5 rows:")
    print(df.head())