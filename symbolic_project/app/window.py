from typing import Callable
import re as regex
from tkinter import Tk
from tkinter import Widget
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import PhotoImage
from tkinter import Entry
from tkinter import Text
from tkinter import Canvas
from tkinter import font as Font
from tkinter import messagebox as Messagebox
from tkinter.ttk import Style as TStyle
from tkinter.ttk import Notebook as TNotebook
from tkinter.ttk import Combobox as TCombobox
from symbolic_project.commons import Error
from symbolic_project.commons import PATH
from symbolic_project.project import fractal  # type: ignore
from symbolic_project.project.symbolic_method import problems  # type: ignore
from symbolic_project.app.symbolic_window import SymbolicWindow  # type: ignore

__back_color = 'white'
__fore_color = 'black'
__sec_color_1 = '#ededed'
__sec_color_2 = 'SlateGray'
__moon_icon: PhotoImage
__theme_button: Button
__style: TStyle
__widgets: list


def run():
    global __widgets
    __widgets = []

    window = Tk()
    __widgets.append(window)
    window.option_add('*TCombobox*Listbox*Font', Font.Font(family='Dubai', size=11))

    b: int = 600
    h: int = 500
    x: int = (int)(window.winfo_screenwidth() / 2 - b / 2)
    y: int = (int)(window.winfo_screenheight() / 2 - h / 2)

    window.title('PyScraper')
    window['bg'] = __back_color
    window.resizable(True, True)
    window.geometry(f'{b}x{h}+{x}+{y}')

    global __style
    __style = TStyle(window)
    __style.theme_create('white',
                         parent='alt',
                         settings={
                             'TNotebook': {'configure': {'tabmargins': [2, 5, 2, 0], 'background': 'white', 'borderwidth': 0}},
                             'TNotebook.Tab': {
                                 'configure': {'padding': [7, 2], 'background': __sec_color_1, 'foreground': 'black', 'font': ('Century Gothic', 11)},
                                 'map':       {'background': [('selected', 'white')], 'foreground': [('selected', 'black')], 'expand': [('selected', [1, 1, 1, 0])]}},
                             'TCombobox': {'configure': {'selectbackground': __sec_color_2, 'selectforeground': 'white', 'fieldbackground': __sec_color_1, 'bordercolor ': 'white', 'background': __sec_color_2, 'arrowcolor': __sec_color_1}}}
                         )

    __style.theme_create('black',
                         parent='alt',
                         settings={
                             'TNotebook': {'configure': {'tabmargins': [2, 5, 2, 0], 'background': 'black', 'borderwidth': 0}},
                             'TNotebook.Tab': {
                                 'configure': {'padding': [7, 2], 'background': __sec_color_2, 'foreground': 'white', 'font': ('Century Gothic', 11)},
                                 'map':       {'background': [('selected', 'black')], 'foreground': [('selected', 'white')], 'expand': [('selected', [1, 1, 1, 0])]}},
                             'TCombobox': {'configure': {'selectbackground': __sec_color_1, 'selectforeground': 'black', 'fieldbackground': __sec_color_2, 'bordercolor ': 'black', 'background': __sec_color_1, 'arrowcolor': __sec_color_2}}}
                         )

    toggle_bar()

    global __theme_button
    __theme_button = Button(master=window, command=lambda: __change_theme(), border=0)
    __theme_button.pack(side='top', expand=False, anchor='e', padx=10, pady=10)
    toggle_icon()

    frame: Frame = __frame(parent=window)
    frame.pack(side='top', expand=True, fill='both')
    __widgets.append(frame)

    # Menus
    menu_frame: Frame = __frame(parent=frame)
    menu_frame.rowconfigure(index=[0, 1, 2, 3], weight=1)
    menu_frame.columnconfigure(index=[0], weight=1)
    menu_frame.pack(expand=True, fill='both')
    __widgets.append(menu_frame)

    problem_frame: Frame = __frame(parent=frame)
    __widgets.append(problem_frame)

    problems_subframe: Frame = __frame(parent=problem_frame)
    problems_subframe.rowconfigure(index=[0, 1, 2, 3], weight=1)
    problems_subframe.columnconfigure(index=[0], weight=1)
    problems_subframe.pack(side='top', expand=True, fill='both')
    __widgets.append(problems_subframe)

    symbolic_frame: Frame = __frame(parent=frame)
    __widgets.append(symbolic_frame)

    symbolic_book: TNotebook = TNotebook(master=symbolic_frame)
    symbolic_book.pack(expand=True, fill='both')
    __widgets.append(symbolic_book)

    symbolic_1: Frame = __symbolic_frame(parent=symbolic_book, text='Método simbólico: Parte 1', options=problems.get_list_1())
    symbolic_1.pack(expand=True, fill='both')
    __widgets.append(symbolic_1)

    symbolic_2: Frame = __frame(parent=symbolic_book)
    symbolic_2.pack(expand=True, fill='both')
    __widgets.append(symbolic_2)

    symbolic_book.add(symbolic_1, text='Parte 1')
    symbolic_book.add(symbolic_2, text='Parte 2')

    fractal_frame: Frame = __frame(parent=frame)
    __widgets.append(fractal_frame)

    fractal_book: TNotebook = TNotebook(master=fractal_frame)
    fractal_book.pack(expand=True, fill='both')
    __widgets.append(fractal_book)

    fractal_1: Frame = __fractal_frame(parent=fractal_book, text='Sierpinski Carpe', function=fractal.sierpinski_carpet)
    fractal_1.pack(expand=True, fill='both')

    fractal_2: Frame = __fractal_frame(parent=fractal_book, text='Sierpinski Sieve (60)', function=lambda: fractal.sierpinsky_sieve_60)
    fractal_2.pack(expand=True, fill='both')

    fractal_3: Frame = __fractal_frame(parent=fractal_book, text='Sierpinski Sieve (90)', function=lambda: fractal.sierpinsky_sieve_90)
    fractal_3.pack(expand=True, fill='both')

    fractal_4: Frame = __fractal_frame(parent=fractal_book, text='Sierpinski Sieve (102)', function=lambda: fractal.sierpinsky_sieve_102)
    fractal_4.pack(expand=True, fill='both')

    fractal_5: Frame = __fractal_frame(parent=fractal_book, text='H', function=lambda: fractal.h)
    fractal_5.pack(expand=True, fill='both')

    fractal_6: Frame = __fractal_frame(parent=fractal_book, text='Haferman Carpet', function=lambda: fractal.haferman_carpet)
    fractal_6.pack(expand=True, fill='both')

    fractal_7: Frame = __fractal_frame(parent=fractal_book, text='Cantor Square', function=lambda: fractal.cantor_square)
    fractal_7.pack(expand=True, fill='both')

    fractal_8: Frame = __fractal_frame(parent=fractal_book, text='Box', function=lambda: fractal.box)
    fractal_8.pack(expand=True, fill='both')

    fractal_book.add(fractal_1, text='Sierpinski Carpet')
    fractal_book.add(fractal_2, text='Sierpinski Sieve (60)')
    fractal_book.add(fractal_3, text='Sierpinski Sieve (90)')
    fractal_book.add(fractal_4, text='Sierpinski Sieve (102)')
    fractal_book.add(fractal_5, text='H')
    fractal_book.add(fractal_6, text='Haferman Carpet')
    fractal_book.add(fractal_7, text='Cantor Square')
    fractal_book.add(fractal_8, text='Box')

    about_frame: Frame = __frame(parent=frame)
    # __widgets.append(about_frame)

    # Main menu
    menu_title: Label = __title_label(parent=menu_frame, text='Método Simbólico &\nFractales')
    menu_title.grid(column=0, row=0)

    problem_button: Button = __menu_button(parent=menu_frame, text='INICIAR', command=lambda: __go_to(problem_frame, menu_frame))
    problem_button.grid(column=0, row=1)

    about_button: Button = __menu_button(parent=menu_frame, text='ABOUT', command=lambda: __go_to(about_frame, menu_frame))
    about_button.grid(column=0, row=2)

    # Problem Menu
    symbolic_button: Button = __menu_button(parent=problems_subframe, text='METODO SIMBOLICO', command=lambda: __go_to(symbolic_frame, problem_frame))
    symbolic_button.grid(column=0, row=1)

    fractal_button: Button = __menu_button(parent=problems_subframe, text='FRACTALES', command=lambda: __go_to(fractal_frame, problem_frame))
    fractal_button.grid(column=0, row=2)

    problem_back_button: Button = __back_button(parent=problem_frame, command=lambda: __go_to(menu_frame, problem_frame))
    problem_back_button.pack(side='top', expand=False, anchor='w')

    # Symbolic Menu
    symbolic_back_button: Button = __back_button(parent=symbolic_frame, command=lambda: __go_to(problem_frame, symbolic_frame))
    symbolic_back_button.pack(side='top', expand=False, anchor='w')

    # Fractal Menu
    fractal_back_button: Button = __back_button(parent=fractal_frame, command=lambda: __go_to(problem_frame, fractal_frame))
    fractal_back_button.pack(side='top', expand=False, anchor='w')

    # About Menu
    about_text: Text = Text(master=about_frame, wrap='word', highlightthickness=0, border=0)
    about_text.tag_config('title', font=('Times New Roman', 30))
    about_text.tag_config('fonts', font=('Times New Roman', 20))
    about_text.insert('end', 'Proyecto computacional:\nEntrega 2\n\n', 'title')
    about_text.insert('end', 'Andrea Arias\n', 'fonts')
    about_text.insert('end', 'Omar Cifuentes\n', 'fonts')
    about_text.insert('end', 'Santiago Hernández\n', 'fonts')
    about_text.configure(state='disabled')
    about_text.pack(expand=True, fill='both', padx=40)

    about_back_button: Button = __back_button(parent=about_frame, command=lambda: __go_to(menu_frame, about_frame))
    about_back_button.pack(expand=False, anchor='w')

    window.mainloop()


