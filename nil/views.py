from django.shortcuts import render


def error404(request):
  """
  Render 404 Not Found page.
  """
  return render(request, "nil/http404.html")


def error500(request):
  """
  Render 500 Internal Server Error page.
  """
  return render(request, "nil/http500.html")
