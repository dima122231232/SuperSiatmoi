from django.shortcuts import render, redirect
from .models import Message

def index(request):
    messages = Message.objects.all().order_by('-id')  # Получить все сообщения и отсортировать их по убыванию id
    message_count = messages.count()  # Подсчет количества сообщений
    return render(request, 'main/osnova.html', {'messages': messages, 'message_count': message_count})

def save_message(request):
    if request.method == 'POST':
        username = request.POST['username']
        text = request.POST['text']
        message = Message(username=username, text=text)
        message.save()
        return redirect('/')  # Перенаправьте на главную страницу
    return render(request, 'main/osnova.html')
