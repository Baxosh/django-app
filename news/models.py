from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    author = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

class Comments(models.Model):
    author = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return str(self.comment_text)
