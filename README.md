# Assessment of Projection Pursuit Index for Classifying High Dimension Low Sample Size Data in R

This is the repository for the paper "Assessment of projection pursuit index for classifying high dimension low sample size data in R" by Zhaoxing Wu and Chunming Zhang.

- `./data` contains all data used in the paper. 
- `./output` contains all plots used in the paper. 
- `./script` includes all the code.
  - `./script/fun.R`: useful functions, including `S()`, `plot_test_train()`, `acc()`, `cross_validation()`. Section 2 of the paper also explains these functions in details.

## Keywords

Large p Small n; Linear Discriminant Analysis; Penalized Discriminant Analysis; Supervised Classification; SVM

<img src="https://github.com/zwu363/projection-pursuit-index/blob/main/output/code_pp.jpeg" width="350" />
    
## Citation

```
@article{wu_zhang_2023,
    author = {Zhaoxing Wu and Chunming Zhang},
    title = {Assessment of Projection Pursuit Index for Classifying High Dimension Low Sample Size Data in R},
    journal = {Journal of Data Science},
    volume = {21},
    number = {2},
    year = {2023},
    pages = {310--332},
    doi = {10.6339/23-JDS1096},
    issn = {1680-743X},
    publisher = {School of Statistics, Renmin University of China}
}
```

## To reproduce the experiments in the paper

- Simulation study (section 3: simulation evaluation): Run `./script/simulated_example.Rmd` to simulate datasets under 4 different conditions, including `./data/1_perc_imp_var.csv`, `./data/2_ratio_dim_obs.csv`, `./data/3_num_classes.csv`, `./data/4_outliers_imp.csv`, `./data/4_outliers.csv`. Code plotting the above datasets is also contained in `./script/simulated_example_plot.Rmd`
  
<p float="left">
  <img src="https://github.com/zwu363/projection-pursuit-index/blob/main/output/1_perc_imp_var.png" width="250" />
  <img src="https://github.com/zwu363/projection-pursuit-index/blob/main/output/2_ratio_dim_obs.png" width="250" />
  <img src="https://github.com/zwu363/projection-pursuit-index/blob/main/output/4_outliers.png" width="250" />
  <img src="https://github.com/zwu363/projection-pursuit-index/blob/main/output/3_num_classes_acc.png" width="250" />
  <img src="https://github.com/zwu363/projection-pursuit-index/blob/main/output/3_num_classes_mae.png" width="250" />
  <img src="https://github.com/zwu363/projection-pursuit-index/blob/main/output/3_num_classes_mse.png" width="250" />
</p>

- Microarray data analysis (section 4.1: microarray data): Run `./script/datamicroarray.Rmd` to analyze different microarray datasets. Please note that different microarray datasets are analyzed in this paper and all contained in the R package `datamicroarray`, so one need to manually change the code to use different datasets to reproduce the results (instructions can be found in the comments of the code).
- 
<img src="https://github.com/zwu363/projection-pursuit-index/blob/main/output/micro.jpeg" width="550" />

- Music data analysis (section 4.2: music data): Run `./script/extract_music_features.py` to extract features from music clips and generate `./data/music.csv`. The music clips can be found in `./data/processed_music/*`. Run `./script/music.Rmd` to analyze the music dataset.

<p float="left">
  <img src="https://github.com/zwu363/projection-pursuit-index/blob/main/output/music_artist.png" width="350" />
  <img src="https://github.com/zwu363/projection-pursuit-index/blob/main/output/music_genre.png" width="350" />
</p>

- Non-Gaussian distributed data analysis (section 5: discussion and conclusion): Run the last chunck of code in `./script/simulated_example.Rmd`. The mean values of different model performance are printed to the screen.

## Examples

The following code loads leukemia dataset and splits it into training and test sets.

```{r}
library(classPP)
source("fun.R")
library(cancerclass)
data("GOLUB1") #leukemia data
df = as.data.frame(t(scale(GOLUB1@assayData[["exprs"]])))
cls = GOLUB1@phenoData@data[["class"]] 
ALL = GOLUB1@phenoData@data[["type"]] 
class = c()
for (i in 1:length(cls))
    class = c(class, trimws(paste(cls[i], ALL[i])))
n = nrow(df)

ind = sample(1:n, n/4, replace=FALSE)
test = df[ind,]
train = df[-ind,]
cls_test = class[ind]
cls_train = class[-ind]
```

Project leukemia data into 2 dimensions using the PDA index and plot the projected training and test sets for comparison.

```{r}
PP.opt = PP.optimize.anneal("PDA", 2, train, cls_train, lambda = 0.6)
proj.data.test = as.matrix(test)%*%PP.opt$proj.best
proj.data.train = as.matrix(train)%*%PP.opt$proj.best
plot_test_train(proj.data.test, proj.data.train, cls_test, cls_train,
               levels(as.factor(class)))
```

<img src="https://github.com/zwu363/projection-pursuit-index/blob/main/output/example.png" width="350" />

Get the accuracy score for the PDA index on the leukemia data.

```{r}
acc(PP.opt$proj.best, t(train), t(test), cls_train, cls_test)
```
Hyperparameter selection for PDA index: 

```{r}
S(as.matrix(df), class, "PDA", 2, seq(0, 0.99, 0.01))
```


<img src="https://github.com/zwu363/projection-pursuit-index/blob/main/output/code_s.png" width="350" />


