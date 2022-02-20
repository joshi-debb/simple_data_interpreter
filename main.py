#llbreria para creacion de graficas
import matplotlib.pyplot as plt
#librerias para creacion y exportacion a HTML
from os import startfile
from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader
#libreria para abrir ventanas en escritorio
from tkinter import Tk
from tkinter.filedialog import askopenfilename
#libreria para importar Listas de tipo Type[List]
from typing import List
#libreria para  para cargar imágenes desde archivos y para crear nuevas imágenes
from PIL import Image

#listas globales
#archivo .data almacenado linea por linea
data_base = []
#archivo .lfp almacenado linea por linea
directions_base = []
#listado de meses
month = []
#listado de anios
year = []
#lista de listas de objetos de productos
List_Of_Market = []
#lista de listas de instrucciones
List_Of_Graphs = []
#listado de productos como objetos
item_products = []
#listado de instrucciones como objetos
item_directions = []
#lista de objetos para mandarlos al parseo
item_subject = []
#lista de instrucciones para mandarlos al parse
item_subject2 = []
#listas de datos para imprimir graficas
x_data_graphics = []
y_data_graphics = []

#variables globales
#aux para parseo de nombre de mes
month_Name = ''
#aux para parseo de nombre de anio
year_Name = ''
#aux para parseo de objetos
item_product = ''
#aux para parseo de instrucciones
item_direction = ''

#clase Item para almacenar productos como objetos
class Item:
    def __init__(self, item_name: str, item_price: float, item_sold: int) -> None:
        self.item_name: str = item_name.upper()
        self.item_price: float = float(item_price)
        self.item_sold: int = int(item_sold)
        self.item_earnings: float = (int(item_sold)*float(item_price))

#clase market para almacenar meses y anio como objetos
class Market:
    def __init__(self, month_name: str, year_name: int ) -> None:
        self.month_name: str = month_name.upper()
        self.year_name: int = year_name
        #lista de itemes para manipular las ventas
        self.items_list: list = []

    #metodo que aniade un item a la lista de items
    def add_Item(self, item: Item):
        self.items_list.append(item)
    
    #metodo que invoca el metodo burbuja para ordenar objetos
    def sort_datas_earnings(self):
        return bubble_sort_earnings(self.items_list)

    #devuelve el item con el mayor numero de ventas
    def sort_datas_up_solds(self):
        bubble_sort_solds(self.items_list)
        return (self.items_list[0].item_name)

    #devuelve el item con el menor numero de ventas
    def sort_datas_low_solds(self):
        bubble_sort_solds(self.items_list)
        return (self.items_list[len(self.items_list)-1].item_name)

#clase Item para instrucciones como objetos
class Direction:
    def __init__(self, graph_name: str, graph_type: str, graph_title:
                                   str, graph_title_X: str, graph_title_Y: str) -> None:
        self.graph_name: str = graph_name
        self.graph_type: str = graph_type
        self.graph_title: str = graph_title
        self.graph_title_X: str = graph_title_X
        self.graph_title_Y: str = graph_title_Y