def __change_theme() -> None:
    global __back_color
    global __fore_color
    global __sec_color_1
    global __sec_color_2
    global __widgets

    __back_color, __fore_color = __fore_color, __back_color
    __sec_color_1, __sec_color_2 = __sec_color_2, __sec_color_1

    for widget in __widgets:
        if widget.__class__.__name__ == 'Entry':
            try:
                widget.configure(bg=__sec_color_1, fg=__sec_color_2, selectforeground=__back_color)  # type: ignore
            except (Exception):
                pass
        else:
            try:
                widget.configure(bg=__back_color)  # type: ignore
            except (Exception):
                pass

            try:
                widget.configure(fg=__fore_color)  # type: ignore
            except (Exception):
                pass

    toggle_bar()
    toggle_icon()


def toggle_icon() -> None:
    global __moon_icon
    global __theme_button

    __moon_icon = PhotoImage(file=PATH + f'/resources/images/{__fore_color}_moon.png').zoom(1).subsample(8)
    __theme_button.configure(bg=__back_color, activebackground=__fore_color, image=__moon_icon)


def toggle_bar() -> None:
    global __style
    __style.theme_use(__back_color)


def __frame(parent: Widget) -> Frame:
    frame: Frame = Frame(master=parent, bg=__back_color)
    __widgets.append(frame)
    return frame


