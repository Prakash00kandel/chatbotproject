from django.shortcuts import render
# from django.http import HttpResponse
from .main import *
from .models import *

# Create your views here.

def index(request):
    return render(request, 'botsummit/base.html')


# def about(request):
#     return HttpResponse()
def ChatbotView(request):


    if request.method == "POST":
        print("this is post")
        get_message = request.POST.get('msg', None)

        print('get_message', get_message)

        reply_messages = chat(get_message)
        print('reply_messages', reply_messages)

        
        context = {
            'ram': 'ram',
            'get_message':get_message,
            'reply_messages':reply_messages,

        }
        return render(request, 'botsummit/base.html', context)




