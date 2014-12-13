import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.views.generic.edit import FormMixin, ProcessFormView
from django.db.models import F
from .models import Snippet, SnippetExtras
from .forms import SnippetForm


class qSession(object):
  """
  Simple mixin to clear the 'searchSnippetQ' session variable.
  """
  def dispatch(self, request, *args, **kwargs):
    # Delete the search query in request.session.
    request.session.pop("searchSnippetQ", None)
    return super(qSession, self).dispatch(request, *args, **kwargs)


class SnippetCreateView(qSession, CreateView):
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
  
  def form_invalid(self, form):
    return HttpResponseBadRequest(json.dumps(form.errors), content_type = "application/json")


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
    # Update the 'hits' counter.
    SnippetExtras.objects.filter(pk = snippet.snippetextras.id).update(hits = F("hits") + 1)
    return snippet


class SnippetListView(qSession, ListView):
  """
  List all Snippets (with pagination).
  """
  model = Snippet
  template_name = "snippet/all.html"
  paginate_by = 4
  page_kwarg = "pg"
  
  def get_queryset(self):
    """
    Return the list of items for this view.
    """
    return self.model.objects.all().order_by("-_date_added")


class SnippetSearchFormView(qSession, TemplateView):
  def get(self, request, *args, **kwargs):
    return super(SnippetSearchFormView, self).get(request, *args, **kwargs)


class SnippetSearchView(ListView, ProcessFormView):
  """
  Search Snippets (with pagination).
  """
  model = Snippet
  template_name = "snippet/search.html"
  paginate_by = 3
  page_kwarg = "pg"
  
  def dispatch(self, request, *args, **kwargs):
    """
    Set request.method to 'POST' if session is found.
    """
    if not request.method == "POST":
      request.method = "POST"
    return super(SnippetSearchView, self).dispatch(request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    """
    Process search results.
    """
    # Overwrite the session variable.
    if request.POST.get("searchQ", None):
      request.session["searchSnippetQ"] = request.POST["searchQ"]
    
    self.object_list = self.get_queryset()
    # No search results. Redirect to Search form.
    if isinstance(self.object_list, type(None)):
      return HttpResponseRedirect(reverse("snippet:searchFormSnippet"))
    return self.render_to_response(self.get_context_data())
  
  def get_queryset(self):
    """
    Return the list of items for this view.
    """
    searchQ = self.request.POST.get("searchQ", None) or self.request.session.get("searchSnippetQ", None)
    # Niether the POST parameter or the Session variable was found.
    # In which case, return None.
    if not searchQ:
      return None
    
    results = self.model.objects.filter(title__icontains=searchQ).distinct()
    return results
