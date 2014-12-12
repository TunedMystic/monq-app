import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import CreateView, DetailView, ListView
from .models import Snippet
from .forms import SnippetForm

class SnippetCreateView(CreateView):
  """
  Create a Snippet.
  """
  form_class = SnippetForm
  
  def _allowed_methods(self):
    return ["post"]
  
  def post(self, request, *args, **kwargs):
    """
    Handles POST requests, instantiating a form instance with the passed
    POST variables and then checked for validity.
    """
    form_class = self.get_form_class()
    form = self.get_form(form_class)
    # Give the form information about the User.
    form.request = request
    if form.is_valid():
        return self.form_valid(form)
    else:
        return self.form_invalid(form)
  
  def form_valid(self, form):
    savedSnippet = form.save()
    form.save_m2m()
    d = {
      "msg": "This post was a success.",
      "next": savedSnippet.url_code
    }
    return HttpResponse(json.dumps(d), content_type = "application/json")
    #return super(SnippetCreateView, self).form_valid(form)
  
  def form_invalid(self, form):
    return HttpResponseBadRequest(json.dumps(form.errors), content_type = "application/json")
    #return super(SnippetCreateView, self).form_invalid(form)


class SnippetDetailView(DetailView):
  """
  View a single Snippet.
  """
  template_name = "snippet/single.html"
  
  def _allowed_methods(self):
    return ["get"]
  
  def get_object(self):
    """
    Get Snippet based on url parameter 'urlcode'.
    """
    snippet = get_object_or_404(Snippet, url_code = self.kwargs.get("urlcode", None))
    return snippet


class SnippetListView(ListView):
  model = Snippet
  template_name = "snippet/all.html"
  paginate_by = 4
  page_kwarg = "page"
  
  def get_queryset(self):
    """
    Return the list of items for this view.
    """
    return self.model.objects.all()
    return super(SnippetListView, self).get_queryset(self)
  
