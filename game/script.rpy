# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

#----------------------------------------------------------------------------------
#       Declare images, sounds, characters, etc.
#----------------------------------------------------------------------------------
# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")

#----------------------------------------------------------------------------------
#       Init block
#       initialize the array of clues for use in the screens
#----------------------------------------------------------------------------------
init python:
    clues_array = []    #array of clues, in this case Strings
        
#----------------------------------------------------------------------------------
#       Screens
#----------------------------------------------------------------------------------
screen clues_button:
    #create button that shows the clues screen when clicked
    textbutton "Review Clues" action Show("clues")
    
screen clues:   
    zorder 1            #make screen appear on top of other layers
    modal True          #prevent user from clicking on other stuff while clues is open
    
    frame:
        yfill True      #expand to fill available vertical space
        xfill False     #don't fill available horizontal space
        xalign 1.0      #align to the right side
        xsize 600       #set to 600px width
        xpadding 10     #set padding
        ypadding 10
        
        hbox:               #title box 
            spacing 10
            text "Clues" size 30
            textbutton "Hide Clues" action Hide("clues")

        viewport:
            mousewheel True
            scrollbars "vertical"

            vbox:               #add vbox to frame
                spacing 10      #10px between each element
                null height 40  #add space under the title
                
                #add items from clues_array
                for i in clues_array:
                        text i      #add items
                        
                        
screen clue_added(clue):
    modal True          #prevent user from clicking on things outside this screen
    frame:
        xalign 0.5      #center in middle of window
        yalign 0.5
        xpadding 10
        ypadding 10
            
        vbox:
            spacing 10
            text clue + " added to inventory!" size 20
            textbutton "Close" action Hide("clue_added")
        
#----------------------------------------------------------------------------------
#       Start game here
#----------------------------------------------------------------------------------

# The game starts here.
label start:
    show screen clues_button
    
    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    e "Oh look, you found some items!"

    $ clues_array.append("Murder Weapon: Unknown. Seems the killer took it with them.")
    $ clues_array.append("Body: Strangely, the victim seems to have not put up a struggle.")
    $ clues_array.append("Cause of Death: Loss of blood, shock.")
    $ clues_array.append("Time of Death: 8:00PM")
    $ clues_array.append("Location: By the flower shop.")
    
    show screen clue_added("Clues")
    
    e "Try opening your inventory!"
    return
