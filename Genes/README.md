# Genes Analysis Scripts

This folder contains Python scripts and output plots for gene expression analysis of different biological pathways and processes, including Endoplasmic Reticulum (ER), Cell Cycle, and Ferroptosis.

## Contents
- `cell_cycle.py` / `cell_cycle.png`: Script and plot for cell cycle gene expression analysis (CsA and VOC groups).
- `er.py` / `ER_panel_vertical.png`: Script and plot for endoplasmic reticulum gene expression analysis (CsA and VOC groups).
- `ferroptosis.py` / `ferroptosis.png`: Script and plot for ferroptosis gene expression analysis (CsA and VOC groups).

## How to Use
1. **Edit or add gene data**: Update the relevant script (e.g., `ferroptosis.py`) with your gene names, roles, and Log2FC values.
2. **Run the script**:
   ```bash
   python3 <script_name>.py
   ```
   This will generate a PNG plot in the same folder.

## Plot Description
- Each plot shows Log2 Fold Change (Log2FC) for selected genes, grouped and labeled by biological role.
- Red bars indicate positive Log2FC; blue bars indicate negative Log2FC.
- Vertical dashed lines separate functional groups/roles.
- Group labels are positioned above each group of bars.
- The top panel is for CsA vs Control; the bottom panel is for VOC vs Control.

## Requirements
- Python 3.x
- matplotlib
- numpy

Install requirements with:
```bash
pip install matplotlib numpy
```

## Contact
For questions or suggestions, contact the repository owner. 