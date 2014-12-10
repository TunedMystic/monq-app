from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model, authenticate, login
from django.http import Http404, HttpResponseBadRequest

class LoginTest(View):
  template_name = "userextension/testlogin.html"
  
  def _allowed_methods(self):
    return ["post"]
  
  def get(self, request):
    
    harry = authenticate(username = "harry", password = "harry")
    if harry is not None:
      if harry.is_active:
        login(request, harry)
        return render(request, self.template_name, {"msg": "Hello " + str(harry.username)})
      else:
        return HttpResponseBadRequest("The user does not exist.")
    else:
      raise Http404
    
