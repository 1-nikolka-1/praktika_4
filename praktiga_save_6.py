from tkinter import *
from tkinter import ttk
from time import time
from math import sin, tan, cos
import traceback


# Выбор пороговой частоты
def timee():
    try:
        global step
        step = int(ent_time.get())
    except:
        print('Введите число')


# Выбор скорости изменения
def speed():
    global speed_var
    global r
    global a
    r = (time() - a)*(-float(ent_time2.get())+speed_var)+r
    speed_var = float(ent_time2.get())


# Функции
def f1(x):
    return sin(x)+sin(2*x)

def f2(x):
    return sin(x)**3

def f3(x):
    return sin(x)+0.1*sin(10*x)+13

def f4(x):
    return round(sin(x)*10)

def f5(x):
    return round(sin(x)*10)+sin((x+0.5)*10)

def f6(x):
    return sin(x)+0.2*tan(0.99*x)+10*sin(2*x)

def f7(x):
    return -1**(round(sin(x)*10))+sin(x*2)*10+15

def f8(x):
    return sin(x)*cos(2*x)+525


# Выбор функции
def selected(event):
    global f
    selection = combobox.get()
    if selection == 'sin(c)+sin(2*c)':
        f = 'f1'
    elif selection == 'sin(c)**3':
        f = 'f2'
    elif selection == 'sin(x)+0.1*sin(10*x)+13':
        f = 'f3'
    elif selection == 'round(sin(x)*10)':
        f = 'f4'
    elif selection == 'round(sin(x)*10)+sin((x+0.5)*10)':
        f = 'f5'
    elif selection == 'sin(x)+0.2*tan(0.99*x)+10*sin(2*x)':
        f = 'f6'
    elif selection == '-1**(round(sin(x)*10))+sin(x*2)*10+15':
        f = 'f7'
    elif selection == 'sin(x)*cos(2*x)+525':
        f = 'f8'

# Получение значения для вывода    
def upd():
    global a          # начальное время
    global number     # итерация от 1 до 4
    global f          # функция
    global speed_var  # скорость изменения функции
    global r          # смещение 
    c = (time()-a)*speed_var+r
    b = globals()[f](c)
    count = ''
    if number == 4:
        if b<=0:
            plus = '-'
        else:
            plus = ' '
        b = abs(b)
        
        for i in range(len("%.6f" % b)):
            if speed_list[3][i] == speed_list[4][i] and speed_list[3][i] == speed_list[5][i] and \
               speed_list[3][i] == speed_list[6][i]:
                count += speed_list[6][i]
            elif speed_list[2][i] == speed_list[3][i] and speed_list[2][i] == speed_list[4][i] and \
                 speed_list[2][i] == speed_list[5][i]:
                count += speed_list[6][i]
            elif speed_list[1][i] == speed_list[2][i] and speed_list[1][i] == speed_list[2][i] and \
                 speed_list[1][i] == speed_list[3][i]:
                count += speed_list[6][i]
            elif speed_list[0][i] == speed_list[1][i] and speed_list[0][i] == speed_list[1][i] and \
                 speed_list[0][i] == speed_list[2][i]:
                count += speed_list[6][i]
            else:
                break                
        try:
            vizual(plus + "%.6f" % abs(float(count)))
        except:
            pass
        number = 0
    del speed_list[0]
    speed_list.append("%.6f" % b)
    
    number += 1
    root.after(step//4, upd)


# Вывод значения
def vizual(x):
    a1, a2 = spis(label_main['text'][1:])
    b1, b2 = spis(x[1:])
    try:
        for i in range(len(b1)):
        
            if b1[i] == a1[i]:
                pass
            elif b1[i] == a1[i] + 1:
                a1[i] = a1[i] + 1
            elif b1[i] >= a1[i] + 2:
                a1[i] = a1[i] + 2

            elif b1[i] == a1[i] - 1:
                a1[i] = a1[i] - 1
            elif b1[i] >= a1[i] - 5:
                a1[i] = a1[i] - 2
            elif b1[i] < a1[i] - 5:
                a1[i] = a1[i] + 2
            a1[i] %= 10
        if a2 == b2:
            pass
        elif len(a2) > len(b2):
            b2 += [0] * (len(a2) - len(b2))
        else:
            a2 += [0] * (len(b2) - len(a2))
        if b2 != a2:
            for i in range(len(b2)):
        
                if b2[i] == a2[i]:
                    pass
                elif b2[i] == a2[i] + 1:
                    a2[i] = a2[i] + 1
                elif b2[i] >= a2[i] + 2:
                    a2[i] = a2[i] + 2

                elif b2[i] == a2[i] - 1:
                    a2[i] = a2[i] - 1
                elif b2[i] >= a2[i] - 5:
                    a2[i] = a2[i] - 2
                elif b2[i] < a2[i] - 5:
                    a2[i] = a2[i] + 2
                if a2[i] >= 10:
                    a2[i] %= 10
    except Exception as e:
        print(e, traceback.format_exc())
    stroka = ''
    a2.reverse()
    for i in a2:
        stroka += str(i)
    stroka += '.'
    for i in a1:
        stroka += str(i)
    #print(a2, a1)
    label_main['text'] = x[0] + stroka


# Преобразование строки в 2 списка
def spis(x):
    b = x.find('.')
    a = []
    c = []
    for i in range(b+1, len(x)):
        a.append(int(x[i]))
    for i in range(b):
        c.append(int(x[b-i-1]))
    return a, c


# Задание переменных
root = Tk()
speed_var = 0.005
f = 'f1'
a = time()
r = 0
number = 0
speed_list = ['0.000000']*7
step = 160    
w = root.winfo_screenwidth()//2
h = root.winfo_screenheight()//2
l = w //2
t = h//2
root.title("Время")
root.geometry(f'{w}x{h}+{l}+{t}')

# Надпись, поле ввода и кнопка Пороговой частоты
Label(text="Пороговая частота(мс):").grid(row=0, column=0)
ent_time = Entry()
ent_time.grid(row=1, column=0)
btn_time = Button(text="Применить", command=timee).grid(row=1, column=1)

# Надпись, поле ввода и кнопка Скорости изменения
Label(text="Скорость изменения функции(0.005):").grid(row=2, column=0)
ent_time2 = Entry()
ent_time2.grid(row=3, column=0)
btn_time = Button(text="Применить", command=speed).grid(row=3, column=1)

# Основной вывод
label_main = Label(text=" 0.000000", font='Calibri  180')
label_main.grid(row=4, column=2)

# Выбор функции
languages = ["sin(c)+sin(2*c)", "sin(c)**3", "sin(x)+0.1*sin(10*x)+13", "round(sin(x)*10)",
             "round(sin(x)*10)+sin((x+0.5)*10)",
             "sin(x)+0.2*tan(0.99*x)+10*sin(2*x)", "-1**(round(sin(x)*10))+sin(x*2)*10+15",
             "sin(x)*cos(2*x)+525"]
languages_var = StringVar(value=languages[0])   
combobox = ttk.Combobox(textvariable=languages_var, values=languages, state="readonly", width = 32)
combobox.grid(row=5, column=0)
combobox.bind("<<ComboboxSelected>>", selected)

root.after(100, upd)
root.mainloop()
