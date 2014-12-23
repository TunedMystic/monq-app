import arrow
from ipware.ip import get_ip, get_real_ip

IP_NOT_FOUND = "N/A"

def getIp(request):
  """
  Attempt to get the ip address of the logged-in user.
  """
  ipAddress = get_real_ip(request)
  if ipAddress is not None:
    return ipAddress
  else:
    ipAddress = get_ip(request)
    if ipAddress is not None:
      return ipAddress
    else:
      IP_NOT_FOUND


def getIsoDate():
  """
  Returns the current date in iso string format.
  """
  return arrow.now().datetime.isoformat()


def isoToDate(isostring):
  """
  Accepts an isoformat-ted string and
  returns a datetime instance.
  """
  return arrow.get(isostring).datetime


def formatDate(d):
  """
  Accepts a datetime object and returns 
  a string representation.
  """
  return d.strftime("%A %b %d, %Y - %I:%M:%S %p")
