import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import sem
from pathlib import Path

plt.rcParams['font.family'] = 'Times New Roman'

# Get project root and construct Excel file path
project_root = Path(__file__).resolve().parent.parent
file_path = project_root / 'Excel' / '20220720 MTT.xlsx'
df = pd.read_excel(file_path)

# Clean donor names if needed (e.g., Rep 1 -> pT 6, etc.)
donor_map = {
    'Rep 1': 'pT 6',
    'Rep 2': 'pT 11',
    'Rep 3': 'pT 21',
    'Rep 4': 'pT 23',
}
df['Donor'] = df['Donor'].map(donor_map)

# Group and calculate mean and SEM
agg = df.groupby(['Drug', 'Donor', 'Concentration']).agg(
    mean_viability = ('Cell Viability', 'mean'),
    sem_viability = ('Cell Viability', sem)
).reset_index()

# Plotting function
def plot_dose_response(drug, out_path):
    data = agg[agg['Drug'] == drug]
    plt.figure(figsize=(6, 5))
    ax = plt.gca()
    donors = data['Donor'].unique()
    palette = ['#E9967A', '#228B22', '#20B2AA', '#DA70D6']  # match example colors
    markers = ['o', 'o', 'o', 'o']
    linestyles = ['-', '--', '-', '--']
    for i, donor in enumerate(donors):
        d = data[data['Donor'] == donor]
        ax.errorbar(
            d['Concentration'], d['mean_viability'], yerr=d['sem_viability'],
            label=donor, color=palette[i % len(palette)], marker=markers[i % len(markers)],
            linestyle=linestyles[i % len(linestyles)], linewidth=2, markersize=7, capsize=4
        )
    ax.set_xscale('log')
    ax.set_xticks([0.01, 0.1, 1, 10])
    ax.get_xaxis().set_major_formatter(plt.ScalarFormatter())
    ax.set_xlabel('Concentration (μM)', fontsize=14)
    ax.set_ylabel('Cell Viability (%)', fontsize=14)
    ax.set_ylim(-1, 1)  # Updated y-axis limit for ferroptosis
    ax.set_xlim(0.008, 12)
    ax.grid(True, axis='y', linestyle='-', alpha=0.2)
    # Panel label
    ax.text(0.5, 1.13, drug, fontsize=18, fontweight='bold', ha='center', va='top', transform=ax.transAxes,
            bbox=dict(facecolor='#cccccc', edgecolor='none', boxstyle='round,pad=0.3'))
    # Title
    ax.set_title('48 Hour CNI Exposure', fontsize=20, fontweight='bold', pad=30)
    # Legend
    ax.legend(title='Donor', fontsize=12, title_fontsize=13, loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.savefig(out_path, dpi=300)
    plt.close()

plot_dose_response('CsA', 'Dose Response/CsA_dose_response.png')
plot_dose_response('VOC', 'Dose Response/VOC_dose_response.png')

print('Dose response plots saved in Dose Response/') 