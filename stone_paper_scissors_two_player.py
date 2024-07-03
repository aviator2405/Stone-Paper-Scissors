from tkinter import *
import winsound
import time

player1 = None
player2 = None


def compare():
    global player2, player1
    print(f'player1-{player1}')
    print(f'player2-{player2}')

    if player1 is None or player2 is None:
        print('hello')
        return

    if player1 == 'stone':
        if player2 == "stone":
            l1.config(text='RESULT- DRAW', font='jokerman 20 bold', fg='RED', bg='yellow')
        elif player2 == 'paper':
            l1.config(text="RESULT- PLAYER 2 WINS", font='jokerman 20 bold', fg='red', bg='yellow')
        else:
            l1.config(text='RESULT- PLAYER 1 WINS', font='jokerman 20 bold', fg='RED', bg='yellow')

    elif player1 == 'paper':
        if player2 == "stone":
            l1.config(text='RESULT- PLAYER 1 WINS', font='jokerman 20 bold', fg='RED', bg='yellow')
        elif player2 == 'paper':
            l1.config(text="RESULT- DRAW", font='jokerman 20 bold', fg='red', bg='yellow')
        else:
            l1.config(text='RESULT- PLAYER 2 WINS', font='jokerman 20 bold', fg='RED', bg='yellow')

    elif player1 == 'scisssors':
        if player2 == "stone":
            l1.config(text='RESULT- PLAYER 2 WINS', font='jokerman 20 bold', fg='RED', bg='yellow')
        elif player2 == 'paper':
            l1.config(text="RESULT- PLAYER 1 WINS", font='jokerman 20 bold', fg='red', bg='yellow')
        else:
            l1.config(text='RESULT- DRAW', font='jokerman 20 bold', fg='RED', bg='yellow')
    i = 10
    scissorsl1.config(state=DISABLED)
    paperl1.config(state=DISABLED)
    stonel1.config(state=DISABLED)
    stonel2.config(state=DISABLED)
    paperl2.config(state=DISABLED)
    scissorsl2.config(state=DISABLED)
    while i >= 0:
        timelabel.update()
        winsound.Beep(600, 200)
        winsound.Beep(600, 200)
        print(i)
        timelabel.config(text=f'TIME REMAINING- {i} SEC', font='Helvetica 11 bold')
        time.sleep(0.8)
        i -= 1
    timelabel.config(text=f'')
    scissorsl1.config(state=NORMAL)
    paperl1.config(state=NORMAL)
    stonel1.config(state=NORMAL)
    # stonel2.config(state=NORMAL)
    # paperl2.config(state=NORMAL)
    # scissorsl2.config(state=NORMAL)
    l1.config(text='PLAYER 1 TURN')
    player1, player2 = None, None
    print(player1)
    print(player2)


# FUNCTIONS FOR PLAYER 1 CHOICES
def stone1(useless):
    print(useless)
    winsound.Beep(400, 200)
    global player1
    player1 = 'stone'
    l1.config(text='PLAYER 2 TURN')
    stonel2.config(state=NORMAL)
    paperl2.config(state=NORMAL)
    scissorsl2.config(state=NORMAL)
    scissorsl1.config(state=DISABLED)
    paperl1.config(state=DISABLED)
    stonel1.config(state=DISABLED)
    compare()


def paper1(useless):
    print(useless)
    winsound.Beep(400, 200)
    global player1
    player1 = 'paper'
    l1.config(text='PLAYER 2 TURN')
    stonel2.config(state=NORMAL)
    paperl2.config(state=NORMAL)
    scissorsl2.config(state=NORMAL)
    scissorsl1.config(state=DISABLED)
    paperl1.config(state=DISABLED)
    stonel1.config(state=DISABLED)
    compare()


def scissors1(useless):
    print(useless)
    winsound.Beep(400, 200)
    global player1
    player1 = 'scissors'
    l1.config(text='PLAYER 2 TURN')
    stonel2.config(state=NORMAL)
    paperl2.config(state=NORMAL)
    scissorsl2.config(state=NORMAL)
    scissorsl1.config(state=DISABLED)
    paperl1.config(state=DISABLED)
    stonel1.config(state=DISABLED)
    compare()


