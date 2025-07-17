opcion = 0
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1TB', 'Intel Core i5', 'Nvidia GTX1050'],
            '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '8GB', 'HDD', '1TB', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'HDD', '1TB', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['lenovo', 14, '6GB', 'HDD', '1TB', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['lenovo', 15.6, '8GB', 'HDD', '1TB', 'AMD Ryzen 7', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'HDD', '1TB', 'AMD Ryzen 3', 'Nvidia GTX1050'],

             }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
         }



def stock_marca(marca):
    diccionariofiltrado={}
    for clave, productos in stock:
        if stock [1] == stock [1]:
            return diccionariofiltrado 



def busqueda_precio(p_min, p_max):
    diccionariofiltrado={}
    for clave, stock in productos.items():
         if p_min <= stock[clave] <= p_max:
              diccionariofiltrado[1]=stock
              return diccionariofiltrado



def filtrar_stock_marca():
     marca=input("Ingrese la marca a consultar: ") 
     for clave, stock in productos.items():
            print(f"El stock es de {stock[1]}")
            return 

 

def filtrar_busqueda_precio(): 
        try:
          p_min=int(input("Ingrese el precio minimo: "))
          p_max=int(input("Ingrese el precio maximo: "))
          for clave, stock in productos.items():
                if p_min <= stock[1] <= p_max:
                     print(f"Los notebooks entre los precios que consultas son: {productos[0]} -- {stock[3]}")                

        except ValueError:
             print("Debe ingresar valores enteros!!")



while True:
        try:
            print("***MENU PRINCIPAL***")
            print("1. Stock marca")
            print("2. Busqueda por precio") 
            print("3. Actualizar precio")
            print("4. Salir")
            match = opcion=int(input("Ingrese opcion: ")) 
            case = "1"
            filtrar_stock_marca()
            case = "2"
            filtrar_busqueda_precio()
            case = "3"
            pass
            case = "4"
            print ("Programa finalizado.")
        except ValueError:
             print("Debe seleccionar una opción válida!!")  