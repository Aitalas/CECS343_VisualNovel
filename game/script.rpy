# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


#----------------------------------------------------------------------------------
#       Init block
#       Some functions for interacting with the screens maybe?
#----------------------------------------------------------------------------------
init python:
    # array of clues, in this case Strings
    clues_array = ["item 1", "item 2"]
    
    # functions for adding clues
    def add_clue(string_clue):
        clues_array.append(string_clue)
        
#----------------------------------------------------------------------------------
#       Screens
#       Clues
#----------------------------------------------------------------------------------
screen clues_button:
    #create button that shows the clues screen when clicked
    textbutton "Review Clues" action Show("clues")
    
screen clues:   
    modal True          #prevent user from clicking on other stuff while clues is open
    
    frame:
        yfill True      #expand to fill available vertical space
        xfill False     #don't fill available horizontal space
        xalign 1.0      #align to the right side
        xsize 600       #set to 400px width
        xpadding 10     #set padding
        ypadding 10
    
        vbox:                   #add vbox to frame, must indent
            spacing 10          #10px between each element
            box_wrap True       
            
            hbox:               #title box 
                spacing 10
                text "Clues" size 30
                textbutton "Hide Clues" action Hide("clues")
        
            #add items from clues_array
            for i in range(0, len(clues_array)):
                    text clues_array[i]
            
#----------------------------------------------------------------------------------
#       Start game here
#----------------------------------------------------------------------------------

# The game starts here.
label start:
    show screen clues_button
    
    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    e "Oh look, you found [Item 3]!"
    
    #$ add_clue("item 3")

    return
