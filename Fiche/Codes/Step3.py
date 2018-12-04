def on_key_down(key):
  # A gauche
  if key == keys.LEFT :
    # Où le boo est-il ? 
    boo.counter = durée_du_déplacement
    boo.moveX   = ?
  # A droite
  elif key == keys.RIGHT :
    # Où le boo est-il ? 
    boo.counter = durée_du_déplacement
    boo.moveX   = ?   
    
# Apellée 60 fois par seconde    
def update() :

  # Une animation est en cours
  if boo.counter > 0 :
    boo.counter -= 1
    
    # Déplacer le boo ici
    boo.x += boo.moveX