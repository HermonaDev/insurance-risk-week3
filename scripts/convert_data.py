import pandas as pd
import sys
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def convert_txt_to_csv(input_path, delimiter='|'):
    """
    Convert a text file to CSV with error handling.
    
    Args:
        input_path (str): Path to input .txt file
        delimiter (str): Delimiter used in the text file
    
    Returns:
        pandas.DataFrame: Loaded dataframe
    """
    try:
        # Check if file exists
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        logger.info(f"Loading data from {input_path} with delimiter '{delimiter}'")
        
        # Read the text file
        df = pd.read_csv(input_path, delimiter=delimiter, low_memory=False)
        
        # Create output path
        output_path = input_path.replace('.txt', '.csv')
        
        # Save as CSV
        df.to_csv(output_path, index=False)
        
        logger.info(f"Conversion complete: {df.shape[0]:,} rows, {df.shape[1]:,} columns")
        logger.info(f"Output saved to: {output_path}")
        
        # Basic validation
        logger.info(f"TotalPremium sum: R{df['TotalPremium'].sum():,.2f}")
        logger.info(f"TotalClaims sum: R{df['TotalClaims'].sum():,.2f}")
        
        return df
        
    except Exception as e:
        logger.error(f"Error during conversion: {str(e)}")
        raise


if __name__ == "__main__":
    try:
        # Default paths
        input_file = 'data/MachineLearningRating_v3.txt'
        
        # Convert
        df = convert_txt_to_csv(input_file, delimiter='|')
        
        print("\nFirst 3 rows of converted data:")
        print(df.head(3))
        
    except Exception as e:
        print(f"\n❌ Conversion failed: {e}")
        sys.exit(1)