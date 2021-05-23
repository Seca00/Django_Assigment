# Django_Assigment

This is an assignment No 1 from Evreka Back-End Developer Evaluation Questions
I created a simple web project with 2 models, and used default SQLite database

NavigationRecord          Vehicle
id PK                     id PK
vehicle FK                plate CharField
datetime DateTimeField
latitude FloatField
longitude FloatField

And returned records from last 48 hours. Didn't see a requirement for creating a view for the table since Django ORM handles it pretty well with "Foreign Key".
The query is: 'SELECT * FROM NavigationRecord WHERE datetime >= 2_days_ago'
Since we are using date as a parameter I included NR.datetime as a index (you can see the comments in the models).
Ideas for further improvements:
- Make the datetime order desc and index. And with DB's like MongoDB and PostgreSQL, this would be enough to handle queries since I've used it for retrieving log datas from ~10m entries.
- We can delete miliseconds from the datetime parameter since it helps with the searching, but this would request a set of changes which will apply system wide:
  For Django: In your settings file set the follwing:

        DATETIME_FORMAT="%Y-%m-%d%H:%M:%S"
        L10N=False to make sore localization data doesn't take precedent when it comes to dates format.
        USE_TZ=False

- Another way we can create a new column for a view with only the date and make it index.

- I don't think there is a need for any tools. But to be sure we can always use some load balancer tool for balancing the network traffic and to handle the requests 
so that we can manage the congestions in the system.
