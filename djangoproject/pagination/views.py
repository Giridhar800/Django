from django.shortcuts import render
from pagination.models import Book
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.core.paginator import Paginator


# Create your views here.
# def page_view(request):
#     all_pages = Book.objects.all().order_by('id')
#     paginator = Paginator(all_pages, 3, orphans=1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'pages.html', {'page_obj':page_obj})

class PageListView(ListView):
    model = Book
    template_name = "pages.html"
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 1
    def get_context_data(self, *args, **kwargs):
        try:
            return super(PageListView,self).get_context_data(*args,**kwargs)
        except Http404:
            self.kwargs['page']=1
            return super(PageListView,self).get_context_data(*args, **kwargs)

class PageDetailView(DetailView):
    model = Book
    template_name = 'detaile.html'


