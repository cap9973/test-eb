from django.views.generic import ListView, DetailView, CreateView, UpdateView
from books.models import Book
from reviews.forms import ReivewInput


class BooksView(ListView):
  
  model = Book
  paginate_by = 15
  paginate_orphans = 5
  ordering = "-created_at"
  context_object_name = "books"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_title'] = "All Books"
    return context


class BookDetail(DetailView):
  model = Book
  context_object_name = 'book'
  
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.kwargs['pk']를 통해서 url에서 pk값을 받을 수 있습니다.
        # url은 `path('<pk>/', PhotoView.as_view())으로 구현되어있어서 해당 pk 부분을 받아옵니다.`
        review=Book.objects.get(pk=self.kwargs['pk'])
        context['review'] = review.reviews.all()
        context['form']=ReivewInput
        return context


class CreateBook(CreateView):
  model = Book
  fields = (
    "title",
    "year",
    "cover_image",
    "rating",
    "category",
    "writer",
  )


class UpdateBook(UpdateView):
  model = Book
  fields = (
    "title",
    "year",
    "cover_image",
    "rating",
    "category",
    "writer",
  )