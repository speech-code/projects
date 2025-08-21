from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import UserRegisterForm, NoteForm, TagForm, CategoryForm
from .models import Note, Tag, Category

def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("notes:note_list")
    else:
        form = UserRegisterForm()
    return render(request, "notes/register.html", {"register_form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("notes:note_list")
    else:
        form = AuthenticationForm()
    return render(request, "notes/login.html", {"login_form": form})

@login_required
def logout_request(request):
    logout(request)
    return redirect("notes:login")

@login_required
def note_list(request):
    query = request.GET.get('q')
    tag_filter = request.GET.get('tag')
    category_filter = request.GET.get('category')

    notes = request.user.notes.all()

    if query:
        notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query))
    if tag_filter:
        notes = notes.filter(tags__name=tag_filter)
    if category_filter:
        notes = notes.filter(category__name=category_filter)

    tags = Tag.objects.all()
    categories = Category.objects.all()

    return render(request, "notes/note_list.html", {"notes": notes, "tags": tags, "categories": categories})

@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            form.save_m2m() # Save many-to-many relationships for tags
            return redirect("notes:note_list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})

@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, "notes/note_detail.html", {"note": note})

@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes:note_detail", pk=pk)
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        note.delete()
        return redirect("notes:note_list")
    return render(request, "notes/note_confirm_delete.html", {"note": note})

@login_required
def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes:note_list")
    else:
        form = TagForm()
    return render(request, "notes/tag_form.html", {"form": form})

@login_required
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes:note_list")
    else:
        form = CategoryForm()
    return render(request, "notes/category_form.html", {"form": form})
