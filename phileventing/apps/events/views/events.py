from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext
from django.conf import settings

from feedreader.parser import from_url
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def index(request):
    return render_to_response('events/choose_category.html', locals(), context_instance=RequestContext(request))
    
@login_required
def events_by_category(request, category, cat_id):
    ENTRIES_PER_PAGE = 5
    
    phillyfun_url = "http://www.phillyfunguide.com/feeds/event/rss"
    url = "%s/%s/" % (phillyfun_url, cat_id)
    
    parsed = from_url(url)
    entry_list = parsed.entries
    
    paginator = Paginator(entry_list, ENTRIES_PER_PAGE)
    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        entries = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        entries = paginator.page(paginator.num_pages)
    
    return render_to_response('events/get_by_category.html', locals(), context_instance=RequestContext(request))