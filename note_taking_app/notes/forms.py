from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Category, Note, Tag, User


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "tags", "category"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
