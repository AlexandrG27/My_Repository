from tkinter import *
from playsound import playsound

root = Tk()
root.title('TicTacToe')
root.geometry('300x400')
root.resizable(False, False)
root.configure(background='#cc99ff')

f = Frame(root, bg='#cc99ff')
f.place(relwidth=1, relheight=0.8)

lbl_turn = Label(f, text='Player 1 turn', bg='#cc99ff')
lbl_turn.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.1)

lbl_result = Label(root, bg='#cc99ff', font=('Arial', 14, 'bold'))
lbl_result.place(relx=0.1, rely=0.88, relwidth=0.8, relheight=0.1)

def about():
    reset.place_forget()
    undo.place_forget()
    root.geometry('400x250')
    new_frame.pack()
    lbl_about = Label(new_frame, text='By: Alexander Gorabnev' + '\n' + 'August, 2020',
                      font=('Arial', 14, 'bold')).place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3)
    b_back = Button(new_frame, text='Back', bg='#33cc33', command=back).place(relx=0.3, rely=0.7, relwidth=0.4,
                                                                              relheight=0.15)


def back():
    root.geometry('300x400')
    new_frame.pack_forget()
    reset.place(relx=0.35, rely=0.77, relwidth=0.3, relheight=0.1)
    undo.place(relx=0.35, rely=0.65, relwidth=0.3, relheight=0.1)


menuuu = Menu(root)
root.config(menu=menuuu)

new_frame = Frame(root, bg='#4d88ff', width=400, height=400)

m = Menu(menuuu, tearoff=0)
menuuu.add_cascade(label='File', menu=m)
m.add_command(label='About', command=about)
m.add_separator()
m.add_command(label='Back', command=back)
m.add_separator()
m.add_command(label='Exit', command=root.quit)

total_turns = 0

clicked_buttons = []


def CheckWin():
    win = False
    if b1['text'] == b2['text'] == b3['text'] != ' ' \
            or b4['text'] == b5['text'] == b6['text'] != ' ' \
            or b7['text'] == b8['text'] == b9['text'] != ' ' \
            or b1['text'] == b4['text'] == b7['text'] != ' ' \
            or b2['text'] == b5['text'] == b8['text'] != ' ' \
            or b3['text'] == b6['text'] == b9['text'] != ' ' \
            or b1['text'] == b5['text'] == b9['text'] != ' ' \
            or b3['text'] == b5['text'] == b7['text'] != ' ':
        win = True
    return win


def CheckDraw():
    draw = False
    if total_turns == 9 and not CheckWin():
        draw = True
    return draw


def add_sign(n):
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    global total_turns
    global clicked_buttons

    clicked_buttons.append(n)
    if total_turns % 2 == 0:
        lbl_turn['text'] = 'Player 2 turn'
        n['font'] = 18
        n['text'] = 'X'
        n['state'] = 'disabled'
    elif total_turns % 2 == 1:
        lbl_turn['text'] = 'Player 1 turn'
        n['font'] = 18
        n['text'] = '0'
        n['state'] = 'disabled'
    if CheckWin():
        undo['state'] = 'disabled'
        if b1['text'] == b2['text'] == b3['text'] != ' ':
            b1['bg'] = 'red'
            b2['bg'] = 'red'
            b3['bg'] = 'red'
        elif b4['text'] == b5['text'] == b6['text'] != ' ':
            b4['bg'] = 'red'
            b5['bg'] = 'red'
            b6['bg'] = 'red'
        elif b7['text'] == b8['text'] == b9['text'] != ' ':
            b7['bg'] = 'red'
            b8['bg'] = 'red'
            b9['bg'] = 'red'
        elif b1['text'] == b4['text'] == b7['text'] != ' ':
            b1['bg'] = 'red'
            b4['bg'] = 'red'
            b7['bg'] = 'red'
        elif b2['text'] == b5['text'] == b8['text'] != ' ':
            b2['bg'] = 'red'
            b5['bg'] = 'red'
            b8['bg'] = 'red'
        elif b3['text'] == b6['text'] == b9['text'] != ' ':
            b3['bg'] = 'red'
            b6['bg'] = 'red'
            b9['bg'] = 'red'
        elif b1['text'] == b5['text'] == b9['text'] != ' ':
            b1['bg'] = 'red'
            b5['bg'] = 'red'
            b9['bg'] = 'red'
        elif b3['text'] == b5['text'] == b7['text'] != ' ':
            b3['bg'] = 'red'
            b5['bg'] = 'red'
            b7['bg'] = 'red'

        for b in buttons:
            b['state'] = 'disabled'

        if total_turns % 2 == 0:
            lbl_result['text'] = 'Game over. X wins'
        elif total_turns % 2 == 1:
            lbl_result['text'] = 'Game over. 0 wins'
        lbl_turn['text'] = ''
        playsound('win_sound.mp3', False)

    total_turns += 1

    if CheckDraw():
        undo['state'] = 'disabled'
        lbl_result['text'] = 'Draw'

        for b in buttons:
            b['state'] = 'disabled'

        lbl_turn['text'] = ''


