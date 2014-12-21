import json
import arrow
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import View, DetailView, ListView, TemplateView
from django.views.generic.edit import ProcessFormView
from django.contrib.auth import get_user_model, authenticate, login
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, Http404
from ipware.ip import get_ip, get_real_ip
from braces.views import LoginRequiredMixin
from .forms import DashboardForm

User = get_user_model()

class LoginTest(View):
  template_name = "userextension/testlogin.html"
  
  def _allowed_methods(self):
    return ["post"]
  
  def get(self, request):
    print "hello"
    harry = authenticate(username = "harry", password = "harry")
    if harry is not None:
      if not request.user == harry:
        login(request, harry)
        import pdb; pdb.set_trace();
        return render(request, self.template_name, {"msg": "Hello " + harry.username + " !", "u": request.user})
      else:
        return render(request, self.template_name, {"msg": "How's it going " + harry.username + " ?", "u": request.user})
    else:
      return HttpResponseBadRequest("The user does not exist.")


class LoginView(TemplateView):
  template_name = "userextension/login.html"
  
  def get_context_data(self, **kwargs):
    context = super(LoginView, self).get_context_data(**kwargs)
    context["request"] = self.request
    return context
    

class UserProfileView(DetailView):
  """
  View a person's public profile.
  If viewing youself, you will be redirected to the dashboard.
  """
  model = User
  template_name = "userextension/profile.html"
  limit_by = 10
  
  def get(self, request, *args, **kwargs):
    """
    If the User views their own public profile, 
    redirect to the 'dashboard' url.
    """
    if request.user.username == kwargs.get("usrname", ""):
      return HttpResponseRedirect(reverse("userext:dashboard"))
    return super(UserProfileView, self).get(request, *args, **kwargs)
  
  def get_object(self):
    """
    Get User based on url parameter 'usrname'.
    """
    usr = get_object_or_404(self.model, username = self.kwargs.get("usrname", None))
    return usr
  
  def get_context_data(self, **kwargs):
    context = super(UserProfileView, self).get_context_data(**kwargs)
    usr = context["object"]
    # Collect recent Snippets made by the public User.
    context["recentSnippets"] = usr.snippet_set.all()\
                                   .exclude(visibility = "private")\
                                   .order_by("-date_added_raw")[:self.limit_by]
    return context


class UserDashboardView(LoginRequiredMixin, DetailView, ProcessFormView):
  """
  Render the (Logged-in) user's dashboard.
  Accept Ajax form to update User's (userprofile) data.
  """
  model = User
  form_class = DashboardForm
  template_name = "userextension/dashboard.html"
  limit_by = 10
  login_url = "/login/"
  
  def get_object(self):
    # Return the authenticated user.
    if self.request.user and not self.request.user.is_anonymous():
      return self.request.user
    else:
      # User is not logged in... redirect to login page....
      raise Http404
  
  def get_context_data(self, **kwargs):
    context = super(UserDashboardView, self).get_context_data(**kwargs)
    usr = context["object"]
    # Get the most recent Snippets made.
    context["recentMadeSnippets"] = usr.snippet_set.all().order_by("-date_added_raw")[:self.limit_by]
    # Get the most recent Snippets liked.
    context["recentLikedSnippets"] = usr.snippetlike_set.all().order_by("-date_liked")[:self.limit_by]
    # Get the User login details.
    context["loginDetails"] = usr.userprofile.getLoginDetailsList()
    # Build the full url of the User's public profile (This is used if the User has no website).
    context["profileUrl"] = self.request.build_absolute_uri(reverse("userext:profile", kwargs={"usrname": self.object.username}))
    return context
  
  def post(self, request, *args, **kwargs):
    """
    Validates the DashboardForm and updates UserProfile.
    """
    form = self.form_class(request.POST, instance = request.user.userprofile)
    if form.is_valid():
        return self.form_valid(form)
    else:
        return self.form_invalid(form)
  
  def form_valid(self, form):
    savedSnippet = form.save()
    d = {
      "msg": "Profile successfully updated.",
    }
    return HttpResponse(json.dumps(d), content_type = "application/json")
  
  def form_invalid(self, form):
    return HttpResponseBadRequest(json.dumps(form.errors), content_type = "application/json")


class UserSnippetsView(LoginRequiredMixin, ListView):
  """
  Display all Snippets of the (logged-in) User.
  Results are paginated.
  """
  #model = Snippet
  template_name = "userextension/usersnippets.html"
  paginate_by = 4
  page_kwarg = "pg"
  login_url = "/login/"
  
  def get_queryset(self):
    """
    Returns the (paginated) results of all Snippets made by the (logged-in) User.
    """
    return self.request.user.snippet_set.all().order_by("-date_added_raw")


class UserSnippetLikesView(LoginRequiredMixin, ListView):
  """
  Displays all Snippets liked by the (logged-in) User.
  Results are paginated.
  """
  #model = Snippet
  template_name = "userextension/userlikedsnippets.html"
  paginate_by = 4
  page_kwarg = "pg"
  login_url = "/login/"
  
  def get_queryset(self):
    """
    Returns the (paginated) results of all Snippets liked by the (logged-in) User.
    """
    return self.request.user.snippetlike_set.all().order_by("-date_liked")
