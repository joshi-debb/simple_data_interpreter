from tkinter import filedialog, Tk

CantNumeros = 0
CantLetras  = 0
CantSimbolos = 0
CantCaracteres = 0

def Open():
    Tk().withdraw()
    File = filedialog.askopenfile(
        title = "Directory",
        initialdir = "./",
        filetypes = [("Files","*.*")]
    )

    if File is None:
        File('No se ha seleccionado un archivo\n')
        return None
    else:
        Text = File.read()
        File.close()
        return Text

if __name__ == '__main__':
    Lista = []
    txt = Open()

    if txt is not None: 
        print("=====================================================================")
        print(txt)
        if(len(txt) > 0):
            for Caracter in txt:
                CantCaracteres += 1
                if ord(Caracter) == 10:
                    pass
                elif ord(Caracter) == 32:
                    pass
                elif ord(Caracter) in range(48, 57):
                    CantNumeros += 1
                elif ord(Caracter) in range(65, 90):
                    CantLetras += 1
                elif ord(Caracter) in range(97, 122):
                    CantLetras += 1
                else:
                    CantSimbolos += 1
        else:
            print('No hay texto :v F')
    else:
        print('No se puede procesar\n')


print("=====================================================================")

print("Cantidad de Caracteres en el texto: " + str(CantCaracteres))
print("Cantidad de Numeros en el texto: " + str(CantNumeros))
print("Cantidad de Letras en el texto: " + str(CantLetras))
print("Cantidad de Simbolos en el texto: " + str(CantSimbolos))
    
print("=====================================================================")


