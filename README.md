# CNI (Cellular Network Investigation)

A Python-based toolkit for analyzing and visualizing RNA-seq data, with a focus on cellular networks and pathway analysis.

## Overview

CNI is a comprehensive data analysis and visualization toolkit designed for processing RNA-seq data, particularly focusing on cellular networks and pathway analysis. The project provides various tools for data processing, statistical analysis, and generation of publication-quality visualizations.

## Features

- **Excel Data Processing**: Read and process RNA-seq data from Excel files
- **Statistical Analysis**: Perform basic statistical analysis on numeric columns
- **Visualization Tools**:
  - Volcano plots for differential expression analysis
  - Pathway enrichment analysis
  - Group comparison visualizations
  - Clustered heatmaps
  - Custom grouped bar plots
  - PCA plots
  - Box plots

## Requirements

- Python 3.x
- Required packages (see requirements.txt):
  - matplotlib >= 3.7.1
  - seaborn >= 0.12.2
  - networkx >= 3.1
  - plotly >= 5.15.0
  - numpy >= 1.24.3
  - pandas >= 2.0.2

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/CNI.git
cd CNI
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Main Analysis Pipeline

The main analysis pipeline can be run using the `excel_reader.py` script:

```bash
python excel_reader.py
```

This will:
1. Read the RNA-seq data from 'RNAseq LogFC.xlsx'
2. Generate various visualizations:
   - Volcano plot (volcano_plot.png)
   - Pathway enrichment analysis (pathway_enrichment.png)
   - Group comparison (group_comparison.png)
   - Clustered heatmap (clustered_heatmap.png)
3. Generate statistical summaries:
   - Pathway statistics (pathway_statistics.csv)
   - Group statistics (group_statistics.csv)

### Custom Visualizations

The project includes several scripts for custom visualizations:

1. Custom Bar Plot:
```bash
python custom_barplot.py
```

2. Gene Bar Plot from Excel:
```bash
python gene_barplot_from_excel.py
```

## Output Files

The analysis generates several output files:

- **Visualizations**:
  - volcano_plot.png
  - pathway_enrichment.png
  - group_comparison.png
  - clustered_heatmap.png
  - custom_grouped_barplot.png
  - gene_barplot_from_excel.png
  - rnaseq_pca.png
  - rnaseq_heatmap.png
  - rnaseq_boxplot.png

- **Statistical Summaries**:
  - pathway_statistics.csv
  - group_statistics.csv

## Project Structure

```
CNI/
├── excel_reader.py          # Main analysis pipeline
├── custom_barplot.py        # Custom bar plot generation
├── gene_barplot_from_excel.py # Gene expression bar plots
├── graph_examples.py        # Example visualizations
├── requirements.txt         # Project dependencies
├── RNAseq LogFC.xlsx        # Input data file
└── Genes/                   # Gene-related data
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

