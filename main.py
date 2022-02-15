import matplotlib.pyplot as plt

from os import startfile
from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import List


#listas globales
data_base = []
directions_base = []
month = []
year = []
List_Of_Market = []
List_Of_Graphs = []
item_products = []
item_directions = []
item_subject = []
item_subject2 = []

#variables globales
month_Name = ''
year_Name = ''
item_product = ''
item_direction = ''

#clase Item para almacenar productos como objetos
class Item:
    def __init__(self, item_name: str, item_price: float, item_sold: int) -> None:
        self.item_name: str = str (item_name.upper())
        self.item_price: float = float (item_price)
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

        #metodo para imprimir lista en consola
    def print_dates(self):
        print('================================================')
        print('Mes : {}'.format(str(self.month_name)))
        print('Anio: {}'.format(str(self.year_name)))

        print('Cantidad de items: {}'.format(len(self.items_list)))
        
        for Item in self.items_list:
            print('Producto: {}, Precio: {}, Ventas: {}, Ganancias: {}'.format(Item.item_name,
                                                                               Item.item_price,
                                                                               Item.item_sold,
                                                                               Item.item_earnings))
        print('================================================')

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

    def print_dates2(self):
        for direction in self.instructions_list:
            print('================================================')

            print('Nombre: {}, Tipo: {}, Titulo: {}, TituloX: {}, TituloY: {}'.format(
                                                                                      direction.graph_name,
                                                                                      direction.graph_type,
                                                                                      direction.graph_title,
                                                                                      direction.graph_title_X,
                                                                                      direction.graph_title_Y)
                                                                                      )
            print('================================================')
    

    def plot_graphics(self):

        x = []
        y = []

        plt.rcdefaults()
        figB, axB = plt.subplots()
        figL, axL = plt.subplots()
        figP, axP = plt.subplots()

        for markets in List_Of_Market:
            for item in markets.items_list:
                #llenando las listas con los datos de los objetos
                x.append(item.item_name)
                y.append(item.item_sold * item.item_price)

        # Datos Gráfica de Barras
        ejeXB = x
        ejeYB = y
        # Datos Gráfica de Líneas
        ejeXL = x
        ejeYL = y
        # Datos Gráfica de pie
        ejeXP = x
        ejeYP = y
        
        for direction in self.instructions_list:
            
            if direction.graph_type.upper() == "BARRAS":
                # Datos de los ejes de la gráfica de barras, se usa función bar()   
                axB.bar(ejeXB, ejeYB) 
                # Titulos de los ejes  
                axB.set_xlabel(direction.graph_title_X, fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'blue'}) # Titulos de los ejes
                axB.set_ylabel(direction.graph_title_Y, fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'red'})

                axB.grid(axis='y', color='lightgray', linestyle='dashed')
                axB.set_title(direction.graph_title)

                figB.savefig('./GraficaBarras.png')

            elif direction.graph_type.upper() == "LINEAS":
                # Configuración de los ejes de la gráfica de lineas, se usa función plot()
                axL.plot(ejeXL, ejeYL) 
                # Titulos de los ejes
                axL.set_xlabel(direction.graph_title_X, fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'blue'})
                axL.set_ylabel(direction.graph_title_Y, fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'red'})

                axL.grid(axis='y', color='darkgray', linestyle='dashed')
                axL.set_title(direction.graph_title)

                figL.savefig('./graficaLineas.png')

            elif direction.graph_type.upper() == "PIE":
                # Configuración de los ejes de la gráfica de lineas, se usa función plot()
                axP.pie(ejeYP, labels = ejeXP, autopct="%0.1f %%") 

                # Titulos de los ejes
                axP.set_xlabel(direction.graph_title_X, fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'blue'})
                axP.set_ylabel(direction.graph_title_Y, fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'red'})

                axP.grid(axis='y', color='darkgray', linestyle='dashed')
                axP.set_title(direction.graph_title)

                figP.savefig('./graficaPie.png')
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
    directions_list = item_direction.join(pointer).split('\n')
    #print(directions_list)
    #recorrer lista de objetos
    for item in directions_list:
        #separar posiciones por ','
        position = item.split(',')
        #la priemra posicion deber removerse el 'NOMBRE' , ':' , '¿' , '"' y quitar espacios
        name = position[0].replace('Nombre','').replace(':','').replace('¿','').replace('"','').strip()
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
    print (product_list)
    #recorrer lista de objetos
    for item in product_list:
        #separar posiciones por ','
        position = item.split(',')
        #la priemra posicion deber removerse el '[' y '"' y quitar espacios
        name = position[0].replace('[','').replace('"','').strip()
        #segunda posicon debe removerse los espacios
        price = position[1].strip()
        #tercera posicion debe removerse el ']' y quitar espacios
        sold = position[2].replace(']','').strip()
        #queda la lista de esta forma producto1,25,33;producto2,25,33;...
        #aniadimos los datos al constructor de items
        item_products.append(Item(name, price, sold))
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
    year_Name_Parsed = year_Name.join(year).strip()
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
        filename = askopenfilename()
        input_file = open(filename, 'r+', encoding='utf-8')
    except FileNotFoundError:
        print('Error al cargar el archivo \n')
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
        print('Se ha cargado la data Exitosamente! \n')

def load_directions():
    try:
        Tk().withdraw()
        filename = askopenfilename()
        input_file = open(filename, 'r+', encoding='utf-8')
    except FileNotFoundError:
        print('Error al cargar el archivo \n')
    else:
        #leer el archivo linea por linea
        for line in input_file.readlines():
            for item in line.strip():
                #por cada linea crea un objeto
                #lo almacena en la lista data_base
                directions_base.append(item)
        print(directions_base)
        #mandamos a extraer el mes y el anio
        extract_keys(directions_base)
        print('Se han cargado las instrucciones Exitosamente! \n')

#metodo para imprimir datos en consola
def print_datas():
    for graphics in List_Of_Graphs:
        graphics.print_dates2()

#metodo para exportar a pdf
def export_report():
    #ambiente generado por la libreria jinja2
    env = Environment(loader=FileSystemLoader('templates/'),
                      autoescape=select_autoescape(['html']))
    #se selecciona la platilla a partir de la cual se generara el reprote
    template = env.get_template('report_template.html')
    #se crea el archivo html a partir de la platilla
    html_file = open('Oficial_Report.html', 'w+', encoding='utf-8')
    html_file.write(template.render(List_Of_Market=List_Of_Market))
    html_file.close()
    #comando para iniciar automaticamente el html
    startfile('Oficial_Report.html')

#metodo para imprimir grafiacas en formato png
def export_graphics():
    for graphics in List_Of_Graphs:
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

if __name__ == '__main__':
    main_menu()
