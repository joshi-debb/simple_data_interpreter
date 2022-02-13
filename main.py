from tkinter import Tk
from tkinter.filedialog import askopenfilename

#listas globales
data_base = []
month = []
year = []
List_Of_Market = []
item_products = []
item_subject = []

#variables globales
month_Name = ''
year_Name = ''
item_product = ''

#clase Item para almacenar productos como objetos
class Item:
    def __init__(self, item_name: str, item_price: float, item_sold: int) -> None:
        self.item_name: str = item_name
        self.item_price: float = item_price
        self.item_sold: int = item_sold

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

#metodo para extraer los objetos separados por ;
def extract_Objects(pointer: list):
    #crear lista de objetos,unidos,sin espacion y separados por ;
    product_list = item_product.join(pointer).strip().split(';')
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

def load_file():
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

def print_datas():
    for markets in List_Of_Market:
        markets.print_dates()

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
            continue
        elif option == '3':
            continue
        elif option == '4':
            continue
        elif option == '5':
            flag = False
            print('=======================')
            print('=>Ejecucion Terminada<=')
            print('=======================')
        else:
            print('Opcion Invalida!')

if __name__ == '__main__':
    main_menu()
