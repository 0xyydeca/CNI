import pandas as pd
import matplotlib.pyplot as plt
import sys

# Read gene list from genes.txt
with open('genes.txt') as f:
    GENES_TO_PLOT = [line.strip() for line in f if line.strip()]

# Read group/comparison from command line argument, or use the first available group
GROUP_TO_PLOT = None
if len(sys.argv) > 1:
    GROUP_TO_PLOT = sys.argv[1]

# Read the Excel file
df = pd.read_excel('RNAseq LogFC.xlsx')

# If no group specified, use the first available group
if 'Group' in df.columns:
    if GROUP_TO_PLOT is None:
        GROUP_TO_PLOT = df['Group'].unique()[0]
    df = df[df['Group'] == GROUP_TO_PLOT]

# Filter for the specified genes (preserving order)
gene_df = df[df['Gene'].isin(GENES_TO_PLOT)]
gene_df = gene_df.set_index('Gene').reindex(GENES_TO_PLOT).reset_index()

# Plot
plt.figure(figsize=(10, 6))
colors = ['red' if v > 0 else 'blue' for v in gene_df['logfc']]
plt.bar(gene_df['Gene'], gene_df['logfc'], color=colors, edgecolor='black')
plt.ylabel('Log$_2$ Fold Change', fontsize=14)
plt.xlabel('Gene', fontsize=14)
plt.title(f'{GROUP_TO_PLOT} Log$_2$ Fold Change', fontsize=18)
plt.xticks(rotation=45, ha='right', fontsize=12, fontweight='bold', style='italic')
plt.tight_layout()
plt.savefig(f'gene_barplot_{GROUP_TO_PLOT.replace(" ", "_")}.png', dpi=300)
plt.close()

print(f'Bar plot saved as gene_barplot_{GROUP_TO_PLOT.replace(" ", "_")}.png') 