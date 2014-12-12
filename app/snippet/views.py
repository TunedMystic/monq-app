import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import CreateView
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
  
  
