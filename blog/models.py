from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog_previews/', verbose_name='Превью', blank=True, null=True,
                                help_text='Загрузите фото')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(verbose_name='Опубликовано', default=False)
    views = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0,
                                        help_text='Укажите количество просмотров')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['title']
