# Project_M20

## Week 3 Project Deliverables

Deliverable #1 - PROJECT PRESENTATION can be found in Google Slides at 
https://docs.google.com/presentation/d/1LRGL9fkDld9kNaR7kHqptzNkjxrQsmkt7Id-hZfG8Ac/edit?usp=sharing

Deliverable #2 - GITHUB - this GitHub Repository 

Deliverable #3 - Machine Learning Model - code found in file new_dataset_test.lpynb in Master Branch plus description added below under ML Overview week 2 deliverables. 

Deliverable #4 - Database: 
Database presentation can be found in Google Slides at
https://docs.google.com/presentation/d/1IF_iHJMSYnA6jvOHU9LZdg2cg2WcogY5j00ZlOhlpWU/edit?usp=sharing

* Fake Data Python Code found under  Fake_Data Folder in Master Branch
* Real Data Python Code found under ETL Folder in Master Branch 
* Database ERD and SQL Code found under ETL Folder in Master Branch

Deliverable #5 - Gentrification Dashboard - Google Slide https://docs.google.com/presentation/d/1gG6KDQ8mBVEYPGtawjPi9MpZdGQSC38lWJVrBN4hK-w/edit?usp=sharing


## Week 2 Project Deliverables
Note - This week we lost 1 team member Sierra Harris who has applied to drop the course and enroll in next semester. We now have 3 members Daniel, Alena, and Thomas 

Deliverable #1 - PROJECT PRESENTATION can be found in Google Slides at 
https://docs.google.com/presentation/d/1LRGL9fkDld9kNaR7kHqptzNkjxrQsmkt7Id-hZfG8Ac/edit?usp=sharing

Deliverable #2 - GITHUB - this GitHub Repository 

Deliverable #3 - Machine Learning Model - code found in file new_dataset_test.lpynb in Master Branch plus description added below under ML Overview week 2 deliverables. 

Deliverable #4 - Database: 
* Fake Data Python Code found under  Fake_Data Folder in Master Branch
* Real Data Python Code found under ETL Folder in Master Branch 
* Database ERD and SQL Code found under ETL Folder in Master Branch
* Description added to this file below under Database Week 2 Deliverables below

Deliverable #5 - Gentrification Dashboard - Google Slide https://docs.google.com/presentation/d/1gG6KDQ8mBVEYPGtawjPi9MpZdGQSC38lWJVrBN4hK-w/edit?usp=sharing

## Machine Learning Overview Week 2 Deliverable

Due to the complexity and multilayer nature of the topic we've selected, and not having complete data available, we had to create our dataset from scratch, hand picking only the features we were going to ultimately use in the mahcine learning model. The decision was based on societal and economic research conducted by other organizations. Hence, the feature selection part was done during the data collection. The downside is, we now have to manually create the outcome column based on existing data. This will require some time, as the plan is to find the already gentrified zipcodes, look at their metrics and come up with a formula/threshold for the rest of the dataset. And for the time being I created a mock outcome, just to see if it works.

As for the feature engineering, I am still debating between 2 algorithms, which are either Random Forest or Gradient Boost. Why I am debating between two: Random Forests require little parameter tuning, robust to noise (which I hope we've aleviated), they're interpretable and great for classification problems. However, using larger random forest require more memory and slows down the process, they do not predict beyond the range of the response values in the training data, and they can be very prone to overfitting.

Gradient Boost is less interpretable, but shows great perfomance, suitable for almost any ML problem, and I just personally like this algorithm. Cons: it requires parameter tuning and prone to overfitting.

Both of the algorithms don't require feature scaling. And at the moment we do not have any categorcial data, thus won't need to encode any variables.

UPD: I did a test run on the new dataset, Random Forest showed 100% on every metric, which is most likely the indicator of overfitting. Gradient Boost showed the same 'success'. Like I said before, they can be very prone to overfitting, and that is what I think happening here. That's why I did a test using Logistic Regression. The results are more modest, however, with the higher bias, the variance is lower in this case, which is a more preferable outcome.

Conclusion: The dataset needs more work done. For the ML model I might shift to simpler, much more interpretable algorithms, that are robust to overfit.


## Database Week 2 Deliverables

* Database ERD included in ETL folder in Master Branch
* Database SQL code included in ETL folder in Master Branch
* PostgresSQL database setup with a picture of tables setup in Database
* Two Tables Variables_1 and Variables_2 hold all X- Feature data and are joined to create final DF read into Machine Learning Model. 
* SQLAlchemy connection string

Next steps week 3  - Three more columns are being added to the dataframe as part of week 3 work to make the model even more robust. This will add Percent_Change_House_Value to ML Model. TO further enhance our application, AWS Cloud Server is being setup so we can have access to data connection anytime via internet rather than tied to a local machine. Again, this will be handled as an enhancement in week 3. 

## Project Process Overview
The Class instructors divided the class into 3 4-person teams with each team defining their own project within the Rubric provided. The project will run over 4 weeks with defined deliverables due at the end of each week on Sunday. The Rubric can be found in the Master Branch of the Repository. 

## Phase 1 - Project Definition
During the first week, the team will meet during normal class hours on Monday and Wednesday and hold any additional Zoom meetings as determined by the team. The objectives during this first week are to:
1) Get acquainted with team members
2) Choose a project and determine roles
3) Do due diligence on various aspects of the project such as source of data, technology stack, how work will be assigned and tracked. 

