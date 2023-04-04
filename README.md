# robust_monitoring_organoid_growth

This repository reproduces the results of the paper x

Requirements

1. Install conda
2. Create environment and install conda
1. Download data from and unpack in data/

<img src='plots/example_gt_segmentation.png'
     alt="Markdown Monster icon"
     style="float: center; margin-right: 10px; height:300px" />

Results from data_analysis.ipynb
1. Comparison of segmentation performance

<img src='results/dice_scores_segformer_vs_morgana.png'
     style="float: center; margin-right: 10px; height:300px" />

<img src='results/dice_scores_per_day_segformer_vs_morgana.png'
     style="float: center; margin-right: 10px; height:300px" />

2. Comparison of predictions

<img src='plots/morgana_mlp_c_vs_segformer_one_example_per_day_selected.png'
     style="float: center; margin-right: 10px; height:700px" />

3. Comparison of growth monitoring

<img src='plots/gt_vs_morgana_vs_segformer_org_size.png'
     alt="Markdown Monster icon"
     style="float: center; margin-right: 10px; height:300px" />

<img src='plots/gt_vs_morgana_vs_segformer_org_size_rel_to_wt.png'
     alt="Markdown Monster icon"
     style="float: center; margin-right: 10px; height:300px" />