def __label(parent: Widget, text: str) -> Label:
    label: Label = Label(master=parent, bg=__back_color, fg=__fore_color, font=('Corbel', 15), anchor='w', text=text)
    __widgets.append(label)
    return label


def __title_label(parent: Widget, text: str) -> Label:
    label: Label = Label(master=parent, bg=__back_color, fg=__fore_color, font=('Lucida Sans Typewriter', 30), anchor='center', text=text)
    __widgets.append(label)
    return label


def __button(parent: Widget, text: str, command: Callable) -> Button:
    button: Button = Button(master=parent, bg=__back_color, fg=__fore_color, text=text, command=command)
    __widgets.append(button)
    return button


def __menu_button(parent: Widget, text: str, command: Callable) -> Button:
    button: Button = Button(master=parent, bg=__back_color, fg=__fore_color, font=('Lucida Sans', 18), text=text, command=command)
    __widgets.append(button)
    return button


def __back_button(parent: Widget, command: Callable) -> Button:
    button: Button = Button(master=parent, bg=__back_color, fg=__fore_color, font=('Consolas', 14, 'bold'), text='<-', command=command)
    __widgets.append(button)
    return button


def __entry(parent: Widget) -> Entry:
    entry: Entry = Entry(master=parent, bg=__sec_color_1, fg=__sec_color_2, font=('Consolas', 14), justify='center', border=0, width=10, insertbackground='lime', selectbackground='lime', selectforeground=__back_color)
    __widgets.append(entry)
    return entry


