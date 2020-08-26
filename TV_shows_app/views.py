from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def index(request):
    return redirect('/shows')

def new(request):
    return render(request, "newShow.html")

def create(request):
    errors = Show.objects.showValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['date'], desc=request.POST['desc'])
    
    return redirect(f'/shows/{new_show.id}')

def View(request, showid):
    current_show = Show.objects.get(id=showid)
    context = {
        "show" : current_show
    }
    return render(request, "view.html", context)


def delete(request, showid):
    Show.objects.get(id=showid).delete()
    return redirect('/shows')


def edit(request, showid):
    edit_show = Show.objects.get(id=showid)
    context = {
        "show" : edit_show
    }
    return render(request, "edit.html", context)

def update(request, showid):
    errors = Show.objects.showValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{showid}/edit')

    updated_show = Show.objects.get(id=showid)
    updated_show.title = request.POST['title']
    updated_show.network = request.POST['network']
    updated_show.release_date = request.POST['date']
    updated_show.desc = request.POST['desc']
    updated_show.save()
    return redirect(f'/shows/{showid}')

def shows(request):
    all_shows = Show.objects.all()
    context = {
        "show" : all_shows
    }
    return render(request, "shows.html", context)
