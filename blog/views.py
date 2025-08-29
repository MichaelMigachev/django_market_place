from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


class PostListView(ListView):
    model = Post
    # template_name = 'blog/post_list.html'  # Создать этот шаблон
    context_object_name = 'posts'


    def get_queryset(self):
        # Фильтруем только опубликованные записи
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):
    model = Post
    # template_name = 'blog/post_detail.html'  # Создайте этот шаблон
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Увеличиваем счетчик просмотров
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'preview', 'published']  #  нужные поля

    def get_success_url(self):
        # После успешного создания перенаправляем на детальное представление записи
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  # можно использовать тот же шаблон, что и для создания
    fields = ['title', 'content', 'preview', 'published']
    success_url = reverse_lazy('blog:post_list')

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})



class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # шаблон для подтверждения удаления
    success_url = reverse_lazy('blog:post_list')

