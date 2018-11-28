#import pgzrun
import random

random.seed()

TITLE                       = 'Boo climb'
WIDTH                       = 1366
HEIGHT                      = 768
NB_BRANCHES_PER_SIDE        = 5
MOVE_SPEED                  = 12
BOMB_START_AT_SCORE         = 15
BAD_BRANCHES_START_AT_SCORE = 10
TIME_FOR_BRANCH_TO_BREAK    = 0.3

# Description
#   This function sets the position of
#   the specified left branch
#
# Parameters
#   i - The branch index
#
# Returns
#   Nothing
#
def SetLeftBranchPos(i) :
    if left_branches[i] :
        left_branches[i].pos = ((WIDTH - tree.width) / 2) + 36 - left_branches[i].width, i * 200 - left_branches[i].height

# Description
#   This function sets the position of
#   the specified right branch
#
# Parameters
#   i - The branch index
#
# Returns
#   Nothing
#
def SetRightBranchPos(i) :
    if right_branches[i] :
        right_branches[i].pos  = ((WIDTH - tree.width) / 2) + tree.width - 36, i * 200 - right_branches[i].height
    
# Description
#   This function sets the position of
#   the all the branches in the stable state
#
# Parameters
#   None
#
# Returns
#   Nothing
#    
def SetBranchesPosition() :
    for i in range(0, NB_BRANCHES_PER_SIDE):
        SetLeftBranchPos(i)   
        SetRightBranchPos(i)
    
# Description
#   This function sets the position of
#   the specified left branch
#
# Parameters
#   i - The branch index
#
# Returns
#   Nothing
#
def SetLeftBombPos(i) :
    if left_bombs[i] :
        left_bombs[i].pos = ((WIDTH - tree.width) / 2) - 100, i * 200 - 50 - left_branches[i].height

# Description
#   This function sets the position of
#   the specified right branch
#
# Parameters
#   i - The branch index
#
# Returns
#   Nothing
#
def SetRightBombPos(i) :
    if right_bombs[i] :
        right_bombs[i].pos = ((WIDTH - tree.width) / 2) + tree.width + 45, i * 200 - 50 - right_branches[i].height
    
# Description
#   This function sets the position of
#   the all the branches in the stable state
#
# Parameters
#   None
#
# Returns
#   Nothing
#    
def SetBombsPosition() :
    for i in range(0, NB_BRANCHES_PER_SIDE):
        SetLeftBombPos(i)   
        SetRightBombPos(i)

# Description
#   This function generates a valid
#   combination for the branches
#
# Parameters
#   _Value - The combination value
#
# Returns
#   The pair representing the { left, right } branches
#
def GenerateBranchLevelCombination() :
    
    if boo.score > BAD_BRANCHES_START_AT_SCORE :
        value = random.randint(0, 7)
    else :
        value = random.randint(0, 2)
    
    if value == 0 :
        return Actor('good_branch_left',  anchor=('left', 'top')), Actor('good_branch_right', anchor=('left', 'top')) 
    elif value == 1 :
        return Actor('good_branch_left',  anchor=('left', 'top')), None
    elif value == 2 :
        return None, Actor('good_branch_right', anchor=('left', 'top')) 
    elif value == 3 :
        return Actor('bad_branch_left',   anchor=('left', 'top')), Actor('good_branch_right', anchor=('left', 'top')) 
    elif value == 4 :
        return Actor('good_branch_left',  anchor=('left', 'top')), Actor('bad_branch_right',  anchor=('left', 'top')) 
    elif value == 5 :
        return Actor('bad_branch_left',   anchor=('left', 'top')), Actor('bad_branch_right',  anchor=('left', 'top')) 
    elif value == 6 :
        return Actor('bad_branch_left',  anchor=('left', 'top')), None 
    else :
        return None, Actor('bad_branch_right', anchor=('left', 'top')) 

# Description
#   This function generates a valid
#   combination for the bombs based
#   on the given branch pattern
#
# Parameters
#   branches - The branch combination
#
# Returns
#   The pair representing the { left, right } bombs
#
def GenerateBombCombination(branches) :
    
    # Is there two branches ?
    if branches[0] and branches[1] :

        # Don't place bomb until score is 20
        if boo.score > BOMB_START_AT_SCORE :    
            # Pick up a value randomly
            value = random.randint(1, 3)
        else :
            value = 0

        # No bomb
        if value == 0 :
            return None, None 
        # Bomb is on the left
        elif value == 1 :
            return Actor('bomb', anchor=('left', 'top')), None 
        # Bomb is on the right
        elif value == 2 :
            return None, Actor('bomb', anchor=('left', 'top')) 

    # There is a single branch
    # thus we cannot place bomb
    return None, None

