Machine Learning Overview 

Due to the complexity and multilayer nature of the topic we've selected, and not having complete data available, we had to create our dataset from scratch, hand picking only the features we were going to ultimately use in the mahcine learning model. 
The dicision was based on societal and economic research conducted by other organizations.
Hence, the feature selection part was done during the data collection. The downside is, we now have to manually create the outcome column based on existing data. This will require some time, as the plan is to find the already gentrified zipcodes, look at their metrics and come up with a formula/threshold for the rest of the dataset. 

As for the feature engineering, I am still debating between 2 algorithms, which are either Random Forest or Gradient Boost. 
I have applied both of them on a very small test dataset, and the results were 100% on each metric, which at that point only meant complete overfitting (I would love to assume I somehow created the most perfect model, but that just wasn't it). 

Why I am debating between two:
Random Forests require little parameter tuning, robust to noise (which I hope we've aleviated), they're interpretable and great for classification problems. However, using larger random forest require more memory and slows down the process, they do not predict beyond the range of the response values in the training data, and they can be very prone to overfitting. 

Gradient Boost is less interpretable, but shows great perfomance, suitable for almost any ML problem, and I just personally like this algorithm. Cons: it requires parameter tuning and prone to overfitting. 

Both of the algorithms don't require feature scaling.
And at the moment we do not have any categorcial data, thus won't need to encode any variables. 

So now, as soon we have the outcome column done, I am going to test both of the models and choose the best performance. 
