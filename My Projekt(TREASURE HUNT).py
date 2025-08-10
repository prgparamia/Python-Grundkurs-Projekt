# Module import von MyFunctios

import myFunctions           
import time
import json
import tkinter as tk

import myFirstlevel as mfl
import mySecondlevel as msl
import myThirdlevel as mtl



# Function Aufruf von Module myFunctios
name=myFunctions.myStart()
print("\n")

# Function Aufruf
userWantsToPlay=myFunctions.myReply()
print("\n")
# Sleep Time für Code ,while das Spiel Fenster nimmt 10 sekunden zeit zu öffnen

def mySleep():

   time.sleep(5)
                                
   for i in range(10, 0, -1):
           time.sleep(1)
           print(i)
mySleep()


    
def mySetterLevel():    
    level=1
    myTrials=0
    if userWantsToPlay: 
        # f string 
        print(f"Hello!! {name}:) you are in ***Level 1***")
        print("To go to Level 2 ,You must find the Treasure in less than  20 trials")
        print("\n")

        # neues objekt erstellen und in einen container speichern
        S=mfl.TreasureHunt 
        #  verwenden der methoden auf Instanzen
        S.create_widgets
        S.update_score
        S.check_treasure
        S.disable_all_buttons
        # Führen Sie den Class code aus
        if __name__ == "__main__":
            root = tk.Tk()
            app =mfl. TreasureHunt(root)
            root.mainloop()
            print("My level is:  ",level)
            print("\n")
            print("My score in level 1 is : ",app.score) 
            
            breakpoint
        else:
            print(f"Hey {name} 😢You can not go to level2  with more than 20 attempts")
            breakpoint
        
        
        
    

    try:  
        
        if app.score<=20:   # Den Punktwert aus dem  erstes Spielfenster übernehmen   
            
    
            print(f"Congratulations!! {name }😊 You are ready for level 2")
            print("Tresure Hunt  Level 2 Starts ...")
            mySleep()
            print("To go to level3, You must collect 100 points")

            level=level+1
            print("My level is:" ,level)
            print("\n")

            # Class Aufruf
    
            r=msl.TreasureHuntGame
            #  verwenden der methoden auf Instanzen

            r.place_treasures
            r.draw_grid
            r.draw_player
            r.move_player
            r.check_for_treasure
            r.give_clue
            r.distance
        
            if __name__ == "__main__":
                root = tk.Tk()
                game = msl.TreasureHuntGame(root)
                root.mainloop()
                print("My score  in level 2 is: ",game.score)
            print("\n")
            breakpoint
        else :
            print(f"  Hey {name} 😢You can not play further as your score is: {app.score} more than 20")
            print("\n")
            print("*****PLEASE EXIT*****")
            print("\n")
            breakpoint
    except Exception as e:
        print(e)
        
    try:
        
        if game.score >=100:     # Den Punktwert aus dem  zweites Spielfenster übernehmen   
 
            print(f"Congratulations!! {name} 😊You are ready for level 3")
            print("Tresure Hunt  Level 3 Starts ...")

            mySleep()
            
            print("To Win the game ,You must find all the Treasure ")
            print("\n")
            level=level+1
            print("My level is:" ,level)
            print("\n")
            t=mtl.TreasureHuntHarder
            t.create_grid
            t.place_items
            t.click_cell
            t.disable_all_buttons
            t.reveal_all
          # Führen Sie den Class code aus
            if __name__ == "__main__":
                root = tk.Tk()
                game1 =mtl. TreasureHuntHarder(root)
                root.mainloop()
            
            breakpoint
                
        else:
            print(f"Sorry  {name}😢 you can not go to level 3 with score less than 100 ")  

            print("\n")  
            breakpoint

    except Exception as e:
        print(e)


    try:
       if game1.treasures_found==3: # Den Punktwert aus dem  drietes Spielfenster übernehmen   
        print(f"CONGRATULATIONS !!  {name}😊 YOU ARE THE WINNER")
        print("\n")

       else:
        print(f"SORRY!! {name}😢    YOU LOST THE GAME! BETTER LUCK NEXT TIME")
        print("\n")  
        breakpoint
    
 
    except Exception as e:
        print(e)
    print("*" *130)
    # Funktion Decorator mit wrapper

    def decoErrorHandler(func):
       def wrapper(): 
        
           try:
               func()
               print("Completed all three Levels")
            
           except Exception as e:
               print(f"!ERROR => '{func.__name__}' => {e}")
            
                            # => In Produktivumgebungen sind auch eigen Error Code Mappings denkbar und praktikabel
       return wrapper

    @decoErrorHandler
    def myScoreBoard():
        # Erstellung von einem Dictionary mit allen Levels und scores
             
        myScoreDict={"Name":name,"Level1":f"{app.score}  Attempts","level2":f"{game.score} points","Level3":f"{game1.treasures_found} tresures found"}
        myScoreFile="myScoreDict.json"

        # erstellung einer json Datei

        file = open(myScoreFile, "w")
        json.dump(myScoreDict, file)

        with open(myScoreFile,"w") as f :
          json.dump(myScoreDict,f)

        gameScore={}
        with open(myScoreFile,"r") as f:
          gameScore=json.load(f)
        print(f"Score Board: {gameScore}")
        print("\n")

    myScoreBoard()
    print("*"*130)
    
mySetterLevel()
print(f"Game over!.....See you Next Time!......")







