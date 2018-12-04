# Cette variable contient l'image 'tree'
variable1 = Actor('tree', anchor=('left', 'top'))

# Cette variable ne contient rien
variable2 = None

def draw() :

  # Ce test est vrai, variable1 contient quelque chose
  if variable1 :
    variable1.draw()
    
  # Ce test est faux, variable2 ne contient rien
  if variable2 :
    variable2.draw()