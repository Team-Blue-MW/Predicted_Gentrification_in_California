Machine Learning Overview 

Due to the complexity and multilayer nature of the topic we've selected, and not having complete data available, we had to create our dataset from scratch, hand picking only the features we were going to ultimately use in the mahcine learning model. 
The decision was based on societal and economic research conducted by other organizations.
Hence, the feature selection part was done during the data collection. The downside is, we now have to manually create the outcome column based on existing data. This will require some time, as the plan is to find the already gentrified zipcodes, look at their metrics and come up with a formula/threshold for the rest of the dataset. And for the time being I created a mock outcome, just to see if it works. 

As for the feature engineering, I am still debating between 2 algorithms, which are either Random Forest or Gradient Boost. 
Why I am debating between two:
Random Forests require little parameter tuning, robust to noise (which I hope we've aleviated), they're interpretable and great for classification problems. However, using larger random forest require more memory and slows down the process, they do not predict beyond the range of the response values in the training data, and they can be very prone to overfitting. 

Gradient Boost is less interpretable, but shows great perfomance, suitable for almost any ML problem, and I just personally like this algorithm. Cons: it requires parameter tuning and prone to overfitting. 

Both of the algorithms don't require feature scaling.
And at the moment we do not have any categorcial data, thus won't need to encode any variables. 

UPD: I did a test run on the new dataset, Random Forest showed 100% on every metric, which is most likely the indicator of overfitting. Gradient Boost showed the same 'success'. Like I said before, they can be very prone to overfitting, and that is what I think happening here. 
That's why I did a test using Logistic Regression. The results are more modest, however, with the higher bias, the variance is lower in this case, which is a more preferable outcome. 

Conclusion:
The dataset needs more work done. For the ML model I might shift to simpler, much more interpretable algorithms, that are robust to overfit.
