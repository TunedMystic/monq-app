from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model, authenticate, login
from django.http import Http404, HttpResponseBadRequest
from ipware.ip import get_ip, get_real_ip

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
    
