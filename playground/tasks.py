from time import sleep
from storefront.celery import celery##it is not a good approach because this app is going to be dependent another app which is called storefront. Instead
from celery import shared_task


# @celery.task 
# def notify_customers(message):
#     print("message")
#     print("sending 100k messages")
#     sleep(10)
#     print("message were successfully sent!")

@shared_task 
def notify_customers(message):
    print(message)
    print("sending 100k messages")
    sleep(10)
    print("message were successfully sent!")