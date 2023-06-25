from tkinter import *
import random
from datetime import date

# Создание окна
window = Tk()
window.title('STDs')
window.attributes('-toolwindow', True)
window.resizable(False, False)
window.geometry('450x430+500+200')

random_number = 0
current_date = 0

risk_value = IntVar()
risk_var = 0

# Установка шрифтов
font_label = ('Trebuchet MS', 13)
font_answer = ('Trebuchet MS', 12)
font_button = ('Trebuchet MS', 13, 'bold')

# Переход к выбору режима
def start():
    global random_number, current_date, file
    label.forget()
    image_label.forget()
    start_btn.forget()
    warning_label.forget()
    current_date = date.today()
    random_number = random.randrange(1000, 10000)
    file = open('users.txt', 'a')
    file.write('Дата: {}\nПользователь №{} зарегистрирован\n'.format(current_date,random_number))
    file.close()
    label.config(text='№{}'.format(random_number))
    label.pack(anchor=NW, padx=15, pady=10)
    warning_label.config(text='ВЫБОР РЕЖИМА:',
                         font=('Trebuchet MS', 13, 'bold'))
    warning_label.pack(anchor=N, pady=25)
    risk_btn.config(text='''ОЦЕНКА СТЕПЕНИ
    РИСКА ЗППП''', font=font_button,
                    width=18,
                    command=start_risk)
    risk_btn.pack(anchor=N, pady=30)
    start_btn.config(text='САМОДИАГНОСТИКА\nЗППП',
                     width=18)
    start_btn.pack(anchor=N, pady=10)

def start_risk():
    file = open('users.txt', 'a')
    file.write('РЕЖИМ: ОЦЕНКА СТЕПЕНИ РИСКА ЗППП\nОтветы:\n')
    risk_btn.forget()
    start_btn.forget()
    warning_label.config(text='''Ведете ли вы половую жизнь сейчас?
    Если нет, вели ли ее раньше?''', justify=CENTER, font=font_label)
    warning_label.pack(anchor=N, pady=15)
    risk_rb1.config(text='ДА',
                    font=font_answer,
                    variable=risk_value, value=1)
    risk_rb1.pack(anchor=N, pady=30)
    risk_rb2.config(text='НЕТ',
                    font=font_answer,
                    variable=risk_value, value=2)
    risk_rb2.pack(anchor=N)
    risk_btn.config(text='ДАЛЕЕ', width=0,
                    command=risk_test2)
    risk_btn.pack(anchor=N, pady=45)

def risk_test2():
    global risk_var, file
    risk_btn.forget()
    risk_rb1.forget()
    risk_rb2.forget()
    if risk_value.get()==1:
        risk_var = 1
        file = open('users.txt', 'a')
        file.write('1. ДА\n')
        file.close()
        warning_label.config(text='''Последний половой контакт был с постоянным 
половым партнером? 
Сколько половых партнеров
у вас было за последние два месяца?''')
        risk_rb1.config(text='ДА, один',
                        variable=risk_value, value=3)
        risk_rb1.pack(anchor=N)
        risk_rb2.config(text='ДА, несколько',
                        variable=risk_value, value=4)
        risk_rb2.pack(anchor=N)
        risk_rb3.config(text='НЕТ, один',
                        variable=risk_value, value=5,
                        font=font_answer)
        risk_rb3.pack(anchor=N)
        risk_rb4.config(text='НЕТ, несколько',
                        variable=risk_value, value=6,
                        font=font_answer)
        risk_rb4.pack(anchor=N)
        risk_btn.config(command=risk_test3)
        risk_btn.pack(anchor=N, pady=30)
    elif risk_value.get()==2:
        risk_var = 0
        file = open('users.txt', 'a')
        file.write('1. НЕТ\n')
        file.close()
        warning_label.config(text='''Случалось ли вам или вашим половым
партнерам употреблять наркотики,
в том числе инъекционные?''')
        risk_rb1.config(text='ДА',
                        variable=risk_value, value=3)
        risk_rb1.pack(anchor=N, pady=30)
        risk_rb2.config(text='НЕТ',
                        variable=risk_value, value=4)
        risk_rb2.pack(anchor=N)
        risk_btn.config(command=risk_test7)
        risk_btn.pack(anchor=N, pady=45)

def risk_test7():
    global file, risk_var
    if risk_value.get()==3:
        risk_var+=1
        file = open('users.txt', 'a')
        file.write('3. ДА\n')
        file.close()
    elif risk_value.get()==4:
        risk_var+=0
        file = open('users.txt', 'a')
        file.write('3. НЕТ\n')
        file.close()
    warning_label.config(text='''Были ли у вас раньше инфекции,
передаваемые половым путем?''')
    risk_rb1.config(text='ДА',
                    variable=risk_value, value=12)
    risk_rb2.config(text='НЕТ',
                    variable=risk_value, value=13)
    risk_btn.config(command=risk_test8)
    risk_btn.pack(anchor=N, pady=45)