# FUNCTIONS FOR PLAYER 1 CHOICES
def stone2(useless):
    print(useless)
    winsound.Beep(400, 200)
    global player2
    player2 = 'stone'
    l1.config(text='PLAYER 2 TURN')
    compare()


def paper2(useless):
    print(useless)
    winsound.Beep(400, 200)
    global player2
    player2 = 'paper'
    l1.config(text='PLAYER 2 TURN')
    compare()


def scissors2(useless):
    print(useless)
    winsound.Beep(400, 200)
    global player2
    player2 = 'scissors'
    l1.config(text='PLAYER 2 TURN')
    compare()


# main root obj for tkinter.Tk() class
root = Tk()
root.title('STONE PAPER SCISSORS')
root.geometry('650x414')
# root.state('zoomed')
root.maxsize(width=650, height=414)

Label(text="WELCOME TO STONE PAPER SCISSORS", font="algerian 20 bold italic underline", background='red').pack(fill=X)

# PLAYER 1 FRAME
p1f = Frame(root, bg='red', borderwidth=2, relief=RIDGE)
p1f.pack(fill='x', side=LEFT, anchor=N, ipadx=10, ipady=19)

# label with clicking events
stphoto1 = PhotoImage(file='stoner.png')
stonel1 = Label(p1f, image=stphoto1, borderwidth=6, relief=RAISED)
stonel1.pack()

paphoto1 = PhotoImage(file='paperr.png')
paperl1 = Label(p1f, image=paphoto1, borderwidth=6, relief=RAISED)
paperl1.pack()

scphoto1 = PhotoImage(file='sciccorsr.png')
scissorsl1 = Label(p1f, image=scphoto1, borderwidth=6, relief=RAISED)
scissorsl1.pack()

scissorsl1.bind('<Button-1>', scissors1)
paperl1.bind('<Button-1>', paper1)
stonel1.bind('<Button-1>', stone1)

Label(p1f, text="PLAYER 1", font='arial 15 bold', background='red').pack()

# PLAYER 2 FRAME
p2f = Frame(root, bg='red', borderwidth=2, relief=RIDGE)
p2f.pack(fill=X, side=RIGHT, anchor=N, ipadx=10, ipady=19)

# label with clicking events
stphoto2 = PhotoImage(file='stoner.png')
stonel2 = Label(p2f, image=stphoto2, borderwidth=6, relief=RAISED)
stonel2.pack()

paphoto2 = PhotoImage(file='paperr.png')
paperl2 = Label(p2f, image=paphoto2, borderwidth=6, relief=RAISED)
paperl2.pack()

scphoto2 = PhotoImage(file='sciccorsr.png')
scissorsl2 = Label(p2f, image=scphoto2, borderwidth=6, relief=RAISED)
scissorsl2.pack()

Label(p2f, text="PLAYER 2", font='arial 15 bold', background='red').pack()

scissorsl2.bind('<Button-1>', scissors2)
paperl2.bind('<Button-1>', paper2)
stonel2.bind('<Button-1>', stone2)

stonel2.config(state=DISABLED)
paperl2.config(state=DISABLED)
scissorsl2.config(state=DISABLED)

# Button(text='STONE', command=stone).pack()
# Button(text='PAPER', command=paper).pack()
# Button(text='SCISSORS', command=scissors).pack()
footer = Frame(root, bg='red', borderwidth=2, relief=RIDGE)
footer.pack(side=TOP, fill=X)
l1 = Label(footer, text='PLAYER 1 TURN', font='jokerman 20 bold', bg='yellow', borderwidth=6, relief=GROOVE)
l1.pack()

photo = PhotoImage(file="ssp.png")
l2 = Label(footer, image=photo, borderwidth=6, relief=RIDGE)
l2.pack()

timelabel = Label(footer, text='', bg='red')
timelabel.pack()

root.mainloop()
