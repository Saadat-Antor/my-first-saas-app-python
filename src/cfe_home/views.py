from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from pprint import pprint

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "paragraph": "This is a paragraph from render context.",
        "page_visit_count": queryset.count()
    }
    html_template = "home.html"
    PageVisit.objects.create()
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return render(request, html_template, my_context)