# Description
#   This function resets the branches
#   and bombs position
#
# Parameters
#   None
#
# Returns
#   Nothing
#    
def ResetBranchesPosition() :

    for i in range(0, NB_BRANCHES_PER_SIDE) :
        
        # Reset branches and bombs positions
        SetLeftBranchPos (i)
        SetRightBranchPos(i)
        SetLeftBombPos   (i)
        SetRightBombPos  (i)
    
# Description
#   This function updates the branches
#   once they have moved
#
# Parameters
#   None
#
# Returns
#   Nothing
#
def UpdateBranches() :

    # Each branches has moved down one level
    for i in range(0, NB_BRANCHES_PER_SIDE - 1) :
        idx = NB_BRANCHES_PER_SIDE - 2 - i
        
        left_branches [idx + 1] = left_branches [idx]
        right_branches[idx + 1] = right_branches[idx]

        left_bombs [idx + 1] = left_bombs[idx]
        right_bombs[idx + 1] = right_bombs[idx]
    
    # Randomly generate next top branch that
    # will appear at the top of the screen
    NextBranches = GenerateBranchLevelCombination()
    NextBombs    = GenerateBombCombination(NextBranches)
    
    left_branches [0] = NextBranches[0]
    right_branches[0] = NextBranches[1]
    
    left_bombs [0] = NextBombs[0]
    right_bombs[0] = NextBombs[1]

# Description
#   This function indicates
#   whether the game is over
#   or not
#
# Parameters
#   None
#
# Returns
#   True    - The game is over
#   False   - The game is not over
#
def IsGameOver() :
    return boo.y > HEIGHT

# Description
#   This function restarts
#   the game
#
# Parameters
#   None
#
# Returns
#   Nothing
#
def RestartGame() :
    boo.moveX       = 0
    boo.moveY       = 0
    boo.counter     = 0
    boo.IsDead      = False
    boo.Direction   = ""
    boo.score       = 0
    boo.pos         = boo.RightPosition, boo.DefaultY

    # Generate initial situation
    for i in range(0, NB_BRANCHES_PER_SIDE - 1) :

        Branches = GenerateBranchLevelCombination()
        Bombs    = GenerateBombCombination(Branches)
        
        left_branches [i] = Branches[0]
        right_branches[i] = Branches[1]
        
        left_bombs [i] = Bombs[0]
        right_bombs[i] = Bombs[1]

    # Make sure the first level where the boo is is clean
    left_branches [NB_BRANCHES_PER_SIDE - 1] = Actor('good_branch_left',  anchor=('left', 'top'))
    right_branches[NB_BRANCHES_PER_SIDE - 1] = Actor('good_branch_right', anchor=('left', 'top'))    
    left_bombs [NB_BRANCHES_PER_SIDE - 1] = None
    right_bombs[NB_BRANCHES_PER_SIDE - 1] = None
    
    ResetBranchesPosition()

# Description
#   This function is called when
#   the user presses a key
#
# Parameters
#   key - The key pressed
#
# Returns
#   Nothing
#
def on_key_down(key):

    # Do we need to restart game ?
    if key == keys.RETURN and IsGameOver() :
        RestartGame()

    Move = False
    
    # Make sure nothing is currently moving
    if boo.counter == 0 and tree.counter == 0 :
        
        # We need to go  left
        if key == keys.LEFT :
            boo.counter     = MOVE_SPEED
            boo.moveX       = (boo.LeftPosition - boo.x) / boo.counter
            boo.Direction   = "Left"
            Move            = True

        # We need to go right
        if key == keys.RIGHT :
            boo.counter     = MOVE_SPEED
            boo.moveX       = (boo.RightPosition - boo.x) / boo.counter
            boo.Direction   = "Right"
            Move            = True
        
        if Move :    
            tree.movedown = True
            tree.counter  = MOVE_SPEED
            clock.unschedule(OnBranchBroken)
            sounds.woosh.play()

# Description
#   This function moves the 
#   branches down if required
#
# Parameters
#   None
#
# Returns
#   Nothing
#
def UpdateTree() :
    
    # Do we need to move ?
    if tree.counter > 0 : 
        
        # Move branches down
        for i in range(0, NB_BRANCHES_PER_SIDE) :
            if left_branches [i] :
                left_branches [i].y += 200 / MOVE_SPEED
            
            if right_branches[i] :
                right_branches[i].y += 200 / MOVE_SPEED
        
        # Move bombs down
        for i in range(0, NB_BRANCHES_PER_SIDE) :
            
            if left_bombs [i] :
                left_bombs [i].y += 200 / MOVE_SPEED
            
            if right_bombs[i] :
                right_bombs[i].y += 200 / MOVE_SPEED
        
        tree.counter -= 1
        
        # We are done moving
        if tree.counter == 0 :
            
            # Update the branches
            UpdateBranches()
            
            # Make sure they are at the appropriated spot
            ResetBranchesPosition()
                
            
