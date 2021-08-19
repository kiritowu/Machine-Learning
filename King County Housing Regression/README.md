# King County Housing Regression
### Buy Low Sell High

Author : Wong Zhao Wu, Bryan

## Modelling Objective
Perform EDA and Modelling to find the optimal solution in estimating the housing prices by minimizing Root Mean Squared Error as the primary metrics.

## Keywords
- Supervised Learning
- Regression
- Feature Engineering
- Hierarchical Clustering
- Gradient Boosted Trees

## Credits
- King Country Housing Dataset: [https://geodacenter.github.io/data-and-lab//KingCounty-HouseSales2015/](https://geodacenter.github.io/data-and-lab//KingCounty-HouseSales2015/)

## Personal Learning Reflection

Through the seattle housing price prediction problem, I've learned more of **Geo-location Feature Engineering** without leaking the actual housing prices as well as grasp a better understanding of the **Bias-Variance trade-off** through countless iterations of redefining the params grid, hyperparameter tuning, model evaluation and again! Initially due to the poor design of parameter searching grid, which results in the resulting model being more overfitted than the default parameter, despite the drop in test error. By doing more research and read-up on the Gradient Boosting, I've identified several key hyperparameters that can improve the performance without increasing the variance as much. I've also decided to make use of **AWS Sagemaker** to host and run the entire experiment to speed up the experimenting iteration for this project.

Written By : Wong Zhao Wu

Last Modified : 25 May 2021

![seattle.jpg](https://images.unsplash.com/photo-1502175353174-a7a70e73b362?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=970&q=80)

Image retrieved from [Unsplash](https://unsplash.com/photos/skUTVJi8-jc).
