from django.shortcuts import render, reverse
from django.views.generic import View
from django.shortcuts import redirect
from movies.models import Movie
from books.models import Book
from . import models
from . import forms

class ReviewView(View):
    form_class = forms.ReivewInput
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs['pk']
        form=self.form_class(request.POST)
        if form.is_valid():
            review=form.save()
            review.created_by=self.request.user
            
            review.movie=Movie.objects.get(pk=pk)
            review.save()
            return redirect(reverse("movies:movie",  kwargs={'pk': pk}))
                
                
                
        else:
            return redirect(reverse("movies:movie",  kwargs={'pk': pk}))
        
        
class ReviewBookView(View):
    form_class = forms.ReivewInput
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs['pk']
        form=self.form_class(request.POST)
        if form.is_valid():
            review=form.save()
            review.created_by=self.request.user
            
            review.book=Book.objects.get(pk=pk)
            review.save()
            return redirect(reverse("books:book",  kwargs={'pk': pk}))
        else:
            return redirect(reverse("books:book",  kwargs={'pk': pk}))
                
                
                
def delreview(request, pk, movie_pk):
    review=models.Review.objects.get(pk=pk)
    review.delete()
    return redirect(reverse("movies:movie",  kwargs={'pk': movie_pk}))


def delbookreview(request, pk, book_pk):
    review=models.Review.objects.get(pk=pk)
    review.delete()
    return redirect(reverse("books:book",  kwargs={'pk': book_pk}))