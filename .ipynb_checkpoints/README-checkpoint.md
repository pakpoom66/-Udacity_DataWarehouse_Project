# Project: Data Warehouse

Hi again, My name is **Phakphoom Claiboon**. Currently, I am in the Data Engineering Nanodegree of Udacity, and this is my Data Warehouse Project of this course.
If you have any comments, please feedback to me.

Thanks.

## Introduction
A music streaming startup, **Sparkify**, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description
In this project, you'll apply what you've learned on data warehouses and AWS to build an ETL pipeline for a database hosted on Redshift. To complete the project, you will need to load data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.


## Summary of the Project
The project need to read many json data and ETL them to build DWH data modeling
- Create Amazon Redshift and IAM ROLE
- Design the Data Model
- Create tables for the Data Model
- Load json data to Staging Tables
- ETL/Insert Data from Staging Tables to Data Models

## Schema for Song Play Analysis
Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

![Sparkify_DW_Design](images/Sparkify_DW_Design.drawio.png)

### Fact Table
1. **songplays** - records in log data associated with song plays i.e. records with page `NextSong`
    - songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables
2. **users** - users in the app
    - user_id, first_name, last_name, gender, level
3. **songs** - songs in music database
    - song_id, title, artist_id, year, duration
4. **artists** - artists in music database
    - artist_id, name, location, latitude, longitude
5. **time** - timestamps of records in **songplays** broken down into specific units
    - start_time, hour, day, week, month, year, weekday

## How to run the Python Scripts

1. Open **dwh.cfg**, edit the `KEY` and `SECRET` values in "[AWS]" session with **AWS Access Key ID** and **AWS Secret Access Key**, respectively.
![1_dwh_cfg_prepare1](images/1_dwh_cfg_prepare1.png)


2. Open **01_Prepare_Redshift_Cluster.ipynb** and run code from step 0 to step 10. 
    Waiting to the Redshift Cluseter status is `available`
![2_check_status_cluster1](images/2_check_status_cluster1.png)


    Check the cluster endpoint, role ARN, and try connect to the cluster
![3_check_endpoint_role_connection1](images/3_check_endpoint_role_connection1.png)


3. Open **dwh.cfg**, edit the `HOST` values in "[CLUSTER]" session with **DWH_ENDPOINT** from step 9.
4. Open **dwh.cfg**, edit the `ARN` values in "[IAM_ROLE]" session with **DWH_ROLE_ARN** from step 9.
![4_check_endpoint_role_1](images/4_check_endpoint_role_1.png)


5. Run script **create_tables.py** for create/reset the sparkifydwh database

    ``` bash
    python create_tables.py
    ```


6. Run script **etl.py** or **etl.ipynb** for start the ETL process to each tables in the sparkifydwh database

    ``` bash
    python etl.py
    ```


7. Run **02_Dashboard_for_analytic_queries.ipynb** to run/check a dashboard for analytic queries on sparkifydwh database.

8. After your test to finish, open **01_Prepare_Redshift_Cluster.ipynb** and run code step 11. 

## Reference

I have been searching for some ideas or other help to find solutions in my code that are shown as below:

1. Idea for Data Quality Checks and Dashboard for analytic queries... [Udacity: Question About Project Rubric and the "Suggestions to Make Your Projects Stand Out!" Section.](https://knowledge.udacity.com/questions/167872)
2. Idea and Sample for Load Song data and Log data ... 
    - [Udacity: dataset](https://knowledge.udacity.com/questions/672637)
    - [Udacity: Not able to read multiple JSON file from song_data (s3) in AirFlow Pipeline project](https://knowledge.udacity.com/questions/51254)
    - [Udacity: Why do we need to set a json path for log data but not song data?](https://knowledge.udacity.com/questions/144884)
3. Idea and Sample for Convert/Trsnsform timestamp data ... 
    - [AWS: Date parts for date or timestamp functions](https://docs.aws.amazon.com/redshift/latest/dg/r_Dateparts_for_datetime_functions.html)
    - [Postgresql: 9.9. Date/Time Functions and Operators](https://www.postgresql.org/docs/10/functions-datetime.html#FUNCTIONS-DATETIME-TABLE)
    - [GET MILLISECONDS FROM TIMESTAMP IN POSTGRESQL](https://www.datasciencemadesimple.com/get-milliseconds-from-timestamp-in-postgresql/)
    - [Postgresql: 9.8. Data Type Formatting Functions](https://www.postgresql.org/docs/10/functions-formatting.html)
    - [Stackoverflow: Convert date from long time postgres](https://stackoverflow.com/questions/7872720/convert-date-from-long-time-postgres)
4. Idea and Sample for How to connect Amazon Redshift to python ... [Stackoverflow: How to connect Amazon Redshift to python](https://stackoverflow.com/questions/45212281/how-to-connect-amazon-redshift-to-python/45213674)
5. Idea and Sample for use Matplotlib Pie Charts ... 
    - [w3schools: Matplotlib Pie Charts](https://www.w3schools.com/python/matplotlib_pie_charts.asp)
    - [Stackoverflow: Matplotlib: Plot the result of an SQL query](https://stackoverflow.com/questions/30979962/matplotlib-plot-the-result-of-an-sql-query)