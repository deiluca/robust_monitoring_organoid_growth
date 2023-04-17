# A large brain organoid dataset for improving state-of-the-art analysis pipelines

This repository reproduces the results of the paper x

## Installation
```
git clone https://github.com/deiluca/robust_monitoring_organoid_growth
```
Install conda environment
```
cd path/to/robust_monitoring_organoid_growth
conda env create -f environment.yml
```

Activate the conda environment:

```
conda activate rob_monit_org_growth
```

## Data preparation

Download the data from [Zenodo](https://zenodo.org/deposit/7836864) and unpack it in data/

## Visualization of results


All results below are generated in [data_analysis.ipynb](data_analysis.ipynb).

### Example of image and corresponding annotation

<img src='plots/example_gt_segmentation.png'
     alt="Markdown Monster icon"
     style="float: center; margin-right: 10px; height:250px" />

### Comparison of segmentation performance

<img src='plots/dice_scores_segformer_vs_morgana.png'
     style="float: center; margin-right: 10px; height:340px" />

<img src='plots/dice_scores_per_day_segformer_vs_morgana.png'
     style="float: center; margin-right: 10px; height:300px" />

### Analysis of predictions

<img src='plots/morgana_mlp_c_vs_segformer_one_example_per_day_selected.png'
     style="float: center; margin-right: 10px; height:1000px" />

### Comparison of growth monitoring

<img src='plots/gt_vs_morgana_vs_segformer_org_size.png'
     alt="Markdown Monster icon"
     style="float: center; margin-right: 10px; height:300px" />

<img src='plots/gt_vs_morgana_vs_segformer_org_size_rel_to_wt.png'
     alt="Markdown Monster icon"
     style="float: center; margin-right: 10px; height:300px" />