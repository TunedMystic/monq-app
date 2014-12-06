"""
 A small script to write all the 'editor mode' variables.
 The variables are found in snippet/definitions/editormodes.py
"""

def deleteIllegalChars(x):
  """
  Deleted illegal characters that would
  cause an error in creating a variable name.
  
  Ex:
    j-s = 'javascript' # Illegal
    js  = 'javascript' # Legal
  """
  illegalChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "[", "]", "{", "}", "\\", "|", ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?" ]
  
  # Replace the token with nothing.
  for token in illegalChars:
    x = x.replace(token, "")
  
  x = x.replace(" ", "_")
  
  return "_" + x


lowercase = []
uppercase = []
variableNames = []
length = 0
filename = "output.py"

# Read all words.
with open("lowercase.txt", "r") as f:
  lowercase = f.readlines()

with open("uppercase.txt", "r") as f:
  uppercase = f.readlines()

with open("uppercase.txt", "r") as f:
  variableNames = f.readlines()
  length = len(lowercase)

# Clean all words.
for i, word in enumerate(lowercase):
  lowercase[i] = word.rstrip("\n")

for i, word in enumerate(uppercase):
  uppercase[i] = word.rstrip("\n")

for i, word in enumerate(variableNames):
  variableNames[i] = word.rstrip("\n")
  variableNames[i] = deleteIllegalChars(variableNames[i])
  variableNames[i] = variableNames[i].upper()

# Write python variables.
with open(filename, "w") as f:
  for i in range(length):
    f.write(variableNames[i] + ' = ' + '"' + lowercase[i] + '"')
    f.write("\n")
  
  f.write("\n\n")
  f.write("Modes = (\n")
  
  for i in range(length):
    f.write('  (' + variableNames[i] + ', "' + uppercase[i] + '"),')
    f.write("\n")
  
  f.write(")\n")
  