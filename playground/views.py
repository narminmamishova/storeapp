from django.core.mail import send_mail, mail_admins,EmailMessage, BadHeaderError
from templated_mail.mail import BaseEmailMessage
from django.shortcuts import render


def say_hello(request):
    try:
        
        # mail_admins('subject', 'message', html_message='message')
        
        
        # message = EmailMessage('subject', 'message', 'from@test.com', ['to@test.com'])
        # message.attach_file('playground/static/images/dog.jpg')
        # message.send()
        
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name':'Narmin'}
        )
        message.send(['john@test.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})