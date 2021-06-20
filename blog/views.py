from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    """To create a post, a user must be logged in."""
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        """Set the author of the form to be the logged user."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """To update a post, a user must be logged in. A user can change only his/her posts."""
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        """Set the author of the form to be the logged user."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """If a user passes certain test conditions. If a user is an author of the post."""
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """To delete a view a user must be logged in and the user is the author of the post."""
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        """If a user passes certain test conditions. If a user is an author of the post."""
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    return render(request, 'about.html')
