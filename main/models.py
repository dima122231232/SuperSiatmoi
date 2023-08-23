from django.db import models

class Message(models.Model):
    username = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_my_computer = models.BooleanField(default=False)  # Добавляем поле для отметки ваших сообщений

    def __str__(self):
        return f"{self.username} - {self.date}"