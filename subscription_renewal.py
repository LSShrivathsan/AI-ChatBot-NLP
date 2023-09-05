import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

import datetime
import re
from appnm.models import SubscriptionTypes

def execute(phone_number, duration):
    try:
        customer_subscription = SubscriptionTypes.objects.get(phone_number=phone_number)
    except SubscriptionTypes.DoesNotExist:
        return "Sorry, we couldn't find a subscription associated with that phone number. Please make sure you provided the correct number."
    
    expiry_date = customer_subscription.expiry_date
    current_date = datetime.datetime.now().date()
    


    if expiry_date is None or expiry_date.date() <= current_date:
        customer_subscription.expiry_date = current_date + datetime.timedelta(days=duration)
        if duration ==30:
            x="Basic Plan"
        elif duration==60:
            x="Premium Plan"
        customer_subscription.subscription_description=x
        customer_subscription.save()
        return f"payment link:...\nYour plan has been successfully renewed for {duration} days."

    return "Your plan is already active and does not require renewal at the moment."

def extract_phone_number(input_string):
    """
    Extracts the phone number from the user's input using regular expressions.
    Returns None if no phone number is found.
    """
    pattern = r'\d{9,}'
    matches = re.findall(pattern, input_string)
    if matches:
        return matches[0]
    else:
        return None
    
def extract_duration(input_string):
    """
    Extracts the duration from the user's input using regular expressions.
    Returns None if no duration is found.
    """
    pattern = r'\d+'
    matches = re.findall(pattern, input_string)
    if matches:
        return int(matches[0])
    else:
        return None

def process_conversation():
    print("Hello! I'd be happy to assist you with renewing your prepaid plan.")

    phone_number = None
    duration = None

    while not phone_number:
        input_string = input("Great! To get it validated, could you please consider sharing your phone number?")
        phone_number = extract_phone_number(input_string)

    while not duration:
        input_string = input("How long would you like to renew your plan for? (Enter the number of days)")
        duration = extract_duration(input_string)

    if duration == 30:
        x = "Basic Plan"
    elif duration == 60:
        x = "Premium Plan"

    print(f"Perfect! Let me do the necessary for the {x} for a {duration}-day renewal. Please bear with me for a moment.")
    result = execute(phone_number, duration)
    print(result)
    print("You're welcome! If you have any more questions or need further assistance, feel free to ask. Have a great day ahead!")
process_conversation()
