# projection-pursuit-index

This is the repository for the paper "Assessment of projection pursuit index for classifying high dimension low sample size data in R" by Zhaoxing Wu and Chunming Zhang.

All data used in the paper is contained in the folder `./data`. Plots used in the paper is contained in the folder `./output`. `./script` includes all the code.

- `./script/fun.R`: useful functions used by the following scripts. Include S(), plot_test_train(), acc(), cross_validation().
- `./script/simulated_example.Rmd`: simulate datasets under 4 different conditions, including `./data/1_perc_imp_var.csv`, `./data/2_ratio_dim_obs.csv`, `./data/3_num_classes.csv`, `./data/4_outliers_imp.csv`, `./data/4_outliers.csv`.
- `./script/datamicroarray.Rmd`: analyze different microarray datasets
- `./script/extract_music_features.py`: extract features from music clips and generate `./data/music.csv`
- `./script/music.Rmd`: analyze the music dataset 

## Examples
The following code loads leukemia dataset and splits it into training and test sets.
```{r}
library(classPP)
source("fun.R")
library(cancerclass)
data("GOLUB1") #leukemia data
df = as.data.frame(t(scale(GOLUB1@assayData[["exprs"]]))) #scale????
cls = GOLUB1@phenoData@data[["class"]] #ALL, AML
ALL = GOLUB1@phenoData@data[["type"]] #ALL_Tcell, ALL_Bcell
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
Get the accuracy score for the PDA index on the leukemia data.
```{r}
acc(PP.opt$proj.best, t(train), t(test), cls_train, cls_test)
```
Hyperparameter selection for PDA index: 
```{r}
S(as.matrix(df), class, "PDA", 2, seq(0, 0.99, 0.01))
```


