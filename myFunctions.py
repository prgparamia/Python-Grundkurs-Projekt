

# Function Declaration




def myStart():
    print("\n")
    print("**********  START GAME  TREASURE HUNT ********")
    name=input("Enter Your Name:")
    print(name)
    
    return name

print("\n")

def myReply():
  

  userWantsToPlay=False
  while True:
        replyToPlay=input("Reply if you want to play(Y/N):")
        print("\n")
        if replyToPlay =="Y":
            userWantsToPlay=True
            print("Lets start the game: TREASURE HUNT")
            print("\n")
            
            break
        elif replyToPlay=="N" :
            userWantsToPlay=False
            print("\n")
            
            print("You want to leave ,see you later") 
            print("\n")
            
        else:
          print("please try to answer with only Y or N")
          print("\n")

  return userWantsToPlay

print("\n")










    