## Project Kickoff Meeting
Team-Blue held their first meeting on Monday at 3 pm over zoom to kick off the project and get acquainted. We did a round robin answering such questions as:

* Why did you take this course and what were your objectives
* How are you doing in the course? Challenges, unit tests
* Work experience
* Project experience
* Any particular domain (subject matter) expertise, hobbies, professional
* Any initial thoughts on project ideas and role you want to play
* Best time for you to work on project
* Best time for team meetings
* Can we contact you during the day via text, cell

During the meeting we brainstormed some initial ideas and committed to each come up with 3-4 project ideas and describe them in written form using the template provided in the Rubric as follows:

* Selected topic
* Reason why we selected the topic
* Description of our source data
* Questions we hoped to answer from the data through prediction or classification via ML. 

With 12 ideas total, we then came back on Weds 4/8 and did a multi-vote. Each member was given 3 votes to vote on their favorite topic. We then tallied the votes and came up with the First, Second, Third Choice. The top topic was:  

* Gentrification - Predicting neighborhood candidates for gentrification glusters. 

The second and third choice will be backup topics if we run into insolveable problems on topic 1. 

Sierra then volunteered and setup our SLACK Channel for Team BLue and this repository. Daniel has subsequently located a quick reference guide for SLACK in a team setting. We are all reading up on it to learn SLACK Workflow for projects. 

## Week 1 Deliverables
Content Team members have drafted their project, including the following:

Selected topic - Gentrification. We have selected our toppic as below: 
It's a growing concern among numerous neighborhoods in different cities, and a hot topic for developers looking to invest money. With this research we are hoping to find out the combination of factors in different areas that already have been gentrified to determine potential future candidates that 'have it all', using supervised machine learning classification algorithm. And, possibly define the 'opportunity zones' through clutering algorithms. (Opportunity zones being the investment in local buisnesses for a certain timeframe, in order to recive tax breaks) 

Data Sources: Los Angeles GeoHub, PortlandMaps Open Data, data.world. Data source links are located in Branch-Alena. Daniel and Thomas are doing preliminary analysis on the datasources. 

Git Hub -  
* Master Branch - this repository. 
* ✓ Includes a README.md - this README. 

✓ Description of the communication protocols:
* We have setup a Team-Blue Slack channel for communication. 
* We also hold Adhoc Zoom Meetings with the whole team twice a week to check progress and next steps. These are in addition to the regular Monday-Wednesday 7-9 pm working meetings setup by the instructor. 
* All progress is recorded in this README file. 

* Individual Branches 
* ✓ At least one branch for each team member - complete. 
* ✓ Each team member has at least four commits from the duration of the first segment - complete. 

Machine Learning Model 
* Alena has placed psuedo code in Branch - Alena for the ML definition. It looks highly likely that we will use a classification model on an imbalanced labeled dataset to train the model. Based on an analysis of the data, this appears we will used a Supervised Learning ML and our labeled dataset to predict our target = Gentrification = 1. 

In addition to psuedo ML code, we have sample data in Branch - ALena and Branch - Thomas.

Database 
* Daniel has created a provisional database (fake data) which mimics major "Features" (X variable) using multiple columns which will be present in final database. He has setup a local POSTGRES database to test and store the values. This task is complete and his code can be found in Branch - Daniel of this repository. 

* We will not connect the machine learning module to the provisional database but instead move directly to setting up a Cloud Based Database on Amazon - fully accessible by all team members. 

* The final data for training and testing our ML model will be prepared by 2 team members - Daniel and Thomas. This will then drive the final DB Schema and data will be moved into the Cloud-Based DB during week 2 of the project. 


Dashboard - To be determined in week 2 of project. Sierra is currently working on the draft storyboard and we will view that draft on Monday of Week 2.

In addition, Thomas reached out to Program Mgr Michael, Trilogy, and TA Rushi to clarify deliverables for Week 1 in area of ML and Database. Both Michael Fox and Hugo (Instructor) responded back and said a description of the ML and database would meet requirements.  

## Project Roles

**Square**: Sierra Harris

**Triangle**: Alena Kuznetsova

**Circle**: Daniel Chang

**X**: Thomas Cottrell

### Team Zoom Meetings

April 6 - 4 PM,
April 6  7-9PM,
April 8 - 3 PM,
April 8 7-9 PM,
April 10 2 PM,
April 13 3 PM,
April 13, 7 PM
April 15 2 PM,
April 15 7 PM,
April 17, 3 PM,
April 20, 7 PM,
April 22 4 PM,
April 22 7 PM,
April 24 3 PM (Sierra told us she is leaving) 
April 25 (shift in duties)
April 26 1PM (Finalize Week 2 Deliverables)


