# from django.core.mail import send_mail, mail_admins,EmailMessage, BadHeaderError
# from templated_mail.mail import BaseEmailMessage
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from rest_framework.views import APIView
import requests


class SayHello(APIView):
    @method_decorator(cache_page(5*60)) 
    def get(self,request):
        response = requests.get("http://httpbin.org/delay/2")
        data = response.json()
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