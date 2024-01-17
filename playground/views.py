# from django.core.mail import send_mail, mail_admins,EmailMessage, BadHeaderError
# from templated_mail.mail import BaseEmailMessage
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from rest_framework.views import APIView
import requests
import logging



logger = logging.getLogger(__name__)

class SayHello(APIView):
    # @method_decorator(cache_page(5*60)) 
    def get(self,request):
        try:
            logger.info("Calling HTTPbin")
            response = requests.get("http://httpbin.org/delay/2")
            logger.info("Received the Response")
            data = response.json()
        except requests.ConnectionError:
            logger.critical("HTTPbin is offline")
        return render(request, 'hello.html', {'name': "Narmin"})

    








# def say_hello(request):
#     try:
        
#         # mail_admins('subject', 'message', html_message='message')
        
        
#         # message = EmailMessage('subject', 'message', 'from@test.com', ['to@test.com'])
#         # message.attach_file('playground/static/images/dog.jpg')
#         # message.send()
        
#         message = BaseEmailMessage(
#             template_name='emails/hello.html',
#             context={'name':'Narmin'}
#         )
#         message.send(['john@test.com'])
#     except BadHeaderError:
#         pass
#     return render(request, 'hello.html', {'name': 'Mosh'})