import tkinter as tk
import random
import tkinter.messagebox

#初期盤面の情報
field = [
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,99,99,99,99,99,99,99,99,99,99,99]
]

#テトリミノの情報
mino = [
    [#O
        [
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ]
    ],
    [#I
        [
            [0,0,0,0],
            [1,1,1,1],
            [0,0,0,0],
            [0,0,0,0]
        ],
        [
            [0,1,0,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,1,0,0]
        ],
        [
            [0,0,0,0],
            [1,1,1,1],
            [0,0,0,0],
            [0,0,0,0]
        ],
        [
            [0,1,0,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,1,0,0]
        ]
    ],
    [#L
        [
            [0,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [0,1,1,1],
            [0,1,0,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,0]
        ],
        [
            [0,0,0,0],
            [0,0,1,0],
            [1,1,1,0],
            [0,0,0,0]
        ]
    ],
    [#J
        [
            [0,0,1,0],
            [0,0,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [0,1,0,0],
            [0,1,1,1],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [0,1,1,0],
            [0,1,0,0],
            [0,1,0,0]
        ],
        [
            [0,0,0,0],
            [1,1,1,0],
            [0,0,1,0],
            [0,0,0,0]
        ]
    ],
    [#S
        [
            [0,0,0,0],
            [0,1,1,0],
            [1,1,0,0],
            [0,0,0,0]
        ],
        [
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [0,1,1,0],
            [1,1,0,0],
            [0,0,0,0]
        ],
        [
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,0,0]
        ]
    ],
    [#Z
        [
            [0,0,0,0],
            [1,1,0,0],
            [0,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,0,1,0],
            [0,1,1,0],
            [0,1,0,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [1,1,0,0],
            [0,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,0,1,0],
            [0,1,1,0],
            [0,1,0,0],
            [0,0,0,0]
        ]
    ],
    [#凸
        [
            [0,1,0,0],
            [1,1,1,0],
            [0,0,0,0],
            [0,0,0,0]
        ],
        [
            [0,1,0,0],
            [0,1,1,0],
            [0,1,0,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [0,0,0,0]
        ],
        [
            [0,1,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,0,0,0]
        ]
    ],
]

dx = 0
dy = 0
fallcount = 0
spin = 0

#ボタンをクリックしたときの処理の関数
def game_start():
    global key,i
    fieldreset()
    i = random.randint(0,6)
    createMino()
    blockMoves()    
    
#初期盤面の描画
def fieldreset():
    fieldInit = [
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,99,99,99,99,99,99,99,99,99,99,99],
    [99,99,99,99,99,99,99,99,99,99,99,99],
    [99,99,99,99,99,99,99,99,99,99,99,99]
]
    canvas.delete("wall")
    canvas.delete("emp")
    for y in range(22):
        for x in range(12):
            field[y][x] = fieldInit[y][x]
            if field[y][x] == 99:
                canvas.create_rectangle(x*20,y*20,x*20+20,y*20+20,fill='gray',outline='white',tag="wall")
            if field[y][x] == 0:
                canvas.create_rectangle(x*20,y*20,x*20+20,y*20+20,fill='white',outline='black',tag="emp")

#盤面の更新
def fieldupdate():
    canvas.delete("block")
    canvas.delete("emp")
    for y in range(0,21,1):
        for x in range(1,11,1):
            if field[y][x] == 1 or field[y][x] == 2:
                canvas.create_rectangle(x*20,y*20,x*20+20,y*20+20,fill='red',outline='white',tag="block")
            if field[y][x] == 0:
                canvas.create_rectangle(x*20,y*20,x*20+20,y*20+20,fill='white',outline='black',tag="emp")

#ライン消去
def deleteLine():
    for y in range(21):
        if field[y] == [99,2,2,2,2,2,2,2,2,2,2,99]:
            field.remove(field[y])
            field.insert(0,[99,0,0,0,0,0,0,0,0,0,0,99])


#テトリミノの生成
def createMino():
    global dx,dy,i
    canvas.delete("block")
    dx = 4
    for y in range(4):
        for x in range(4):
            if mino[i][spin][y][x] == 1 and field[dy+y][dx+x] == 2:
                tkinter.messagebox.showinfo("GAME OVER","GAME OVER です")
                quit(blockMoves)
                break
            if mino[i][spin][y][x] == 1 and field[dy+y][dx+x] == 0:
                canvas.create_rectangle(dx*20,dy*20,dx*20+20,dy*20+20,fill='red',outline='white',tag="block")
                field[dy+y][dx+x] = 1
            
            
#ミノの操作
key = ""
def key_down(e):
    global key
    key = e.keysym 
    #print("KEY:" + str(key))
def key_up(e):
    global key
    key = ""


#移動と回転
def blockMove():
    global key,dx,dy,spin,i
    
    canmoveright=True
    canmoveleft=True
    #Right
    for x in range(10,0,-1):
            for y in range(20,-1,-1):
                if field[y][x] == 1 and field[y][x+1] ==2:
                    canmoveright=False
                if field[y][x] == 1 and field[y][x+1] ==99:
                    canmoveright=False
    #Left
    for x in range(1,11,1):
            for y in range(20,-1,-1): 
                if field[y][x] == 1 and field[y][x-1] == 2:
                    canmoveleft=False
                if field[y][x] == 1 and field[y][x-1] == 99:
                    canmoveleft=False
    #print(dx,dy)
   
    canspin = True
    if key == "Up": #回転
        spin = spin +1 
        if spin == 4:
            spin = 0
        #print(spin)
        for y in range(4):
            for x in range(4):
                if mino[i][spin][y][x] == 1 and field[dy+y][dx+x] ==99:
                    canspin =False
                    spin = spin-1
                    break
                if mino[i][spin][y][x] == 1 and field[dy+y][dx+x] ==2:
                    canspin =False
                    spin = spin-1
                    break
        if canspin ==True:
            for y in range(4):
                for x in range(4):
                    if mino[i][spin][y][x] == 1 and field[dy+y][dx+x]!=99 and field[dy+y][dx+x]!=2:
                        field[dy+y][dx+x] = 1
                        #print(dx,dy)
                    if mino[i][spin][y][x] == 0 and field[dy+y][dx+x]!=99 and field[dy+y][dx+x]!=2:
                        field[dy+y][dx+x] = 0
        #print(field)

    if canmoveright:
        if key == "Right" :
            dx=dx+1
            for x in range(10,0,-1):
                for y in range(20,-1,-1):
                    if field[y][x] == 1 and field[y][x+1] == 0:
                        field[y][x] = 0
                        field[y][x+1] = 1
                    if field[y][x] == 1 and field[y][x+1] != 0:
                        dx=dx-1
                        return
    if canmoveleft:
        if key == "Left" :
            dx=dx-1
            for x in range(1,11,1):
                for y in range(20,-1,-1): 
                    if field[y][x] == 1 and field[y][x-1] == 0:
                        field[y][x] = 0
                        field[y][x-1] = 1
                    if field[y][x] == 1 and field[y][x-1] != 0:
                        dx=dx+1
                        return
    if key == "Down" :
        dy=dy+1
        for y in range(20,-1,-1):
            for x in range(1,11,1):
                if field[y][x] == 1 and field[y+1][x] == 0:
                    field[y][x] = 0
                    field[y+1][x] = 1
                if field[y][x] == 1 and field[y+1][x] != 0:
                    
                    for x in range(1,11,1):
                        if field[y+1][x] ==1:
                            field[y+1][x] = 0
                            field[y][x] = 1
                        if y !=20:
                            if field[y+2][x] == 1:
                                field[y+2][x] = 0
                                field[y+1][x] = 1
                        if y !=19 and y!=20:
                            if field[y+3][x] == 1:
                                field[y+3][x] = 0
                                field[y+2][x] = 1
                    
                    for y in range(20,-1,-1):
                        for x in range(1,11,1):
                            if field[y][x] == 1:
                                field[y][x] = 2
                                dx=4
                                dy=0
                                spin=0
                    deleteLine()
                    i=random.randint(0,6)
                    createMino()
                    return
        

def blockMoves():
    global key, fallcount,dx,dy
    fallcount = fallcount+1
    freeFall()
    blockMove()
    fieldupdate()
    win.after(60,blockMoves)

def freeFall():
    global fallcount,key
    if fallcount >=10:
        fallcount =0
        key ="Down"
        blockMove()
        fieldupdate()
        key = ""


#画面作成
win = tk.Tk()
win.geometry('400x500')
win.title('テトリスゲーム')
win.bind("<KeyPress>",key_down)
win.bind("<KeyRelease>",key_up)

#キャンバスの作成
canvas = tk.Canvas(win,height=440,width=240)
#ボタンの作成
btn=tk.Button(win, text='start / restart',command=game_start)

#ガジェットの配置
canvas.place(x=80,y=50)
btn.pack()

fieldreset()

win.mainloop()