from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import to_do_list, item
from .forms import create_new_list

def index(response, id):
    ls = to_do_list.objects.get(id=id)

    if ls not in response.user.todolist.all():
        return HttpResponseRedirect("/")

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("new_item"):
            txt = response.POST.get("new")

            if len(txt) > 2: 
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid input")
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect("/login")
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = create_new_list(response.POST)
        if not response.user.is_authenticated:
            return HttpResponseRedirect("/login")
        if form.is_valid():
            name = form.cleaned_data["name"]

            lst = to_do_list(name=name)
            lst.save()
            response.user.todolist.add(lst)

            return HttpResponseRedirect("/%i" %lst.id)
    else:
        form = create_new_list()
    return render(response, "main/create.html", {"form": form})