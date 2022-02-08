from tkinter import filedialog, Tk

def load_file():
    Tk().withdraw()
    File = filedialog.askopenfile(
        title = "Directory",
        initialdir = "./",
        filetypes = [("Files","*.data")])
    if File is None:
        File('No se ha seleccionado un archivo\n')
        return None
    else:
        Data = File.read()
        File.close()
        return Data

def load_instructions():
    Tk().withdraw()
    File = filedialog.askopenfile(
        title = "Directory",
        initialdir = "./",
        filetypes = [("Files","*.lfp")])
    if File is None:
        File('No se ha seleccionado un archivo\n')
        return None
    else:
        Instructions = File.read()
        File.close()
        return Instructions

def main_menu():
    flag = True
    while flag:
        print('=======================')
        print('Menu Principal')
        print('=======================')
        print('1. Cargar Data')
        print('2. Cargar Instrucciones')
        print('3. Analizar')
        print('4. Reportes')
        print('5. Salir')
        print('=======================')

        opt = input('> ')

        if opt == '1':
            load_file()
            continue
        if opt == '2':
            load_instructions()
            continue
        if opt == '3':
            continue
        if opt == '4':
            continue
        if opt == '5':
            exit()
        flag = False

if __name__ == '__main__':
    main_menu()
