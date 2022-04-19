from django.db import models

class Articles(models.Model):
    title = models.CharField('Naming', max_length=50)
    anons = models.CharField('Intro', max_length=250)
    full_text = models.TextField('Text')
    date = models.DateTimeField('Publication date')

#для вывода из бд
    def __str__(self):
        return f'New: {self.title}'

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = "News"

