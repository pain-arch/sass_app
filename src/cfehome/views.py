import pathlib
from django.shortcuts import render
from django.http import HttpResponse


this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    my_title = "Home Page"
    my_context ={
        "page_title": my_title
    }
    html_template = "base.html"
    #html_file_path = this_dir / "home.html"
    #html_ = html_file_path.read_text()
    return render(request, html_template, my_context)