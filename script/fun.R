library(DiscriMiner) #function withinSS()
#library(devtools)
#install_github("EK-Lee/classPP")

################################################################################
## Function S: select the appropriate $\lambda$
## specifically for PDA hyperparameter tuning
#data: the original dataset for projection
#class: vector of classes of all samples
#method: LDA or PDA
#dim: the projection dimension
#hyper: the list of hyperparameters
#filename: the file name for the output plot
S = function(data, class, method, dim, hyper){
  S = c()
  for (i in hyper){ #iterate through each hyperparameter
    PP.opt = PP.optimize.anneal(method,dim,data,class,lambda = i)
    #calculate the within-class sum of squares
    W = withinSS(data%*%PP.opt[["proj.best"]], class)
    S = c(S, sum(diag(W))/dim/nrow(data))
  }
  
  #output plot
  smoothingSpline = smooth.spline(hyper, S, spar=0.8)
  plot(hyper, S)
  lines(smoothingSpline, col = "red")
  abline(h=1, col="blue")
}


################################################################################
## plot train and test datasets on the same graph
#proj.data.test: test dataset after projection
#proj.data.train: train dataset after projection
#cls_test: vector of classes of test dataset
#cls_train: vector of classes of train dataset
#cls_tot: vector of distinct classes in the entire dataset
plot_test_train = function(proj.data.test, proj.data.train, cls_test, cls_train,
                           cls_tot){
  lim = c(min(min(proj.data.test), min(proj.data.train)), 
          max(max(proj.data.test), max(proj.data.train)))
  
  plot(x=NA, y=NA, xlim = lim, ylim= lim, xlab="", ylab="", main="", axes=FALSE,
       frame.plot=TRUE)
  for (i in 1:length(cls_tot)){
    #plot projected test data
    points(proj.data.test[,1][cls_test == cls_tot[i]], 
           proj.data.test[,2][cls_test == cls_tot[i]], 
           pch = i, col = "darkgrey")
  }
  #plot projected train data
  text(proj.data.train[,1], proj.data.train[,2], as.numeric(factor(cls_train)), 
       cex=1)
}



################################################################################
## Accuracy score in PDA
#a: the optimal projection (PP.opt$proj.best)
#train: traversed train dataset
#test: traversed test dataset
#cls_test: vector of classes of test dataset
#cls_train: vector of classes of train dataset
acc = function(a, train, test, cls_train, cls_test){
  #get the average of classes in the training dataset
  cls_mean = data.frame(rep(NA, nrow(train)))
  for (i in unique(cls_train))
    cls_mean = cbind(cls_mean, rowMeans(train[, cls_train==i]))
  cls_mean = cls_mean[,-1] #remove the first column of NA
  
  rst = c() #storing predicted class of each test data point
  for (i in 1:ncol(test)){ #iterate through each test data point
    temp=c() #storing the distance of one data point to each class
    for (j in 1:ncol(cls_mean)){ #iterate through each class
      x = 0 #storing the distance of one data point to one class
      for (k in 1:ncol(a)) #iterate through the projected dimension
        x=x+(a[,k]%*%(test[,i]-cls_mean[,j]))^2
      temp=c(temp, x)
    }
    rst = c(rst, unique(cls_train)[which.min(temp)])
  }
  return (sum(rst==cls_test)/length(cls_test))
}

################################################################################
## MSE and MAE in PDA
#a: the optimal projection (PP.opt$proj.best)
#train: traversed train dataset
#test: traversed test dataset
#cls_test: vector of classes of test dataset
#cls_train: vector of classes of train dataset
#return a vector of two values: the first value is MSE, the second is MAE
metrics = function(a, train, test, cls_train, cls_test){
  #get the average of classes in the training dataset
  cls_mean = data.frame(rep(NA, nrow(train)))
  for (i in unique(cls_train))
    cls_mean = cbind(cls_mean, rowMeans(train[, cls_train==i]))
  cls_mean = cls_mean[,-1] #remove the first column of NA
  
  rst = c() #storing predicted class of each test data point
  for (i in 1:ncol(test)){ #iterate through each test data point
    temp=c() #storing the distance of one data point to each class
    for (j in 1:ncol(cls_mean)){ #iterate through each class
      x = 0 #storing the distance of one data point to one class
      for (k in 1:ncol(a)) #iterate through the projected dimension
        x=x+(a[,k]%*%(test[,i]-cls_mean[,j]))^2
      temp=c(temp, x)
    }
    rst = c(rst, unique(cls_train)[which.min(temp)])
  }
  return (c(mean((rst - cls_test)^2), mean(abs(rst - cls_test))))
}


################################################################################
##Cross validation for hyperparameter tuning in PDA
#df: the dataset
#class: vector of classes of all samples
#k: number of folds
#hyperparameter: the list of hyperparameters for tuning
#filename: the file name for storing the output plot
cross_validation = function(df, class, k, hyperparameter, filename){
  ret = c()
  #progress bar setup
  pb <- txtProgressBar(min = 0, max = k, style = 3, width = 50, char = "=") 
  
  ##shuffle dataset
  ind = sample(1:nrow(df))
  df = df[ind, ]
  class = class[ind]
  ##split into k-folds
  temp = seq(1, nrow(df), by = nrow(df)/k) #the first element of the new fold
  for (j in 1:length(hyperparameter)){
    acc = c()
    for (i in 1:k){
      if (i==10)
        ind = seq(floor(temp[k]), nrow(df))
      else
        ind = seq(floor(temp[i]), floor(temp[i+1])-1)
      train = df[-ind, ]
      test = df[ind, ]
      cls_train = class[-ind]
      cls_test = class[ind]
      PP.opt = PP.optimize.anneal("PDA",2,train,cls_train,
                                  lambda = hyperparameter[j])
      proj.data.test = as.matrix(test)%*%PP.opt$proj.best
      proj.data.train = as.matrix(train)%*%PP.opt$proj.best
      acc = c(acc, misclass(PP.opt$proj.best, t(train), t(test), cls_train, 
                            cls_test))
      setTxtProgressBar(pb, i)
    }
    
    writeLines(paste("\nHyperparameter: ", hyperparameter[j], 
                     ", accuracy mean: ", mean(acc), 
                     ", accuracy sd: ", sd(acc)))
    ret = c(ret, mean(acc))
  }
  
  close(pb)
  
  png(filename, width=4, height=4, units="in", res=300)
  #smoothingSpline = smooth.spline(hyperparameter, ret, spar=0.8)
  plot(hyperparameter, ret, xlab = TeX(r'($\lambda$)'), 
       ylab = "Accuracy Score")
  #lines(smoothingSpline, col = "red")
  dev.off()
}





