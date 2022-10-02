# projection-pursuit-index

This is the repository for the paper "xxx" by Zhaoxing Wu and Chunming Zhang.

All data used in the paper is contained in the folder `./data`. Plots used in the paper is contained in the folder `./output`. `./script` includes all the code.

- `./script/fun.R`: useful functions used by the following scripts. Include S(), plot_test_train(), acc(), cross_validation().
- `./script/simulated_example.Rmd`: simulate datasets under 4 different conditions, including `./data/1_perc_imp_var.csv`, `./data/2_ratio_dim_obs.csv`, `./data/3_num_classes.csv`, `./data/4_outliers_imp.csv`, `./data/4_outliers.csv`.
- `./script/datamicroarray.Rmd`: analyze different microarray datasets
- `./script/extract_music_features.py`: extract features from music clips and generate `./data/music.csv`
- `./script/music.Rmd`: analyze the music dataset 


