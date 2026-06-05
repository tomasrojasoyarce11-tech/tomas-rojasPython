# while True:
#     try:
#         edad =int(input("ingrese su edad: "))

#         if edad > 0:
#             print("edad registrada: ", edad)
#             break
#         else:
#             print(" la edad debe ser mayor que 0")

#     except ValueError:
#         print("error: debe ingresar un numero")        




# while True: 
#     try:
#         nota = int(input("ingrese una nota entre el 1 y 7 "))
#         if nota >=1 and nota <= 7:
#             print("nota valida: ", nota)
#             break
#         else:
#             print("nota fuera de rango")

#     except ValueError:
#         print("error: debe ingresar una nota valida")     
    



# while True:
#     try:
#         num1=int(input("ingrese el primer numero: "))
#         num2=int(input("ingrese el segundo numero: "))
        
#         suma =num1+num2
#         print("la suma es: ", suma)
#         break

#     except ValueError:
#         print("Error: debe ingresar solo numeros")





# while True:
#     print("1.- suma")
#     print("2.- restas")
#     print("3.- multiplicacion")
#     print("4.- divicion")
#     print("5.- salir")

#     try:
#          opcion = int(input("elija una opcion: ")) 

#          if opcion ==1:
#               a= float(input("ingrese el primer numero: "))
#               b= float(input("ingrese el segundo numero: "))
#               print("resultado:", a+b)

#          elif opcion==2:        
#               a= float(input("ingrese el primer numero: "))
#               b= float(input("ingrese el segundo numero: "))
#               print("resultado:", a-b)

#          elif opcion==3:        
#               a= float(input("ingrese el primer numero: "))
#               b= float(input("ingrese el segundo numero: "))
#               print("resultado:", a*b)

#          elif opcion==4:        
#               a= float(input("ingrese el primer numero: "))
#               b= float(input("ingrese el segundo numero: "))
#               print("resultado:", a/b)

#          elif opcion==5:
#               print("prgograma finalizado")
#               break  
            
#          else:
#               print("opcion invalida")    

#     except ValueError:
#          print("Error: ingrese valores numericos")                
                   
              

import random

# numero_secreto= random.randint(1,20)

# while True:
#     try:
#         intento=int(input("Adivina el numero entre el 1 y el 20: "))

#         if intento == numero_secreto:
#             print("¡correcto!")
#             break
#         else:
#             print("incorrecto, intenta nuevamente")

#     except ValueError:
#         print("Error: ingrese un numero valido")        




# saldo= 100000

# while True:
#     print("1.-consultar saldo")
#     print("2.-retirar saldo")
#     print("3.-salir")

#     try:
#         opcion=int(input("seleccione una opcion: "))
#         if opcion == 1:
#             print("su saldo es: ", saldo)

#         elif opcion ==2:
#             monto=int(input("ingrese monto a retirar: "))

#             if monto > saldo:
#                 print("saldo insuficiente")
#             elif monto <= 0:
#                 print("el monto debe ser mayoer que 0") 
#             else:
#                 saldo = saldo - monto
#                 print("retiro exitoso")       
#                 print("saldo actual", saldo)

#         elif opcion==3:
#             print("gracias por usar el cajero")
#             break

#         else:print("opcion invalida ")

#     except ValueError:
#         print("Error: ingrese solo numeros")





# total = 0 
# cantidad = 0


# while True:

#     precio= input("ingrese precio del producto o escriba 'fin': ")
    
#     if precio.lower() == "fin":
#         break


#     try:
#         precio = float(precio)


#         if precio >0:
#             total = total+ precio
#             cantidad = cantidad+1

#         else:
#             print("el precio debe ser mayar que 0")

#     except ValueError:
#         print("Error: debe ingresar un precio valido")

# print("total vendido: ", total )
# print("cantidad de productos: ", cantidad)                    




# while True:
#     print("\n MENU")
#     print("1.- Hamburguesa")
#     print("2.- completo")
#     print("3.- bebida")
#     print("4.- salir")


#     try:
#         opcion = int(input("seleccione una opcion del menu: "))
          
#         if opcion == 1:
#             print("ha seleccionado la hamburguesa")


#         elif opcion == 2:
#             print("ha seleccionado el completo")

#         elif opcion == 3:
#             print("ha seleccionado la bebida")

#         elif opcion == 4:
#             print("gracias por venir")
#             break

#         else:
#             print("opcion invalida")


#     except ValueError:
#         print("Error: ingrese una numero ")            

    


# saldo = 50000


# while True:
#     print("1.-consultar saldo")
#     print("2.-depositar saldo")
#     print("3.-retirar")
#     print("4.-salir")


#     try:
#         opcion=int(input("seleccione una opcion: "))
#         if opcion == 1:
#             print("su saldo es: ", saldo)

#         elif opcion ==2:
#            deposito = int(input("ingrese monto a depositar: "))

#            if deposito >0:
#                saldo =saldo + deposito
#                print("deposito realizado correctamente") 
#                print("saldo actual", saldo)
#            else:
#                print("el monto  debe ser mayor que 0")   

#         elif opcion==3:
            
#             monto=int(input("ingrese monto a retirar: "))

#             if monto > saldo:
#                 print("saldo insuficiente")
#             elif monto <= 0:
#                 print("el monto debe ser mayoer que 0") 
#             else:
#                 saldo = saldo - monto
#                 print("retiro exitoso")       
#                 print("saldo actual", saldo)


#         elif opcion ==4:
#             print("gracias por usar el cajero")
#             break

#         else:print("opcion invalida ")

#     except ValueError:
#         print("Error: ingrese solo numeros")










