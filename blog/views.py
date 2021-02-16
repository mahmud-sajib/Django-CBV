from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import ArticleForm
from .models import Article

from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.

class ArticleListView(ListView):
    template_name = 'article-list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'article-detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
    template_name = 'article-create.html'
    form_class = ArticleForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    template_name = 'article-create.html'
    form_class = ArticleForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'article-delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse("article-list")
    
