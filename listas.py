#uso y explicacion de listas


# lista=[91,-7,44,88,-4]
# print(lista[3])

# for i in lista :
#     print(i*2)


# pokemons=["leafeon","yvisaur","metagross","psyduck","snorlax"]

# print(pokemons [2])
# print(len())



# frutas=["manzana","piña","pera","sandia",]

# for f in frutas:
#     if f [-1].lower()=="a":

# nombres = ["Diego","Martin","Adolf"]

# apellidos=["Robles","Madraso","Hitler"]

# for n  in nombres and apellidos:
#     print(n)

# print(nombres)
# print(apellidos)


# no=input("Agregue su nombre: ")
# ap=input("agregue siu apellido: ")
# nombres.append(no)
# apellidos.append(ap)

# for i in



# juguetes=["yo-yo","tetris"]

# def mostrar():
#      c=1
#      for j in juguetes:
#         print(c,".-",j) 
#      c+=1
#      print("-"*30) 


# def actualizar():
#   mostrar()
#   print("que juguete desa actualizar: ")
# act=int(input())
# nuevojuguete=input("ingrese nuevo juguete: ")
# juguetes[actualizar-1]= nuevojuguete

# def eliminar():
#     mostrar()
#     eliminar=int(input("que juguete desea eliminar: "))
#     juguetes.pop(eliminar-1)
#     print("juguete elimiado")





# while True:
#     try:
#         print("1.-agregar juguete")
#         print("2.-eliminar juguete")
#         print("3.-actualizar juguete")
#         print("4.-mostrar juguete")
#         print("5.-salir")

#     op=int(input("seleccione una opcion: "))

#     match op:
#       case 1:
#        ju=input("agregue un juguete")
#        juguetes.append(ju)

#       case 2: 
#          eliminar()
#       case 3:   
#         actualizar()
                    
#       case 4: 
#         mostrar()

#       case 5:
#          print("salir")
#          break
#       case _:
#           print("opcion invalida")    
#     except Exception as e:    
    
    
numeros=int(input("ingrese numeros enteros separados por espacios: ")) 
listanumeros=numeros.split()
listaNumerosInt=[]
pares=[]
impares=[]


for n in listanumeros:

    listaNumerosInt.append(int(n))
    print(n)


for hh in listaNumerosInt:
    if hh%2==0:
        pares.append(hh)
    else:
        impares.append(hh)

print(f"Los numeros pares son: {pares}") 
print(f"Los numeros impares son: {impares}")       


    




    


















