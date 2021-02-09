from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
import random
import markdown2

md=markdown2.Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_entry(request, title):
    if title in util.list_entries():
        return render(request, "encyclopedia/get_entry.html", {
            "title": title,
            "entry": md.convert(util.get_entry(title))
        })
    else:
        return render (request, "encyclopedia/error.html", {
                "error_message": "Requested page was not found"
            })
    
def search_result(request):

    full_match = False
    partial_matches = []

    if request.method == 'GET':
        title = request.GET['q']
        for entry in util.list_entries():
            if title.lower() == entry.lower():
                full_match = True
                break
            elif title.lower() in entry.lower():
                partial_matches.append(entry)
            
        if full_match:
            return render(request, "encyclopedia/get_entry.html", {
            "title": title,
            "entry": md.convert(util.get_entry(title))
            })
        elif partial_matches:
            return render(request, "encyclopedia/index.html", {
            "entries": partial_matches
            })
        else:
            return render (request, "encyclopedia/error.html", {
                "error_message": "Oops, nothing found"
            })

def new_page(request):
    
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        for entry in util.list_entries():
            if title.lower() == entry.lower():
                return render (request, "encyclopedia/error.html", {
                "error_message": "This title already exists"
            })
            
        util.save_entry(title, content)
        return render(request, "encyclopedia/get_entry.html", {
        "title": title,
        "entry": md.convert(util.get_entry(title))
        })

    return render (request, "encyclopedia/new_page.html", {})

def edit_page(request, title):
    
    content = util.get_entry(title)
    
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        return render(request, "encyclopedia/get_entry.html", {
        "title": title,
        "entry": md.convert(util.get_entry(title))
        })
    
    return render(request, "encyclopedia/edit_page.html", {
        "title": title,
        "content": content
        })
    
def random_page (request):
    title = random.choice(util.list_entries())
    return render(request, "encyclopedia/get_entry.html", {
        "title": title,
        "entry": md.convert(util.get_entry(title))
    })

