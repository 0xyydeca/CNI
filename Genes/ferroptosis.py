import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

plt.rcParams['font.family'] = 'Times New Roman'

# Data from screenshots
voc_data = {
    'SAT1': -0.157, 'VDAC3': -0.178,
    'TFRC': -0.259, 'CP': 0.821
}
voc_roles = {
    'SAT1': 'Oxidative Damage', 'VDAC3': 'Oxidative Damage',
    'TFRC': 'Iron Transport', 'CP': 'Iron Transport'
}
csa_data = {
    'ACSL1': 0.405, 'SAT2': 0.319,
    'TFRC': -0.42, 'PCBP2': 0.22,
    'VDAC3': -0.19, 'ATG7': -0.139,
    'TP53': -0.975
}
csa_roles = {
    'ACSL1': 'Lipid Metabolism', 'SAT2': 'Lipid Metabolism',
    'TFRC': 'Iron Transport', 'PCBP2': 'Iron Transport',
    'VDAC3': 'Oxidative Damage', 'ATG7': 'Oxidative Damage',
    'TP53': 'Antioxidant Defense'
}

role_order = [
    'Lipid Metabolism', 'Iron Transport', 'Oxidative Damage', 'Antioxidant Defense'
]

# VOC panel data (sorted by Log2FC within each role)
voc_genes = []
voc_vals = []
voc_roles_for_plot = []
for role in role_order:
    role_genes = [(gene, fc) for gene, fc in voc_data.items() if voc_roles.get(gene) == role]
    role_genes_sorted = sorted(role_genes, key=lambda x: x[1])
    for gene, fc in role_genes_sorted:
        voc_genes.append(gene)
        voc_vals.append(fc)
        voc_roles_for_plot.append(role)

# CsA panel data (sorted by Log2FC within each role)
csa_genes = []
csa_vals = []
csa_roles_for_plot = []
for role in role_order:
    role_genes = [(gene, fc) for gene, fc in csa_data.items() if csa_roles.get(gene) == role]
    role_genes_sorted = sorted(role_genes, key=lambda x: x[1])
    for gene, fc in role_genes_sorted:
        csa_genes.append(gene)
        csa_vals.append(fc)
        csa_roles_for_plot.append(role)

def get_boundaries_and_positions(roles_for_plot):
    boundaries = []
    role_labels = []
    role_positions = []
    start = 0
    for role in role_order:
        count = sum(1 for r in roles_for_plot if r == role)
        if count > 0:
            end = start + count
            boundaries.append(end)
            role_labels.append(role)
            role_positions.append((start, end))
            start = end
    boundaries = boundaries[:-1]
    return boundaries, role_labels, role_positions

voc_boundaries, voc_role_labels, voc_role_positions = get_boundaries_and_positions(voc_roles_for_plot)
csa_boundaries, csa_role_labels, csa_role_positions = get_boundaries_and_positions(csa_roles_for_plot)

voc_n = len(voc_genes)
csa_n = len(csa_genes)
fig_width = 33
width_ratios = [csa_n, voc_n]
total = sum(width_ratios)
fig = plt.figure(figsize=(fig_width, 12))
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 1])

# CsA panel (top)
ax_csa = fig.add_axes([0.08, 0.55, csa_n/total*0.85, 0.35])
csa_x = np.arange(len(csa_genes))
csa_colors = ['red' if v > 0 else 'blue' for v in csa_vals]
ax_csa.bar(csa_x, csa_vals, color=csa_colors, edgecolor='black')
ax_csa.set_title('CsA vs Control', fontsize=20, fontweight='bold')
ax_csa.set_xticks(csa_x)
ax_csa.set_xticklabels(csa_genes, rotation=45, ha='right', fontsize=14, fontweight='bold', style='italic')
# ax_csa.set_xlabel('Gene', fontsize=16, fontweight='bold', labelpad=12)
ax_csa.set_ylim(-1.15, 0.75)
ax_csa.set_xlim(-0.5, len(csa_genes) - 0.5)
ax_csa.yaxis.grid(True, linestyle='--', alpha=0.5)
for idx in csa_boundaries:
    ax_csa.axvline(idx - 0.5, color='k', linestyle='--', linewidth=1.5)
ylim = ax_csa.get_ylim()
label_y = ylim[0] + (ylim[1] - ylim[0]) * 0.85
for label, (start, end) in zip(csa_role_labels, csa_role_positions):
    xpos = (start + end - 1) / 2
    ax_csa.text(xpos, label_y, label, ha='center', va='bottom', fontsize=13, fontweight='bold', clip_on=False)
ax_csa.set_ylabel('Log$_2$ Fold Change', fontsize=18, labelpad=15)
ax_csa.tick_params(axis='y', labelsize=16)
for label in ax_csa.get_yticklabels():
    label.set_fontweight('bold')

# VOC panel (bottom)
ax_voc = fig.add_axes([0.08, 0.08, voc_n/total*0.85, 0.35])
voc_x = np.arange(len(voc_genes))
voc_colors = ['red' if v > 0 else 'blue' for v in voc_vals]
ax_voc.bar(voc_x, voc_vals, color=voc_colors, edgecolor='black')
ax_voc.set_title('VOC vs Control', fontsize=20, fontweight='bold')
ax_voc.set_xticks(voc_x)
ax_voc.set_xticklabels(voc_genes, rotation=45, ha='right', fontsize=14, fontweight='bold', style='italic')
ax_voc.set_xlabel('Gene', fontsize=16, labelpad=12)
ax_voc.set_ylim(-1.15, 0.75)
ax_voc.set_xlim(-0.5, len(voc_genes) - 0.5)
ax_voc.yaxis.grid(True, linestyle='--', alpha=0.5)
for idx in voc_boundaries:
    ax_voc.axvline(idx - 0.5, color='k', linestyle='--', linewidth=1.5)
ylim = ax_voc.get_ylim()
label_y = ylim[0] + (ylim[1] - ylim[0]) * 0.85
for label, (start, end) in zip(voc_role_labels, voc_role_positions):
    xpos = (start + end - 1) / 2
    ax_voc.text(xpos, label_y, label, ha='center', va='bottom', fontsize=13, fontweight='bold', clip_on=False)
ax_voc.set_ylabel('Log$_2$ Fold Change', fontsize=18, labelpad=15)
ax_voc.tick_params(axis='y', labelsize=16)
for label in ax_voc.get_yticklabels():
    label.set_fontweight('bold')

fig.suptitle('Ferroptosis', fontsize=26, fontweight='bold', y=0.98, x=0.08, ha='left')
plt.savefig('Genes/ferroptosis.png', dpi=300, bbox_inches='tight')
plt.close()

print('Vertical panel Ferroptosis bar plot saved as Genes/ferroptosis.png') 