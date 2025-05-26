import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def read_excel_file(file_path, sheet_name=0):
    """
    Read an Excel file and return a pandas DataFrame
    
    Parameters:
    - file_path: path to the Excel file
    - sheet_name: name or index of the sheet to read (default: first sheet)
    """
    try:
        # Read the Excel file
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print("\nFirst few rows of the data:")
        print(df.head())
        print("\nDataFrame Info:")
        print(df.info())
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading Excel file: {str(e)}")
        return None

def analyze_numeric_columns(df):
    """Generate basic statistics for numeric columns"""
    if df is not None:
        print("\nBasic Statistics for Numeric Columns:")
        print(df.describe())

def create_volcano_plot(df):
    """Create a volcano plot showing significance vs fold change"""
    plt.figure(figsize=(10, 8))
    
    # Calculate -log10 of adjusted p-values
    df['neg_log_pval'] = -np.log10(df['adjpv'])
    
    # Define thresholds for coloring
    fc_threshold = 0.5
    p_threshold = 0.05
    
    # Create color categories
    colors = np.where((abs(df['logfc']) > fc_threshold) & (df['adjpv'] < p_threshold), 
                     'red', 'gray')
    
    plt.scatter(df['logfc'], df['neg_log_pval'], c=colors, alpha=0.6)
    plt.axhline(y=-np.log10(p_threshold), color='k', linestyle='--', alpha=0.3)
    plt.axvline(x=fc_threshold, color='k', linestyle='--', alpha=0.3)
    plt.axvline(x=-fc_threshold, color='k', linestyle='--', alpha=0.3)
    
    # Label some top significant genes
    top_genes = df[df['adjpv'] < 0.001].sort_values('abs_fc', ascending=False).head(5)
    for _, gene in top_genes.iterrows():
        plt.annotate(gene['Gene'], 
                    (gene['logfc'], -np.log10(gene['adjpv'])),
                    xytext=(5, 5), textcoords='offset points')
    
    plt.xlabel('Log2 Fold Change')
    plt.ylabel('-log10(Adjusted P-value)')
    plt.title('Volcano Plot of Gene Expression Changes')
    plt.tight_layout()
    plt.savefig('volcano_plot.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_pathway_analysis(df):
    """Create visualizations for pathway-level analysis"""
    # Calculate mean logfc and count of genes per pathway
    pathway_stats = df.groupby('Pathway').agg({
        'logfc': ['mean', 'count', 'std'],
        'Gene': lambda x: ', '.join(x[:3])  # Show first 3 genes
    }).round(3)
    
    # Sort by absolute mean logfc
    pathway_stats = pathway_stats.sort_values(('logfc', 'mean'), key=abs, ascending=False)
    
    # Create pathway enrichment plot
    plt.figure(figsize=(12, 8))
    bars = plt.barh(y=range(len(pathway_stats)), 
                   width=pathway_stats[('logfc', 'mean')],
                   xerr=pathway_stats[('logfc', 'std')])
    plt.yticks(range(len(pathway_stats)), pathway_stats.index, fontsize=8)
    plt.xlabel('Mean Log2 Fold Change')
    plt.title('Pathway Enrichment Analysis')
    
    # Add gene counts
    for i, bar in enumerate(bars):
        count = pathway_stats[('logfc', 'count')].iloc[i]
        plt.text(bar.get_x(), i, f'n={count}', 
                ha='right', va='center')
    
    plt.tight_layout()
    plt.savefig('pathway_enrichment.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Save pathway statistics to file
    pathway_stats.to_csv('pathway_statistics.csv')

def create_group_comparison(df):
    """Create visualizations comparing different groups"""
    # Box plot of logfc by group
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='Group', y='logfc')
    plt.xticks(rotation=45)
    plt.title('Distribution of Log Fold Changes by Group')
    plt.tight_layout()
    plt.savefig('group_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Create group statistics summary
    group_stats = df.groupby('Group').agg({
        'logfc': ['mean', 'std', 'count'],
        'Gene': lambda x: len([g for g in x if abs(df.loc[df['Gene']==g, 'logfc'].iloc[0]) > 0.5])
    }).round(3)
    group_stats.columns = ['Mean LogFC', 'Std LogFC', 'Total Genes', 'Significant Genes']
    group_stats.to_csv('group_statistics.csv')

def create_heatmap_clusters(df):
    """Create clustered heatmap of genes and pathways"""
    # Pivot table for gene expression by pathway
    pivot_df = df.pivot_table(index='Pathway', columns='Group', values='logfc', aggfunc='mean')
    
    # Create clustered heatmap
    plt.figure(figsize=(12, 8))
    sns.clustermap(pivot_df, cmap='RdBu_r', center=0,
                  yticklabels=True, xticklabels=True,
                  figsize=(12, 8))
    plt.savefig('clustered_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    # Use the RNAseq LogFC file
    file_path = 'RNAseq LogFC.xlsx'
    
    # Read the Excel file
    df = read_excel_file(file_path)
    
    if df is not None:
        # Add absolute fold change column for sorting
        df['abs_fc'] = abs(df['logfc'])
        
        # Analyze the data
        analyze_numeric_columns(df)
        
        # Create all visualizations
        create_volcano_plot(df)
        create_pathway_analysis(df)
        create_group_comparison(df)
        create_heatmap_clusters(df)
        
        print("\nAnalysis complete! Generated files:")
        print("1. volcano_plot.png - Shows significance vs fold change")
        print("2. pathway_enrichment.png - Shows mean expression changes by pathway")
        print("3. group_comparison.png - Shows expression distribution by group")
        print("4. clustered_heatmap.png - Shows hierarchical clustering of pathways")
        print("5. pathway_statistics.csv - Detailed pathway-level statistics")
        print("6. group_statistics.csv - Detailed group-level statistics")

if __name__ == "__main__":
    main() 