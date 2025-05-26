import matplotlib.pyplot as plt
import numpy as np

# Example data (replace with your real data)
genes = [
    'ATF6B', 'XBP1', 'DNAJA1', 'DNAJB1', 'DNAJB2', 'HSP90AB1', 'HSPA4L', 'HSPA8',
    'HSPH1', 'UBXN1', 'UBXN6', 'EDEM2', 'DNAJC10', 'HSPA5', 'HYOU1', 'SIL1', 'EIF2S1'
]
logfc = [
    0.28, 0.28, 0.0, -0.12, 0.22, -0.10, -0.08, -0.05,
    0.0, 0.18, 0.22, 0.23, 0.25, 0.32, 0.27, 0.0, -0.12
]

# Group boundaries and labels (indices are where the vertical lines go)
group_boundaries = [0, 2, 13, 15, 17]  # last index is len(gene)
group_labels = ['ER Stress', 'Protein recognition by luminal chaperones', 'ERAD', 'Misfolded']
group_label_positions = [(0, 2), (2, 13), (13, 15), (15, 17)]

fig, ax = plt.subplots(figsize=(12, 6))

# Bar colors: red for positive, blue for negative
colors = ['red' if v > 0 else 'blue' for v in logfc]

# Draw bars
bars = ax.bar(range(len(genes)), logfc, color=colors, edgecolor='black')

# Custom x-tick labels
ax.set_xticks(range(len(genes)))
ax.set_xticklabels(genes, rotation=45, ha='right', fontsize=12, fontweight='bold', style='italic')

# Y-axis label
ax.set_ylabel('Log$_2$ Fold Change', fontsize=16)

# Title
ax.set_title('CsA vs CNT', fontsize=24, fontweight='bold')

# Draw vertical dashed lines for group boundaries
for idx in group_boundaries:
    ax.axvline(idx - 0.5, color='k', linestyle='--', linewidth=1)

# Add group labels above the plot
for label, (start, end) in zip(group_labels, group_label_positions):
    xpos = (start + end - 1) / 2
    ax.text(xpos, ax.get_ylim()[1] + 0.03, label, ha='center', va='bottom', fontsize=12)

# Adjust y-limits to make space for group labels
ax.set_ylim(ax.get_ylim()[0], ax.get_ylim()[1] + 0.08)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('custom_grouped_barplot.png', dpi=300)
plt.close()

print('Custom grouped bar plot saved as custom_grouped_barplot.png') 