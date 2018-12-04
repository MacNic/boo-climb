# Si vous utilisez mu editor, commentez
# la ligne 'import pgzrun'
#import pgzrun

TITLE   = 'Boo climb'
WIDTH   = 1366
HEIGHT  = 768

# Met à jour les objects        
def update() :
    return
    
# Dessine les objects         
def draw():
     
    screen.blit('sky', (0, 0))
    tree.draw()
    
    return 

####################
## Initialisation ##
####################

# On créé et on positionne l'arbre
tree     = Actor('tree', anchor=('left', 'top'))
tree.pos = ((WIDTH - tree.width) / 2, 0)
    
# Si vous utilisez mu editor, commentez
# la ligne 'pgzrun.go()'
#pgzrun.go()