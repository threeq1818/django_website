from django.views import generic
from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instaces_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    # # your own name for the list as a template variable
    # context_object_name = 'my_book_list'
    # # Get 5 books containing the title war
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    # # Specify your own template name/location
    # template_name = 'books/my_arbitrary_template_name_list.html'

    def get_queryset(self):
        # Get 5 books containing the title war
        return Book.objects.filter()[:5]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

    # # your own name for the list as a template variable
    # context_object_name = 'my_book_list'
    # # Get 5 books containing the title war
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    # # Specify your own template name/location
    # template_name = 'books/my_arbitrary_template_name_list.html'

    def get_queryset(self):
        # Get 5 books containing the title war
        return Author.objects.filter()[:5]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, primary_key):
        author = get_object_or_404(Author, pk=primary_key)
        return render(request, 'catalog/author_detail.html', context={'author': author})