def __go_to(target_frame: Frame, forget_frame: Frame) -> None:
    forget_frame.pack_forget()
    target_frame.pack(expand=True, fill='both')


def __symbolic_frame(parent: Widget, text: str, options: dict) -> Frame:
    frame: Frame = __frame(parent)
    frame.rowconfigure(index=[0, 2, 3], weight=1)  # type: ignore
    frame.columnconfigure(index=[0], weight=1)  # type: ignore
    frame.pack(expand=True, fill='both')

    title: Label = __title_label(parent=frame, text=text)
    title.grid(column=0, row=0)

    combobox: TCombobox = TCombobox(master=frame, state='readonly', values=list(options.values()), font=('Dubai', 13), justify='center', width=60)
    combobox.set('Elija una de las siguientes cadenas:')
    combobox.grid(column=0, row=1, padx=50)

    frame_entry = __frame(parent=frame)
    frame_entry.grid(column=0, row=2)

    label_entry: Label = __label(parent=frame_entry, text=f'Inserte el valor de n (n: longitud de cadenas o cantidad total para cualquier longitud): ')
    label_entry.pack()

    entry: Entry = __entry(parent=frame_entry)
    entry.pack(pady=4, ipadx=3, ipady=3)

    button: Button = __button(parent=frame, command=lambda: __val_symbolic(combobox, entry, options), text='Calcular')
    button.configure(font=('Consolas', 12, 'bold'))
    button.grid(column=0, row=3)

    return frame


def __val_combo(combobox: TCombobox):
    return combobox.current() == -1


def __val_entry(entry: Entry):
    return regex.search('\D', entry.get()) != None


def __val_symbolic(combobox: TCombobox, entry: Entry, options: dict):
    try:
        if __val_combo(combobox):
            raise Exception('Debe elegir una opción en el combobox.')

        if __val_entry(entry):
            raise Exception('Debe digitar un número.')

        code :str = list(options.keys())[combobox.current()].replace("_",entry.get())
        symbolicWindow = SymbolicWindow(code)

    except Error as e:
        Messagebox.showerror('Error!', str(e))
    except Exception as e:
        print(f'{__file__}: {str(e)}')


def __fractal_frame(parent: Widget, text: str, function: Callable) -> Frame:
    frame: Frame = __frame(parent)
    frame.rowconfigure(index=[0, 1, 2], weight=1)  # type: ignore
    frame.columnconfigure(index=[0], weight=1)  # type: ignore
    frame.pack(expand=True, fill='both')

    title: Label = __title_label(parent=frame, text=text)
    title.grid(column=0, row=0)

    frame_entry = __frame(parent=frame)
    frame_entry.grid(column=0, row=1)

    label: Label = __label(parent=frame_entry, text=f'Inserte el tamaño de n para generar el fractal: ')
    label.pack()

    entry: Entry = __entry(parent=frame_entry)
    entry.pack(pady=4, ipadx=3, ipady=3)

    button: Button = __button(parent=frame, command=lambda: print(function, entry.get()), text='Calcular')
    button.configure(font=('Consolas', 12, 'bold'))
    button.grid(column=0, row=2)

    return frame