def risk_test8():
    global risk_var, file
    risk_btn.forget()
    risk_rb1.forget()
    risk_rb2.forget()
    if risk_value.get()==12:
        risk_var+=1
        file = open('users.txt', 'a')
        file.write('4. ДА\n')
        file.close()
    elif risk_value.get()==13:
        risk_var+=0
        file = open('users.txt', 'a')
        file.write('4. НЕТ\n')
        file.close()
    warning_label.config(text='''Беспокоят ли вас (или вашего партнера)
какие-либо симптомы, заставляющие подозревать
наличие инфекции, передаваемой половым путем?
 
 * высыпания в области гениталий
 * боль или жжение при мочеиспускании
 * необычные выделения''')
    risk_rb1.config(text='ДА',
                    variable=risk_value, value=14)
    risk_rb1.pack(anchor=N, pady=10)
    risk_rb2.config(text='НЕТ',
                    variable=risk_value, value=15)
    risk_rb2.pack(anchor=N)
    risk_btn.config(text='ДАЛЕЕ', command=finish_risk_no)
    risk_btn.pack(anchor=N, pady=20)

def finish_risk_no():
    global file, risk_var
    warning_label.forget()
    risk_btn.forget()
    risk_rb1.forget()
    risk_rb2.forget()
    if risk_value.get()==14:
        risk_var+=3
        file = open('users.txt', 'a')
        file.write('5. ДА\n')
        file.write('Итог: {} из 5\n\n'.format(risk_var))
        file.close()
    elif risk_value.get()==15:
        risk_var+=0
        file = open('users.txt', 'a')
        file.write('5. НЕТ\n')
        file.write('Итог: {} из 5\n\n'.format(risk_var))
        file.close()
    if risk_var >= 3:
        warning_label.config(text='''Вы набрали {} баллов из 5 возможных.
Желаете перейти к самодиагностике ЗППП?'''.format(risk_var))
        warning_label.pack(anchor=N, pady=15)
        start_btn.config(text='ДА', width=5)
        start_btn.pack(anchor=N, pady=40)
        risk_btn.config(text='НЕТ', width=5, command=close_window)
        risk_btn.pack(anchor=N)
    else:
        warning_label.config(text='''Вы набрали {} баллов из 5 возможных - 
низкая степень риска ЗППП'''.format(risk_var))
        warning_label.pack(anchor=N)
        risk_btn.config(text='ЗАВЕРШИТЬ', command=close_window)
        risk_btn.pack(anchor=N, pady=45)

def risk_test3():
    global risk_var, file
    risk_btn.forget()
    risk_rb1.forget()
    risk_rb2.forget()
    risk_rb3.forget()
    risk_rb4.forget()
    if risk_value.get()==3:
        risk_var+=0
        file = open('users.txt', 'a')
        file.write('2. ДА, один\n')
        file.close()
    elif risk_value.get()==4:
        risk_var+=1
        file = open('users.txt', 'a')
        file.write('2. ДА, несколько\n')
        file.close()
    elif risk_value.get()==5:
        risk_var+=1
        file = open('users.txt', 'a')
        file.write('2. НЕТ, один\n')
        file.close()
    elif risk_value.get()==6:
        risk_var+=2
        file = open('users.txt', 'a')
        file.write('2. НЕТ, несколько\n')
        file.close()
    warning_label.config(text='''Пользуетесь ли вы презервативами?
Если да, то как вы их используете -
всегда или иногда?''')
    risk_rb1.config(text='ДА, всегда',
                       variable=risk_value, value=7)
    risk_rb1.pack(anchor=N)
    risk_rb2.config(text='ДА, иногда',
                    variable=risk_value, value=8)
    risk_rb2.pack(anchor=N)
    risk_rb3.config(text='НЕТ',
                    variable=risk_value, value=9,
                    font=font_answer)
    risk_rb3.pack(anchor=N)
    risk_btn.config(command=risk_test4)
    risk_btn.pack(anchor=N, pady=30)

def risk_test4():
    global risk_var, file
    risk_btn.forget()
    risk_rb1.forget()
    risk_rb2.forget()
    risk_rb3.forget()
    if risk_value.get()==7:
        risk_var+=0
        file = open('users.txt', 'a')
        file.write('3. ДА, всегда\n')
        file.close()
    elif risk_value.get()==8:
        risk_var+=1
        file = open('users.txt', 'a')
        file.write('3. ДА, иногда\n')
        file.close()
    elif risk_value.get()==9:
        risk_var+=2
        file = open('users.txt', 'a')
        file.write('3. НЕТ\n')
        file.close()
    warning_label.config(text='''Случалось ли вам или вашим половым
партнерам употреблять наркотики,
в том числе инъекционные?''')
    risk_rb1.config(text='ДА',
                    variable=risk_value, value=10)
    risk_rb1.pack(anchor=N, pady=30)
    risk_rb2.config(text='НЕТ',
                    variable=risk_value, value=11)
    risk_rb2.pack(anchor=N)
    risk_btn.config(command=risk_test5)
    risk_btn.pack(anchor=N, pady=45)

