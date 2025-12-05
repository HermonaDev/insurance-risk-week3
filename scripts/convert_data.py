import pandas as pd
import sys

def main():
    # Read raw TXT (pipe separated)
    df = pd.read_csv('data/MachineLearningRating_v3.txt', delimiter='|', low_memory=False)
    
    # Save as CSV
    df.to_csv('data/raw_insurance.csv', index=False)
    print(f"Saved: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # Basic validation
    print(f"TotalPremium sum: R{df['TotalPremium'].sum():,.2f}")
    print(f"TotalClaims sum: R{df['TotalClaims'].sum():,.2f}")
    
if __name__ == "__main__":
    main()