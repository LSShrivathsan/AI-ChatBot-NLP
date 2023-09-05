from django.db import models
from appnm.models import SubscriptionTypes
from datetime import datetime
import psycopg2

# Create a connection to the PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    database="psq",
    user="postgres",
    password="Open@123"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Create and save the instances of SubscriptionTypes
subscription1 = SubscriptionTypes(
    subscription_code='1',
    subscription_description='Basic Plan',
    subscription_web_description='basic plan',
    subscription_mobile_description='basic plan',
    subscription_image='image1.jpg',
    subscription_is_default=True,
    subscription_is_demo=False,
    created_by_user_id=1,
    created_from_ip='127.0.0.1',
    updated_by_user_id=1,
    phone_number=1234567890,
    expiry_date=datetime(2023, 12, 31)  # Set the expiry date
)
subscription1.save()

subscription2 = SubscriptionTypes(
    subscription_code='2',
    subscription_description='Basic plan',
    subscription_web_description='basic plan',
    subscription_mobile_description='basic plan',
    subscription_image='image2.jpg',
    subscription_is_default=False,
    subscription_is_demo=True,
    created_by_user_id=2,
    created_from_ip='127.0.0.1',
    updated_by_user_id=2,
    phone_number=1234567891,
    expiry_date=datetime(2023, 11, 30)  # Set the expiry date
)
subscription2.save()

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

