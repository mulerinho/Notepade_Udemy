import tkinter



def novo():
    text_area.delete(1.0, 'end')


def salvando():
    guardando = text_area.get(1.0, 'end')
    arquivo = open('notepade.txt', 'w')
    arquivo.write(guardando)
    arquivo.close()


def Open():
    arquivo = open('notepade.txt', 'r')
    guardando = arquivo.read()
    text_area.insert(1.0, guardando)



# Instanciando
window = tkinter.Tk()
# Titulo da janela
window.title('JujubaPad')

# Tamanho da janela
window.minsize(600, 500)

# Area de texto
text_area = tkinter.Text(window, width=600, height=500)
text_area.pack()

# menu
main_menu = tkinter.Menu(window)
file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New', command=novo)
file_menu.add_command(label='Save', command=salvando)
file_menu.add_command(label='Open', command=Open)
file_menu.add_command(label='Exit', command=window.quit)

main_menu.add_cascade(label=' File', menu=file_menu)

window.config(menu=main_menu)

window.mainloop()


