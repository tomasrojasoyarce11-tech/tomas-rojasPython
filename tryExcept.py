#ejemplo de uso de try except



# while True:
#     try:
#         num=int(input("ingrese un numero: "))
#         break
#     except:
#         print("solo numeros enteros")
        




# op=0
# total=0



# while op!=4:



#     print("1.- PC $500.000")
#     print("2.- LGTV 55 pulgadas $450.000")
#     print("3.- Microondas Mademsa $100.000")
#     print("4.- Salir")
#     print("Seleccione una opcion")
#     op=int(input())

#     match op:
            
#             case 1:

#                 print("El total a pagar es ",500000*1.19 )
#                 total+=500000*1.19

#             case 2:

#                 print("El total a pagar es ",450000*1.19 )
#                 total+=450000*1.19

#             case 3:

#                 print("El total a pagar es ",100000*1.19 )
#                 total+=100000*1.19

#             case 4:

#                 print("Saliendo")
#                 print("El total a pagar es", total)

#             case _:

#                 print("Opción inválida")


# print("ingrese 3 notas")
# total=0

# for i in range (3):
#     n=float(f"ingrese la nota {i+1}: ")
#     total+=n
# prom=total/3
# print(f"el promedio es {prom}")


   

# while True:
#     try:
#         canP=int(input("que cantidad de pasajes desea vender: "))
#     except Exception as e:
#         TotalIngresos = 0
 
#     for i in range(canP):
#         while True:
#             try:
#                 pasaje=int(input(f"ingrese el precio del pasaje:  {i+1}")) 

#             except ValueError as e:
#                 print("solo valores enteros, error: ", e)

#     print(f"el total de los pasajes es: {TotalIngresos}")

# bliviano=0
# bnormales=0
    

# for i in range(canP):
#     while True:
#         try:
#             bulto=int(input(f"ingrese el peso del bulto {i+1} (en kg): "))
#             if bulto<=5:
#                 blivianos+=1
#             else:
#                 bnormales+=1
#             break
#         except ValueError as e:
#             print("solo valoores enteros, error: ", e) 

# while True:
#     while True:
#         try:
#             canP=int(input(f"ingrese el bulto {i+1}: "))
#             break
#         except ValueError as e:
#             print("solo valores enteros, error: ", e)

       

# print(f"bultos livianos: {bliviano*1000}")
# print(f"bultos livianos: {bnormal*2000}")
# print(f"bultos livianos: {bliviano*1000/bnormales}")






            




















