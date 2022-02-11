from tkinter import filedialog, Tk


def load_file():
    Tk().withdraw()
    File = filedialog.askopenfile(
        title = "Directory",
        initialdir = "./",
        filetypes = [("Files","*.data")])
    if File is None:
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

        option = input('')

        if option == '1':
            load_file()
        elif option == '2':
            load_instructions()
        elif option == '3':
            continue
        elif option == '4':
            continue
        elif option == '5':
            exit()
        else:
            print("Elija una opcion entre 1 y 5")

if __name__ == '__main__':
    main_menu()
