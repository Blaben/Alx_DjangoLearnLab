from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Book, library, UserProfile
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import BookForm, CustomUserCreationForm  # assuming you created a custom form

# ----------------------
# Role test functions
# ----------------------

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'member'


# ----------------------
# Book Views
# ----------------------

@login_required
@user_passes_test(is_librarian)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})


@login_required
@user_passes_test(is_librarian)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/confirm_delete.html', {'book': book})


@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ----------------------
# Library View
# ----------------------

class ViewLibrary(DetailView):
    model = library
    template_name = 'relationship_app/library_detail.html'


# ----------------------
# Role-based Views
# ----------------------

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome to the Admin Dashboard")


@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian Page")


@login_required
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome to the Member Area")


# ----------------------
# User Registration View
# ----------------------

class RegisterView(CreateView):
    form_class = CustomUserCreationForm  # Make sure this exists and extends UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"


# ----------------------
# UserProfile Signals
# ----------------------

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
