import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
from functools import partial

class tictactoe:

    def __init__(self):
        self.t = tk.Tk()
        self.t.title("TIC TAC TOE")

        # Set desired window size
        window_width=700
        window_height=600
        # Get the screen dimensions
        screen_width=self.t.winfo_screenwidth()
        screen_height=self.t.winfo_screenheight()
        # Calculate x and y coordinates to center the window
        center_x=int((screen_width-window_width) / 2)
        center_y=int((screen_height-window_height) / 2)
        # Set the geometry and position
        self.t.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        self.t.resizable(False,False)

        self.label1 = tk.Label(self.t,text="TIC TAC TOE", fg="#c71585", bg="LightBlue2", width=300, height=5,
                               highlightbackground="#c71585", highlightthickness=15)
        self.label1.config(font=("Arial", 30, "bold"))
        self.label1.pack()

        #Scoreboard
        self.score_x=0
        self.score_o=0
        self.score_draw=0

        self.scoreboard_label=tk.Label(self.t, text=self.get_score_text(),font=("Arial", 16, "bold"),
                                       fg="#c71585", bg="LightBlue2", width=40, height=4,relief="solid", bd=3)

        #Dropdown Menu for Starting Player
        self.option_frame=tk.Frame(self.t, bg="LightBlue2")
        self.option_frame.pack(pady=25)

        self.starting_player_label=tk.Label(self.option_frame, text="Choose Starting Player: ", font=("Arial", 15, "bold"),
                                              width=20, height=6,bg="LightBlue2", fg="#c71585")
        self.starting_player_label.pack(side="left")

        self.starting_player=StringVar(value="Random")
        self.starting_player_menu=OptionMenu(self.option_frame, self.starting_player, "Random", "Player X","Player O")
        self.starting_player_menu.config(width=15,height=2,font=("Arial", 12,"bold"), bg="LightBlue2", fg="#c71585")
        self.starting_player_menu.pack(side="right", padx=5)

        #Start button
        self.button1=Button(self.t, text="CLICK HERE TO START", activeforeground="#c71585", activebackground="SkyBlue", fg="#c71585",
                              bg="LightBlue2", width=35, height=3,font=("Arial", 14, "bold"), command=self.new_game)
        self.button1.pack(pady=10)

        self.players=["X","O"]
        self.buttons=[]
        self.frame_=tk.Frame(self.t,highlightbackground="maroon2", highlightthickness=4)
        self.frame_.pack(pady=10)

    def new_game(self):
        if not self.scoreboard_label:
            self.scoreboard_label.pack(pady=5)
        else:
            self.update_scoreboard()
            self.scoreboard_label.pack(pady=5)

        selected_player=self.starting_player.get()
        if selected_player=="Player X":
            self.player_turn ="X"
        elif selected_player=="Player O":
            self.player_turn="O"
        else:
            self.player_turn=random.choice(self.players)

        self.frame_.destroy()
        self.frame_=tk.Frame(self.t)
        self.frame_.pack(pady=10)
        self.label1.pack_forget()
        self.option_frame.pack_forget()
        self.button1.pack_forget()

        self.label2=tk.Label(self.t,text=f"{self.player_turn}'s turn",
                             highlightbackground="#c71585", highlightthickness=14,fg="#c71585", bg="LightBlue2", width=400, height=3)
        self.label2.config(font=("Arial", 20, "bold"))
        self.label2.pack(pady=(4,2))
        self.frame=tk.Frame(self.t)
        self.frame.pack(pady=(2,4))

        self.buttons=[]
        for r in range(3):
            row=[]
            for c in range(3):
                button=tk.Button(self.frame,width=5,height=2,font=("Arial",20,"bold"),activeforeground="LightBlue2",
                                 activebackground="#009acd",fg="#c71585",bg="LightBlue2",command=partial(self.turn,r,c))
                button.grid(row=r,column=c,padx=6, pady=6)
                row.append(button)
            self.buttons.append(row)

    def turn(self,r,c):
        if self.buttons[r][c]['text'] =="":
            self.label2['text'] = f"Player {self.player_turn}'s turn"
            self.buttons[r][c]['text']=self.player_turn

            if self.winner():
                self.label2['text']=f"Player {self.player_turn} wins! "
                messagebox.showinfo("Game Over",f"Player {self.player_turn} Wins! ")
                if self.player_turn == "X":
                    self.score_x += 1
                else:
                    self.score_o += 1

                self.update_scoreboard()
                self.game_end()

            elif self.draw():
                self.label2['text']= "Its a Draw!"
                messagebox.showinfo("Game Over","Its a Draw! ")
                self.score_draw += 1
                self.update_scoreboard()
                self.game_end()

            else:
                self.player_switch()
                self.label2['text']=f"Player {self.player_turn}'s turn"

    def player_switch(self):
        self.player_turn="O" if self.player_turn=="X" else "X"

    def winner(self):
        if self.buttons[0][0]['text']==self.buttons[0][1]['text']==self.buttons[0][2]['text'] !="":
            return True
        if self.buttons[1][0]['text']==self.buttons[1][1]['text']==self.buttons[1][2]['text'] !="":
            return True
        if self.buttons[2][0]['text'] == self.buttons[2][1]['text'] == self.buttons[2][2]['text']!="":
            return True

        if self.buttons[0][0]['text'] == self.buttons[1][0]['text'] == self.buttons[2][0]['text']!="":
            return True
        if self.buttons[0][1]['text'] == self.buttons[1][1]['text'] == self.buttons[2][1]['text']!="":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][2]['text'] == self.buttons[2][2]['text']!="":
            return True

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text']!="":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text']!="":
            return True

        return False

    def draw(self):
        for row in self.buttons:
            for button in row:
                if button['text']=="":
                    return False
        return True

    def get_score_text(self):
        return f"SCOREBOARD:\n-------------------------------\nPlayer X: {self.score_x} | Player O: {self.score_o} | Draw(s): {self.score_draw}"

    def update_scoreboard(self):
        self.scoreboard_label.config(text=self.get_score_text())

    def game_end(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

        self.frame_.destroy()
        self.frame_=tk.Frame(self.t)
        self.frame_.pack(pady=10)

        restart_button=Button(self.frame_,text="PLAY AGAIN GAME", width=25, height=5, font=("Arial", 10, "bold"),activeforeground="#FFC0CB",
                                   activebackground="#009acd",fg="#c71585", bg="LightBlue2", command=self.play_again_game)
        restart_button.pack(side="left", padx=10)

        quit_button=Button(self.frame_,text="QUIT GAME", width=25, height=5, font=("Arial", 10, "bold"),activeforeground="#FFC0CB",
                                activebackground="#009acd", fg="#c71585", bg="LightBlue2", command=self.quit_game)
        quit_button.pack(side="right", padx=10)

        self.label2.pack_forget()

    def play_again_game(self):
        self.frame.destroy()
        self.label2.destroy()
        self.frame_.pack_forget()
        self.new_game()

    def quit_game(self):
        messagebox.showinfo("Quit Game","Thank you for playing! ")
        self.t.destroy()

    def run_game(self):
        self.t.mainloop()

game=tictactoe()
game.run_game()



