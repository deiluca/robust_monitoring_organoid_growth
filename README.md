# A large brain organoid dataset reveals extensive improvement potential of state-of-the-art analysis pipelines

This repository reproduces the results of the paper *A large brain organoid dataset reveals extensive improvement potential of state-of-the-art analysis pipelines*.

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

Download the data from [Zenodo](https://zenodo.org/records/10301912) and unpack it in data/

## Visualization of results

All results below are generated in [data_analysis.ipynb](data_analysis.ipynb).

### Example of image and corresponding annotation

<img src='plots/example_gt_segmentation.svg'
     alt="Markdown Monster icon"
     style="float: center; margin-right: 10px; height:250px" />

### Comparison of segmentation performance

<img src='plots/dice_score_distribution.svg'
     style="float: center; margin-right: 10px; height:340px" />

<img src='plots/dice_scores_per_day.svg'
     style="float: center; margin-right: 10px; height:300px" />

### Analysis of predictions

<img src='plots/qualitative_comparison_org3_days_2_8_10_16_30.svg'
     style="float: center; margin-right: 10px; height:1000px" />

### Comparison of growth monitoring

<img src='plots/org_sizes_both_labs_distinct_mm2.svg'
     alt="Markdown Monster icon"
     style="float: center; margin-right: 10px; height:400px" />

### Clone diversity

<img src='plots/clone_similarity.svg'
     alt="Markdown Monster icon"
     style="float: center; margin-right: 10px; height:300px" />

### SegFormer re-training
Please use the [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) repository and the scripts located in [model_training/SegFormer](model_training/SegFormer).

The configuration files `segformer_mit-b0.py`, `schedule_160k.py`, and `default_runtime.py`, referenced in the [training config files](model_training/SegFormer/config_files_training/split-0.py), are available in the [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) repository. These files have not been modified from their original versions.

The data structure required for training the SegFormer model is as follows:
```
images
└── split0_test/
    ├── xxx.jpg
    ├── xxy.jpg
    └── [...]
└── split0_training/
    └── xxz.jpg
    └── [...]
└── split1_test/
    ├── 123.jpg
    └── [...]
└── [...]

masks
└── split0_test/
    ├── xxx_label.tif
    ├── xxy_label.tif
    └── [...]
└── split0_training/
    └── xxz_label.tif
    └── [...]
└── split1_test/
    ├── 123_label.tif
    └── [...]
└── [...]
```
