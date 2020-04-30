# Install Java, Spark, and Findspark
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q http://www-us.apache.org/dist/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz
!tar xf spark-2.4.5-bin-hadoop2.7.tgz
!pip install -q findspark

# Set Environment Variables
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-2.4.5-bin-hadoop2.7"

# Start a SparkSession
import findspark
findspark.init()
import pyspark

# Download Postgres Driver to allow Spark to interact with Postgres
!wget https://jdbc.postgresql.org/download/postgresql-42.2.9.jar

# Start Spark session and add driver to Spark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("DF_ETL_to_RDS").config("spark.driver.extraClassPath","/content/postgresql-42.2.9.jar").getOrCreate()
# Normally we use the following line of code to kickoff SparkSession
spark = SparkSession.builder.appName("DataFrameFunctions").getOrCreate()
#--------------------------------------------------------------------------

# SAMPLE CODE FOR DANIEL's ETL - READ In Raw CSV webscrapped files From S3 Server
# Read in USA.com scrapped csv files from S3 Bucket databootcamp-csvfiles
from pyspark import SparkFiles
url = “https://databootcamp-csvfiles.s3.amazonaws.com/median_income_2000.csv”

spark.sparkContext.addFile(url)
median_income_df = spark.read.csv(SparkFiles.get("median_income_2000.csv"), sep=",", header=True, inferSchema=True)

# Show DataFrame
median_income_df.show()
# Repeat above process for each of the files and create 2 dfs "economic"
# and "demongraphics"

# --------------------------------------------------------------------
#LOAD 2 DATAFRAMES INTO AWS RDS SERVER for Alena's ML to access
# After all data is cleaned Daniel creates 2 DFs and loads them into the RDS Server. 
# Code to load 2 DF into AWS Server Tables is shown below

mode = "append"
jdbc_url="jdbc:postgresql://datagen.cuwjyqdbqund.us-east-1.rds.amazonaws.com:5432/postgres"
config = {"user":"postgres",
          "password": "accessdb1",
          "driver":"org.postgresql.Driver"}

# Write 2 DataFrames to active_user tables in RDS
economics.write.jdbc(url=jdbc_url, table='active_user', mode=mode, properties=config)
demographics.write.jdbc(url=jdbc_url, table='active_user', mode=mode, properties=config)

# Perform Join in RDS DB to make a single ML table
# ?? Can this be done in PySpark or SQL? 
# Sample: Join the two DataFrames
joined_ml_input_df = economics.join(demographics_df, on"zip", how"inner")
joined_ml_input_df.show()

#--------------------------------------------------------------------
# Run STATISTICAL CODE ON JOINED DF
# Start Spark session and add driver to Spark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("BigDataHW").config("spark.driver.extraClassPath","/content/postgresql-42.2.9.jar").getOrCreate()

# Once Joined ALena pulls file from AWS RDS directly into ML 
# Import functions
from pyspark.sql.functions import avg
reviews_us_clean_Grocery_df.select(avg("star_rating")).show()
# reviews_us_clean_Grocery_df.describe("star_rating")


#-------------------------------------------------------------------------------
# ALENA THEN READS STRUCTURED DATA FROM AWS RDS INTO HER DATAFRAME FOR INPUT TO ML 
# CODE NEEDED ??

