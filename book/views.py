from django.shortcuts import render
from  .import models
from .import forms
from django.views.generic import DetailView

# Create your views here.
class DetailBookView(DetailView):
     model=models.Book
     template_name='detail.html'
     pk_url_kwarg='id'

     def post(self, request, *args, **kwargs):
          comment_form = forms.CommentForm(self.request.POST)
          book = self.get_object()
          if comment_form.is_valid():
               new_comment=comment_form.save(commit=False)
               new_comment.book = book
               new_comment.save()
          return self.get(request, *args, **kwargs)

     def get_context_data(self,**kwargs):
          context = super().get_context_data(**kwargs)
          book = self.object
          comments = book.comments.all()

          comment_form=forms.CommentForm()
          context['comments']=comments
          context['comment_form']=comment_form
          return context