"""
Helper functions for insurance risk analysis.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_loss_ratio_by_group(df, group_column, title_suffix=""):
    """
    Calculate and plot loss ratio by any grouping column.
    
    Args:
        df: DataFrame with TotalPremium and TotalClaims columns
        group_column: Column to group by (e.g., 'Province', 'VehicleType')
        title_suffix: Additional text for plot title
    """
    stats = df.groupby(group_column).agg(
        TotalPremium=('TotalPremium', 'sum'),
        TotalClaims=('TotalClaims', 'sum')
    ).reset_index()
    
    stats['LossRatio'] = stats['TotalClaims'] / stats['TotalPremium']
    stats = stats.sort_values('LossRatio', ascending=False)
    
    plt.figure(figsize=(10, 6))
    top10 = stats.head(10).sort_values('LossRatio', ascending=True)
    colors = ['red' if x > 1 else 'green' for x in top10['LossRatio']]
    
    plt.barh(top10[group_column], top10['LossRatio'], color=colors)
    plt.axvline(x=1.0, color='black', linestyle='--', alpha=0.5, label='Break-even (100%)')
    plt.xlabel('Loss Ratio (Claims/Premium)')
    plt.title(f'Loss Ratio by {group_column} {title_suffix}')
    plt.legend()
    
    return stats, plt.gcf()

def detect_outliers_iqr(series):
    """
    Detect outliers using IQR method.
    
    Returns:
        outlier_mask, lower_bound, upper_bound, iqr
    """
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outlier_mask = (series < lower_bound) | (series > upper_bound)
    
    return outlier_mask, lower_bound, upper_bound, IQR