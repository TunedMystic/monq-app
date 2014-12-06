class LoginHistory(object):
  """
  Responsible for managing 'User' login information.
  """
    Max_Amount = 5
     
    def __init__(self, h = []):
        self.history = []
        for element in h:
          self.addLogin(element)
    
    def addLogin(self, x):
        if len(self.history) == self.Max_Amount:
          self.history.pop(0)
        self.history.append(x)
    
    def __repr__(self):
        return "%s" %(self.history)