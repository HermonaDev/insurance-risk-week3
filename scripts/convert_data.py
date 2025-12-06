import pandas as pd


def convert_txt_to_csv(input_path, delimiter='|'):
    """Convert a text file to CSV."""
    df = pd.read_csv(input_path, delimiter=delimiter, low_memory=False)
    output_path = input_path.replace('.txt', '.csv')
    df.to_csv(output_path, index=False)
    print(f"Saved: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


if __name__ == "__main__":
    convert_txt_to_csv('data/MachineLearningRating_v3.txt')