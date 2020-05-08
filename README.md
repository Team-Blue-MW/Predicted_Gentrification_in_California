Machine Learning Overview 

Due to the complexity and multilayer nature of the topic we've selected, and not having complete data available, we had to create our dataset from scratch, hand picking only the features we were going to ultimately use in the mahcine learning model. 
The decision was based on societal and economic research conducted by other organizations.
Hence, the feature selection part was done during the data collection. The downside is, we now have to manually create the outcome column based on existing data. This will require some time, as the plan is to find the already gentrified zipcodes, look at their metrics and come up with a formula/threshold for the rest of the dataset. And for the time being I created a mock outcome, just to see if it works. SMOTE after all, has been selected as the oversampling technique.

## Week 3
After having run several tests, using Logistic Regression and Random Forest, there was a realization that imbalanced datasets (our class ratio is 4:1)require a completely different evaluation and approach than balanced ones, because accuracy score is only reflecting the underlying class distribution in our case. 

Hence, precision, recall and f1 score are the metrics I will pursue. And I chose Random Forest, because it has shown good performance on imbalanced data before due to its hierarchical structure (linear regression and simpler models aren't equiped to deal with class imbalance). It generally shows a better performance over the single tree classifier, yields generalization error rate and pretty robust to noise. However, RF tends to learn from the class imbalance, focusing on the majority class prediction accuracy rather than minority. To aleviate that, I am going to test balanced random forest and weighted random forest for our model to try to boost predictive performance on minority class.

To find the best parameters, I performed a grid search over specified parameter values using scikit-sklearn implemented GridSearchCV. After that I am going to calibrate the model by adjusting the cutoff by cross-validation. If the metris are still low, I might have to penalize the algorithm, i.e. assign higher missclassification cost.

Another option is to reframe the approach to anomaly detection instead of classification, but I'd like to refrain from that if possible.