def risk_test5():
    global risk_var, file
    risk_btn.forget()
    risk_rb1.forget()
    risk_rb2.forget()
    if risk_value.get()==10:
        risk_var+=1
        file = open('users.txt', 'a')
        file.write('4. ДА\n')
        file.close()
    elif risk_value.get()==11:
        risk_var+=0
        file = open('users.txt', 'a')
        file.write('4. НЕТ\n')
        file.close()
    warning_label.config(text='''Были ли у вас раньше инфекции,
передаваемые половым путем?''')
    risk_rb1.config(text='ДА',
                    variable=risk_value, value=12)
    risk_rb1.pack(anchor=N, pady=30)
    risk_rb2.config(text='НЕТ',
                    variable=risk_value, value=13)
    risk_rb2.pack(anchor=N)
    risk_btn.config(command=risk_test6)
    risk_btn.pack(anchor=N, pady=45)

def risk_test6():
    global risk_var, file
    risk_btn.forget()
    risk_rb1.forget()
    risk_rb2.forget()
    if risk_value.get()==12:
        risk_var+=1
        file = open('users.txt', 'a')
        file.write('5. ДА\n')
        file.close()
    elif risk_value.get()==13:
        risk_var+=0
        file = open('users.txt', 'a')
        file.write('5. НЕТ\n')
        file.close()
    warning_label.config(text='''Беспокоят ли вас (или вашего партнера)
какие-либо симптомы, заставляющие подозревать
наличие инфекции, передаваемой половым путем?
 
 * высыпания в области гениталий
 * боль или жжение при мочеиспускании
 * необычные выделения''')
    risk_rb1.config(text='ДА',
                    variable=risk_value, value=14)
    risk_rb1.pack(anchor=N, pady=10)
    risk_rb2.config(text='НЕТ',
                    variable=risk_value, value=15)
    risk_rb2.pack(anchor=N)
    risk_btn.config(text='ДАЛЕЕ', command=finish_risk_yes)
    risk_btn.pack(anchor=N, pady=20)

def finish_risk_yes():
    global file, risk_var
    warning_label.forget()
    risk_btn.forget()
    risk_rb1.forget()
    risk_rb2.forget()
    if risk_value.get()==14:
        risk_var+=3
        file = open('users.txt', 'a')
        file.write('6. ДА\n')
        file.write('Итог: {} из 10\n\n'.format(risk_var))
        file.close()
    elif risk_value.get()==15:
        risk_var+=0
        file = open('users.txt', 'a')
        file.write('6. НЕТ\n')
        file.write('Итог: {} из 10\n\n'.format(risk_var))
        file.close()
    if risk_var >= 6:
        warning_label.config(text='''Вы набрали {} баллов из 10 возможных.
Желаете перейти к самодиагностике ЗППП?'''.format(risk_var))
        warning_label.pack(anchor=N, pady=15)
        start_btn.config(text='ДА', width=5)
        start_btn.pack(anchor=N, pady=40)
        risk_btn.config(text='НЕТ', width=5, command=close_window)
        risk_btn.pack(anchor=N)
    else:
        warning_label.config(text='''Вы набрали {} баллов из 10 возможных - 
низкая степень риска ЗППП'''.format(risk_var))
        warning_label.pack(anchor=N)
        risk_btn.config(text='ЗАВЕРШИТЬ', command=close_window)
        risk_btn.pack(anchor=N, pady=45)

# Закрытие окна
def close_window():
    window.destroy()

# Основная текстовая метка
label = Label(window, text='''ГРАФИЧЕСКИЙ ПОЛЬЗОВАТЕЛЬСКИЙ ИНТЕРФЕЙС
ДЛЯ САМОДИАГНОСТИКИ ЗАБОЛЕВАНИЙ,
ПЕРЕДАЮЩИХСЯ ПОЛОВЫМ ПУТЕМ''', font=font_label)
label.pack(anchor=N, pady=10)

# Изображение
start_image = PhotoImage(file='med_icon.png')
image_label = Label(window, image=start_image)
image_label.pack(side=TOP)

# Основная кнопка
start_btn = Button(window, text='''НАЧАТЬ
ДИАГНОСТИКУ''', font=font_button, command=start)
start_btn.pack(anchor=N, pady=20)

# Текстовая метка
warning_label = Label(window, text='''※ Данный интерфейс не имеет медицинской лицензии и не должен заменять 
заключение лицензированного практикующего врача. Он предоставляет    
информацию, которая поможет принять решение на основе легкодоступной 
информации о симптомах перед консультацией с поставщиком услуг      
здравоохранения.''', justify=LEFT, font=('Trebuchet MS', 8))
warning_label.pack(anchor=N, side=TOP)

# Кнопка
risk_btn = Button(window)

# Переключатели
risk_rb1 = Radiobutton(window)
risk_rb2 = Radiobutton(window)
risk_rb3 = Radiobutton(window)
risk_rb4 = Radiobutton(window)

# Отображение окна
window.mainloop()
