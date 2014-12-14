from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView
from django.contrib.auth import get_user_model, authenticate, login
from django.http import Http404, HttpResponseBadRequest
from ipware.ip import get_ip, get_real_ip
from braces.views import LoginRequiredMixin

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


class UserProfileView(DetailView):
  """
  View a person's public profile.
  If viewing youself, you will be redirected to the dashboard.
  """
  model = User
  template_name = "userextension/profile.html"
  limit_by = 10
  
  def get_object(self):
    """
    Get User based on url parameter 'usrname'.
    """
    usr = get_object_or_404(self.model, username = self.kwargs.get("usrname", None))
    return usr
  
  def get_context_data(self, **kwargs):
    context = super(UserProfileView, self).get_context_data(**kwargs)
    usr = context["object"]
    context["recentSnippets"] = usr.snippet_set.all().order_by("-date_added_raw")[:self.limit_by]
    return context


class UserDashboardView(LoginRequiredMixin, DetailView):
  """
  Render the (Logged-in) user's dashboard.
  """
  model = User
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
