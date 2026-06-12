peliculas={
   1:"Nombre",
   2:"Boleto",
   3:"Precio"
}



def cine():
   while True:
      try:
         print("-"*20)
         print("1.- cuantas entradas desea comprar ")
         print("2.- seleccione una pelicula de la lista")
         print("3.- ")
         print("4.- Mostrar Vegetal")
         print("6.- crear boleta y salir")
         op=int(input("Seleccione una opcion: "))
         match op:
               case 1:
                  agregarVegetales()
               case 2:
                  eliminarVegetal()
               case 3:
                  actualizarVegetal()
               case 4:
                  mostrarVegetales()
               case 5:
                  comprar()
                  print(carrito)
               case 6:
                  Boleta_salir()   
                  break
               case _:
                    print("Opcion invalida")  
      except Exception as e:
         print("Error:",e)

vegetalesMenu()

##Diccionario con diccionarios
productosDicc={
   1:{"nombre": "Micheal Jackson", "precio": 3000},
   2:{"nombre": "Scary Movie", "precio": 1500},
   3:{"nombre": "", "precio": 1200}
}

carrito = []
productosDicc[4]={"nombre": "Piña", "precio": 3500}



def agregarProducto():
   print("Cual es el nombre del producto?: ")
   nombre = input()
   print("cual es el precio?: ")
   precio = int(input())
   nuevoKey=list(productosDicc.keys())
   nuevoKey.sort()
   productosDicc[nuevoKey[-1]+1]= {
      "nombre": nombre,
      "precio": precio
      }

def MostrarProducto():
   print("-"*40)
   for key, producto in productosDicc.items():
      print(f"{key}.-{producto['nombre']} - ${producto['precio']}")

def eliminarProducto():
   MostrarProducto()
   borrar=int(input("Cual Producto borrará?: "))
   if borrar in productosDicc:
      del productosDicc[borrar]
      print("producto eliminado")
   else:
      print("producto no encontrado")

def actualizarProducto():
   MostrarProducto()
   num=int(input("Que producto desea actualizar?: "))

   if num in productosDicc.keys():
    
    nombre=input("Cual es el nombre nuevo?: ")
    precio=int(input("Cual es el precio nuevo?: "))

    productosDicc[num]={
       "nombre": nombre,
       "precio": precio
         
   }
    print("producto actualizado")
   else:
      print("producto no existente")

def comprar():
   while True:
      MostrarProducto()

      try:
         comprar = int(input("ingrese el producto a comprar: "))
   
         if comprar in productosDicc.keys():
            carrito.append(productosDicc[comprar])
            print(f"producto agregado")
         else:
            print("producto no encontrado")
      except Exception as e:
         print("debe ingresar un numero valido")

def Boleta_salir():
   total=0

   print("-"*30, "0", "-")
   print("bienvenido al minimarket minoria")
   for producto in carrito:
     print(f"{producto["nombre"]}__${producto["precio"]}")   
     print("-"*30, "0", "-"*30) 
     print(f"El total neto es: {round(total*1.19)}")
     print("adios minoria gracias por venir ")