class Graphics:
    def __init__(self) -> None:
        #lista de instrucciones para manipular las graficas
        self.instructions_list: list = []
    
    #metodo que aniade un item a la lista de items
    def add_Direction(self, direction: Direction):
        self.instructions_list.append(direction)

    def plot_graphics(self):

        plt.rcdefaults()
        #subploteo de grafica de barras
        figB, axB = plt.subplots()
        #subploteo de grafica de lineas
        figL, axL = plt.subplots()
        #subploteo de grafica de pastel
        figP, axP = plt.subplots()

        for markets in List_Of_Market:
            for item in markets.items_list:
                #llenando las listas con los datos de los objetos
                x_data_graphics.append(item.item_name)
                y_data_graphics.append(item.item_sold * item.item_price)

        # Datos Gráfica de Barras
        ejeXB = x_data_graphics
        ejeYB = y_data_graphics
        # Datos Gráfica de Líneas
        ejeXL = x_data_graphics
        ejeYL = y_data_graphics
        # Datos Gráfica de pie
        ejeXP = x_data_graphics
        ejeYP = y_data_graphics
        
        for direction in self.instructions_list:
            
            if direction.graph_type.upper() == "BARRAS":
                # Datos de los ejes de la gráfica de barras, se usa función bar()   
                axB.bar(ejeXB, ejeYB) 
                # Titulos de los ejes  
                axB.set_xlabel(direction.graph_title_X, fontdict = { 'fontsize':12, 'color':'blue'})
                axB.set_ylabel(direction.graph_title_Y, fontdict = { 'fontsize':12, 'color':'green'})

                axB.grid(axis='y', color='lightgray', linestyle='dashed')

                for markets in List_Of_Market:
                    #tomando los atributos de la clase Market
                    title_mes = markets.month_name
                    title_anio = markets.year_name 
                    
                axB.set_title(direction.graph_title.upper() +'\n'+ title_mes + title_anio , fontdict = { 'fontweight':'bold', 'fontsize':16, 'color':'red'})

                figB.savefig('./{}.png'.format(direction.graph_name))

                Graphic_Barra = Image.open('./{}.png'.format(direction.graph_name))
                Graphic_Barra.show()

                print("Se Ha Generado Un Grafico De Barras!")

            elif direction.graph_type.upper() == "LINEAS":
                # Configuración de los ejes de la gráfica de lineas, se usa función plot()
                axL.plot(ejeXL, ejeYL) 
                # Titulos de los ejes
                axL.set_xlabel(direction.graph_title_X, fontdict = {'fontsize':12, 'color':'blue'})
                axL.set_ylabel(direction.graph_title_Y, fontdict = {'fontsize':12, 'color':'green'})

                axL.grid(axis='y', color='darkgray', linestyle='dashed')

                for markets in List_Of_Market:
                    #tomando los atributos de la clase Market
                    title_mes = markets.month_name
                    title_anio = markets.year_name

                axL.set_title(direction.graph_title.upper() +'\n'+ title_mes + title_anio , fontdict = { 'fontweight':'bold', 'fontsize':16, 'color':'red'})

                figL.savefig('./{}.png'.format(direction.graph_name))

                Graphic_Line = Image.open('./{}.png'.format(direction.graph_name))
                Graphic_Line.show()

                print("Se Ha Generado Un Grafico De Lineas!")

            elif direction.graph_type.upper() == "PIE" or direction.graph_type.upper() == "PASTEL":
                # Configuración de los trazos de la grafica de pastel, se usa función pie()
                axP.pie(ejeYP, labels = ejeXP, autopct="%0.1f %%") 

                axP.grid(axis='y', color='darkgray', linestyle='dashed')

                for markets in List_Of_Market:
                    #tomando los atributos de la clase Market
                    title_mes = markets.month_name
                    title_anio = markets.year_name

                axP.set_title(direction.graph_title.upper() +'\n'+ title_mes + title_anio , fontdict = { 'fontweight':'bold', 'fontsize':16, 'color':'red'})

                figP.savefig('./{}.png'.format(direction.graph_name))

                Graphic_Pie = Image.open('./{}.png'.format(direction.graph_name))
                Graphic_Pie.show()

                print("Se Ha Generado Un Grafico De Pastel!")

            else:
                print("Especifique un tipo valido de grafica")
                print("===>Grafica: Barras, Lineas o Pie<===")


#metodo para realizar el ordenamiento burbuja mayor a menor ganancias
def bubble_sort_earnings(data_to_print: List[Item]):
    data_earnings = data_to_print.copy()
    for i in range(len(data_earnings) - 1):
        for j in range(0, len(data_earnings) - i - 1):
            if data_earnings[j].item_earnings < data_earnings[j + 1].item_earnings:
                    data_earnings[j], data_earnings[j + 1] = data_earnings[j + 1], data_earnings[j]
    return data_earnings