def Reset():
    global total_turns
    total_turns = 0
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    for b in buttons:
        b['text'] = ' '
        b['state'] = 'normal'
        b['bg'] = '#ffffffffffff'


    lbl_turn['text'] = ''
    lbl_result['text'] = ''

    lbl_turn['text'] = 'Player 1 turn'
    if undo['state'] == 'disabled':
        undo['state'] = 'normal'


def Undo():
    global total_turns
    if total_turns > 0:
        clicked_buttons[-1]['text'] = ' '
        clicked_buttons[-1]['state'] = 'normal'
        if lbl_turn['text'] == 'Player 1 turn':
            lbl_turn['text'] = 'Player 2 turn'
        elif lbl_turn['text'] == 'Player 2 turn':
            lbl_turn['text'] = 'Player 1 turn'
        clicked_buttons.pop()
        total_turns -= 1


b1 = Button(f, text=' ', relief=GROOVE, bd=2, padx=46, pady=30, command=lambda: add_sign(b1))
b2 = Button(f, text=' ', relief=GROOVE, bd=2, padx=46, pady=30, command=lambda: add_sign(b2))
b3 = Button(f, text=' ', relief=GROOVE, bd=2, padx=46, pady=30, command=lambda: add_sign(b3))
b4 = Button(f, text=' ', relief=GROOVE, bd=2, padx=46, pady=30, command=lambda: add_sign(b4))
b5 = Button(f, text=' ', relief=GROOVE, bd=2, padx=46, pady=30, command=lambda: add_sign(b5))
b6 = Button(f, text=' ', relief=GROOVE, bd=2, padx=46, pady=30, command=lambda: add_sign(b6))
b7 = Button(f, text=' ', relief=GROOVE, bd=2, padx=46, pady=30, command=lambda: add_sign(b7))
b8 = Button(f, text=' ', relief=GROOVE, bd=2, padx=46, pady=30, command=lambda: add_sign(b8))
b9 = Button(f, text=' ', relief=GROOVE, bd=2, padx=46, pady=30, command=lambda: add_sign(b9))

b1.place(relx=0.1, rely=0.1, relwidth=0.266, relheight=0.2)
b2.place(relx=0.366, rely=0.1, relwidth=0.266, relheight=0.2)
b3.place(relx=0.632, rely=0.1, relwidth=0.266, relheight=0.2)
b4.place(relx=0.1, rely=0.3, relwidth=0.266, relheight=0.2)
b5.place(relx=0.366, rely=0.3, relwidth=0.266, relheight=0.2)
b6.place(relx=0.632, rely=0.3, relwidth=0.266, relheight=0.2)
b7.place(relx=0.1, rely=0.5, relwidth=0.266, relheight=0.2)
b8.place(relx=0.366, rely=0.5, relwidth=0.266, relheight=0.2)
b9.place(relx=0.632, rely=0.5, relwidth=0.266, relheight=0.2)

undo = Button(root, text='UNDO', bg='#ff8533', command=Undo)
undo.place(relx=0.35, rely=0.65, relwidth=0.3, relheight=0.1)

reset = Button(root, text='RESET', bg='#ff5500', command=Reset)
reset.place(relx=0.35, rely=0.77, relwidth=0.3, relheight=0.1)

root.mainloop()
