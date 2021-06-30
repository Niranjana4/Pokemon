from tkinter import*
from PIL import ImageTk,Image
import random

root=Tk()
root.title("ENDLESS POKEMON GAME")
root.geometry("600x400")
root.configure(background="purple")

Img=ImageTk.PhotoImage(Image.open("Pokemon_Trading_Card_Game_cardback.jpg"))

player1=Label(root,text="Player 1",bg="black",fg="purple")
player1.place(relx=0.2,rely=0.3,anchor=CENTER)

player2=Label(root,text="Player 2",bg="black",fg="purple")
player2.place(relx=0.8,rely=0.3,anchor=CENTER)

play1sc=Label(root,bg="white",fg="lavender")
play1sc.place(relx=0.2,rely=0.4,anchor=CENTER)

play2sc=Label(root,bg="white",fg="lavender")
play2sc.place(relx=0.8,rely=0.4,anchor=CENTER)

random_dice=Label(root,bg="black",fg="pink")
random_dice.place(relx=0.5,rely=0.5,anchor=CENTER)

player1_sc=0
def player1():
    global player1_sc
    ran_player=random.randint(1,6)
    random_dice["text"]="Player 1 dice random number"+str(ran_player)
    player1_sc=player1_sc+ran_player
    play1sc["text"]="Score"+str(player1_sc)
    
    player2_sc=0
def player2():
    global player2_sc
    ran_player1=random.randint(1,6)
    random_dice["text"]="Player 2 dice random number"+str(ran_player1)
    player2_sc=player1_sc+ran_player
    play2sc["text"]="Score"+str(player2_sc)
    
btn_player1=Button(root,image=Img,command=player1)
btn_player1.place(relx=0.5,rely=0.5,anchor=CENTER)

btn_player2=Button(root,image=Img,command=player2)
btn_player2.place(relx=0.8,rely=0.5,anchor=CENTER)
root.mainloop()



root.mainloop()