#metodo para realizar el ordenamiento burbuja mayor a menor ventas
def bubble_sort_solds(data_to_print: List[Item]):
    for i in range(len(data_to_print) - 1):
        for j in range(0, len(data_to_print) - i - 1):
            if data_to_print[j].item_sold < data_to_print[j + 1].item_sold:
                    data_to_print[j], data_to_print[j + 1] = data_to_print[j + 1], data_to_print[j]
    return data_to_print


#metodo para extraer instrucciones separadas por ,
def extract_directions(pointer: list):
    #crear lista de objetos,unidos,sin espacios y separados por '\n'
    directions_list = item_direction.join(pointer).replace('\n',';').split(';')
    #print(directions_list)
    #recorrer lista de objetos
    for item in directions_list:
        try:
            #separar posiciones por ','
            position = item.split(',')
            #la priemra posicion deber removerse el 'NOMBRE' , ':' , '¿' , '"' y quitar espacios
            name = position[0].replace('Nombre','').replace(':','').replace('¿','').replace('"','').strip()
            #print(name)
            #la segunda posicion deber removerse el 'NOMBRE' , ':' , '"' y quitar espacios
            type = position[1].replace('Grafica','').replace(':','').replace('"','').strip()
            #la segunda posicion deber removerse el 'NOMBRE' , ':' , '"' y quitar espacios
            title = position[2].replace('Titulo','').replace(':','').replace('"','').strip()
            #la segunda posicion deber removerse el 'NOMBRE' , ':' , '"' y quitar espacios
            titleX = position[3].replace('TituloX','').replace(':','').replace('"','').strip()
            #la priemra posicion deber removerse el 'NOMBRE' , ':' , '?' , '"' y quitar espacios
            titleY = position[4].replace('TituloY','').replace(':','').replace('"','').replace('?','').strip()
            #aniadimos los datos al constructor de items
            item_directions.append(Direction(name,type,title,titleX,titleY))
            #retornar lista
        except IndexError:
            item = 'null'
    return item_directions
        
#metodo para extraer el anio y el mes
def extract_keys(directions_base: list):
    #apuntador en la lista database
    extract_pointer = directions_base[0]
    graphics = Graphics()
    #almacenar el objeto en la lista de general de graficas
    List_Of_Graphs.append(graphics)
    #no guardar nada que este antes del '<'
    while extract_pointer != '<':
        directions_base.pop(0)
        extract_pointer = directions_base[0]
    #reiniciar los punteros
    directions_base.pop(0)
    extract_pointer = directions_base[0]
    #no guardar nada que este despues de '>'
    while extract_pointer != '>':
        #almacenar los objetos separados por ,
        item_subject2.append(directions_base.pop(0))
        extract_pointer = directions_base[0]
    #mandar los objetos para parseo
    for Direction in extract_directions(item_subject2):
        #despues del parseo agrega los items
        #a una lista de la clase Graphics
        graphics.add_Direction(Direction)

#metodo para extraer los objetos separados por ;
def extract_Objects(pointer: list):
    #crear lista de objetos,unidos,sin espacios y separados por ;
    product_list = item_product.join(pointer).strip().split(';')
    #print (product_list)
    #recorrer lista de objetos
    for item in product_list:
        try:
            #separar posiciones por ','
            position = item.split(',')
            #la priemra posicion deber removerse el '[' y '"' y quitar espacios
            name = position[0].replace('[','').replace('"','').strip()
            #print(name)
            #segunda posicon debe removerse los espacios
            price = position[1].strip()
            #tercera posicion debe removerse el ']' y quitar espacios
            sold = position[2].replace(']','').strip()
            #queda la lista de esta forma producto1,25,33;producto2,25,33;...
            #aniadimos los datos al constructor de items
            item_products.append(Item(name, price, sold))
        except IndexError:
            item = 'null'
        #retornar lista
    return item_products

