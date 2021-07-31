from django.shortcuts import render
from django.http import HttpResponse
from .main import chat
from django.shortcuts import redirect
from .models import *
from .forms import UserInfoForm


# Create your views here.

def index(request):
        if request.method == 'POST':
            print('SUccess \n\n')
            details = UserInfoForm(request.POST)

            if details.is_valid():
                user_info = details.save(commit=False)

                user_info.save()
                print('SUccess \n\n')
                return redirect('botsummit:chatbot')
            else:
                return render(request, 'botsummit/getUserInfo.html', {'form': details})

        else:
            print('ELSE \n\n')
            return render(request, 'botsummit/getUserInfo.html', {'form': UserInfoForm(None)})

def form(request):

    if request.method == 'POST':
        details = UserInfoForm(request.POST)

        if details.is_valid():
            user_info = details.save(commit=False)

            user_info.save()
            print('SUccess \n\n')
            return redirect('botsummit:chatbot')
        else:
            return render(request, 'botsummit/getUserInfo.html', {'form': details})

    else:
        print('ELSE \n\n')
        return render(request, 'botsummit/getUserInfo.html', {'form': UserInfoForm(None)})

# def about(request):
#     return HttpResponse()
def ChatbotView(request):
    print(f'{request.method} \n\n')
    if request.method == "POST":
        # print("this is post")
        get_message = request.POST.get('msg')
        if get_message != None:

            print('get_message', get_message)

            reply_messages = chat(get_message)
            print('reply_messages', reply_messages)

            context = {
                'get_message': get_message,
                'reply_messages': reply_messages,

            }
            # return context
            return render(request, 'botsummit/response.html', context)
        else:
            return HttpResponse(404)
    return render(request, 'botsummit/chatbox.html')