# Description
#   This function is called 
#   when a branch creeks
#
# Parameters
#   None
#
# Returns
#   Nothing
#
def OnBranchBroken() :
    
    if boo.Direction == "Left" :
        left_branches [NB_BRANCHES_PER_SIDE - 1] = None
    else :
        right_branches[NB_BRANCHES_PER_SIDE - 1] = None
    
    sounds.branch_crack.play()
    sounds.dead.play()
    
    # boo is dead    
    boo.IsDead = True

# Description
#   This function checks wheter
#   the boo is dead or nothing
#
# Parameters
#   None
#
# Returns
#   True    - The boo is dead
#   False   - The boo is not dead
#
def IsBooDead() :

    Bomb   = None
    Branch = None

    # We were going left
    if boo.Direction == "Left" :
        Bomb    = left_bombs   [NB_BRANCHES_PER_SIDE - 1]
        Branch  = left_branches[NB_BRANCHES_PER_SIDE - 1]
    else :    
        Bomb    = right_bombs   [NB_BRANCHES_PER_SIDE - 1]
        Branch  = right_branches[NB_BRANCHES_PER_SIDE - 1]

    # Is it a bad branch
    if Branch and (Branch.image == "bad_branch_left" or Branch.image == "bad_branch_right") :
        clock.schedule(OnBranchBroken, TIME_FOR_BRANCH_TO_BREAK)
    
    if Bomb :
        sounds.bomb.play()
    
    # There is a bomb or there is no branch
    return (Bomb or not Branch)
        
# Description
#   This function moves the 
#   boo if required
#
# Parameters
#   None
#
# Returns
#   Nothing
#
def UpdateBoo() :

    if boo.IsDead :
        boo.y += 10
    
    elif boo.counter > 0 :
        boo.x += boo.moveX
        
        if boo.counter > (MOVE_SPEED / 2) :
            boo.y -= 5
        else :
            boo.y += 5
            
        boo.counter -= 1
    
        # We are done moving
        if boo.counter == 0 :
            boo.IsDead = IsBooDead()
            
            if not boo.IsDead :
                boo.score += 1
            else :
                sounds.dead.play()
                
    
# Description
#   This function updates the
#   objects position if required
#
# Parameters
#   None
#
# Returns
#   Nothing
#        
def update() :
    
    UpdateTree()
    UpdateBoo ()
    
# Description
#   This function redraws the
#   objects on screen if required
#
# Parameters
#   None
#
# Returns
#   Nothing
#            
def draw():
    screen.blit('sky', (0, 0))
    tree.draw()
    for branch in left_branches :
        if branch :
            branch.draw()
    for branch in right_branches :
        if branch :
            branch.draw()
    for bomb in left_bombs :
        if bomb :
            bomb.draw()
    for bomb in right_bombs :
        if bomb :
            bomb.draw()
    boo.draw()
        
    if IsGameOver() :
        screen.draw.text("Game over", (WIDTH / 2 - 90, HEIGHT / 2), fontsize=48, color=(255, 0, 0))
    
    screen.draw.text("Score: {0}".format(boo.score), (0, 0), fontsize=48, color=(255, 255, 255))

#######################
## START OF THE GAME ##
#######################

# Start the background music
#music.play("kalimba")

# Create the tree
tree         = Actor('tree', anchor=('left', 'top'))
tree.pos     = ((WIDTH - tree.width) / 2, 0)
tree.counter = 0

# Define the branches
left_branches   = []
right_branches  = []
   
# Define the bombs
left_bombs    = []
right_bombs   = []

# Create and initializes the branches
for i in range(0, NB_BRANCHES_PER_SIDE):
    left_branches.append (Actor('good_branch_left',  anchor=('left', 'top')))
    right_branches.append(Actor('good_branch_left',  anchor=('left', 'top')))
    
# Create and initializes the bombs
for i in range(0, NB_BRANCHES_PER_SIDE):
    left_bombs.append (Actor('bomb',  anchor=('left', 'top')))
    right_bombs.append(Actor('bomb',  anchor=('left', 'top')))

# Create and initialize the boo
boo = Actor('boo', anchor=('left', 'top'))

# The boo will only have 2 position : on the left or on the right
boo.LeftPosition  = ((WIDTH - tree.width - left_branches[0].width) / 2) - (boo.width/2) + 57
boo.RightPosition = ((WIDTH + tree.width + left_branches[0].width) / 2) - boo.width - 5

# So after each move, it will land at the same Y value
boo.DefaultY      = 750 - left_branches[0].height

# boo starts on the right (arbitrary)
boo.pos           = boo.RightPosition, boo.DefaultY

# The counters to move the boo
boo.moveX         = 0
boo.moveY         = 0
boo.counter       = 0
boo.Direction     = ""
boo.IsDead        = False
boo.score         = 0

# Generate initial situation
RestartGame()

#pgzrun.go()