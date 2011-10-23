# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from searchs.search import SearchForm

def search(request):
    search_form = SearchForm()
    context = {
        'form': search_form,
    }
    return render_to_response('search.html', context, context_instance=RequestContext(request),)