from django.shortcuts import render
from django.views.generic import  View
from django.contrib.auth.mixins import  LoginRequiredMixin
from marketing.models import  Setting
from whatsapp import  WhatsApp , Message
from django.http import HttpResponse

class MarketingSender(LoginRequiredMixin, View):

    def send_message(self,*args, **kwargs):
        whatsapp = WhatsApp(phone_number_id="01776618909")
        print(whatsapp)

        phone_number = '01776618909'  # Replace with the actual phone number
        message_text = 'Hello, this is a test message'
        media_url = 'https://example.com/image.jpg'  # Replace with the actual media URL
        message = Message(phone_number, message_text, media_url)
        message.send(whatsapp)
        status = message.get_status(whatsapp)
        if status == 'seen':
            print("Message has been seen")
        else:
            print("Message has not been seen")

        return HttpResponse("Message sent successfully")













class MarketingSetting(LoginRequiredMixin , View):
    def get(self , request):
        settings = Setting.objects.get_or_create(id=1)

        return render(self , 'give_tamplate' , {'settings':settings})

    def post(self , request , *args , **kwargs):
        setting = Setting.objects.get(id=1)
        pass