#metodo para extraer el anio y el mes
def extract_month_year(data_base: list):
    #apuntador en la lista database
    extract_pointer = data_base[0]
    #extraer lo que este antes del ':'
    while extract_pointer != ':':
        month.append(data_base.pop(0))
        extract_pointer = data_base[0]
    #parsear el nombre del mes extraido
    month_Name_Parsed = month_Name.join(month).strip()
    #extraer lo que este antes del '='
    while extract_pointer != '=':
        year.append(data_base.pop(0))
        extract_pointer = data_base[0]
    #parsear el numero del anio extraido
    year_Name_Parsed = year_Name.join(year).replace(':','').strip()
    #crear el objeto de la clase market
    markets = Market(month_Name_Parsed,year_Name_Parsed)
    #almacenar el objeto en la lista de general de ventas
    List_Of_Market.append(markets)
    #no guardar nada que este antes del '('
    while extract_pointer != '(':
        data_base.pop(0)
        extract_pointer = data_base[0]
    #reiniciar los punteros
    data_base.pop(0)
    extract_pointer = data_base[0]
    #no guardar nada que este despues de ')'
    while extract_pointer != ')':
        #almacenar los objetos separados por [];
        item_subject.append(data_base.pop(0))
        extract_pointer = data_base[0]
    #mandar los objetos para parseo
    for Item in extract_Objects(item_subject):
        #despues del parseo agrega los items
        #a una lista de la clase Market
        markets.add_Item(Item)

def load_datas():
    try:
        Tk().withdraw()
        filename = askopenfilename(filetypes = [('Files','*.data')])
        input_file = open(filename, 'r+', encoding='utf-8')
    except FileNotFoundError:
        print('Error Al Cargar El Archivo \n')
    else:
        #leer el archivo linea por linea
        for line in input_file.readlines():
            for item in line.strip():
                #por cada linea crea un objeto
                #lo almacena en la lista data_base
                data_base.append(item)
        #print(data_base)
        #mandamos a extraer el mes y el anio
        extract_month_year(data_base)
        print('Se Ha Cargado La Data Exitosamente! \n')

def load_directions():
    try:
        Tk().withdraw()
        filename = askopenfilename(filetypes = [('Files','*.lfp')])
        
        input_file = open(filename, 'r+', encoding='utf-8')
    except FileNotFoundError:
        print('Error Al Cargar El Archivo \n')
    else:
        #leer el archivo linea por linea
        for line in input_file.readlines():
            for item in line.strip():
                #por cada linea crea un objeto
                #lo almacena en la lista data_base
                directions_base.append(item)
        #print(directions_base)
        #mandamos a extraer el mes y el anio
        extract_keys(directions_base)
        print('Se Han Cargado Las Instrucciones Exitosamente! \n')

#metodo para exportar a pdf
def export_report():
    #ambiente generado por la libreria jinja2
    env = Environment(loader=FileSystemLoader('templates/'),
                      autoescape=select_autoescape(['html']))
    #se selecciona la platilla a partir de la cual se generara el reprote
    template = env.get_template('report_template.html')
    #se crea el archivo html a partir de la platilla
    html_file = open('Oficial_Report.html', 'w+', encoding='utf-8')
    html_file.write(template.render(List_Of_Market = List_Of_Market))
    html_file.close()
    #comando para iniciar automaticamente el html
    startfile('Oficial_Report.html')

#metodo para imprimir grafiacas en formato png
def export_graphics():
    for graphics in List_Of_Graphs:
        #invocando metodo para imprimir graficas
        graphics.plot_graphics()


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
            load_datas()
        elif option == '2':
            load_directions()
        elif option == '3':
            export_graphics()
        elif option == '4':
            export_report()
        elif option == '5':
            flag = False
            print('=======================')
            print('=>Ejecucion Terminada<=')
            print('=======================')
        else:
            print('Opcion Invalida!')
            print('Presione 1. Para cargar Data')
            print('Presione 2. Para cargar Instrucciones')
            print('Presione 3. Para Analizar')
            print('Presione 4. Para generar un reporte')
            print('Presione 5. Para Salir')

if __name__ == '__main__':
    main_menu()
