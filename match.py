#explicion y uso de match

# op=0
# total=0

# while op!=4:

#     print("1.- Pc ryzen $800000")
#     print("2.- LGTV $400000")
#     print("2.- Parlante JBl Piure Sound 90000")
#     print("4.- salir")
#     print("seleccione una opcion")
#     op=int(input())

    # match op:
    #     case 1:
    #         print ("tiene que pagar ", 800000*1.19)
    #         total+=800000*1.19

    #     case 2:
    #        print("tiene que pagar: ", 450000*1.19 )
    #        total+=450000*1.19

    #     case 3:
    #         print("htiene que pagar: ",90000*1.19) 
    #         total+=90000*1.19

    #     case 4:
    #         print("saliendo")
    #         print(f"el total a pagar con iva es: {round(total,2)}")        

    #     case _:
    #         print("opcion invalida")  
             





# op=0
# while op!=5:

#     print("1.-suma")
#     print("2.-resta ")
#     print("3.-multiplicacion")
#     print("4.-divicion")
#     print("5.-salir")
#     print("seleccione una opcion")

#     op=int(input())
#     match op:
#         case 1:
            
#             n1=int(input("ingrese el primer  numero: "))
#             n2=int(input("ingrese el segundo numero: "))
#             print(f"la suma es: {n1+n2}")

#         case 2:
           
#             n1=int(input("ingrese el primer  numero: "))
#             n2=int(input("ingrese el segundo numero: "))
#             print(f"la resta es: {n1-n2}")

#         case 3:
#             n1=int(input("ingrese el primer  numero: "))
#             n2=int(input("ingrese el segundo numero: "))
#             print(f"la multiplicacion es: {n1*n2}") 
            

#         case 4:

#             n1=int(input("ingrese el primer  numero: "))
#             n2=int(input("ingrese el segundo numero: "))
#             print(f"la divicion es: {n1/n2}") 

#         case 5:
#            print("saliendo")           

#         case _:
#             print("opcion invalida")  
             

import random
# num =random.randint(1,9)

# while abs(-3)!=num:
#     print(num)
#     time.sleep(1)
#     num =random.randint(1,9)



# n1=int(input("ingrese el valor de limite inferior: "))
# n2=int(input("ingrese el valor de limite superior: "))
# #validar  que el limite superior sea mayor que el limite inferior
# #hay un limite qe rompe el deseo

# while n1>=n2:
#     print("error, el limite superior debe se mayor ")
#     n2=int(input("ingrese el valor de limite superior: "))  

# num=random.randint(n1,n2)
# print(num)
import time

lata = 0
plancha =0


pecesCap=random.randint(10,20)
print(f"El total d peces capturados es: {pecesCap}")

peso=random.randint(300,3000)

if peso <= 800:
    lata=+1
elif peso >= 801 and peso <= 3000:
    plancha=+1
else:
    print("peso invaido")        

time.sleep(2)
print(f"El total de peces en lata son: {lata}")
time.sleep(2)
print(f"El total de peces en plancha son {plancha}")



#forma 2

# peces=random.randint(10,20)
# p_lata=0
# p_plancha=0
# print(f"capturados {peces} peces ")
# time.sleep(2)

# for p in range(peces):
#  pez=random.randint(257,3000)

# if pez<=800:
#  p_lata=+1
# else:
#  p_plancha=+1

#  print(f"")




# peso =int(input("ingrese l peso del producto"))

# sodio=int(input("ingrese el porentaje de sopdio: "))

# mercado=int(input("ingrese el mercado del producto 1.- Nacional - 2.-internacional")) 

# if peso <500:
  
#   lata="lata normal"

# elif 501<peso<1500:
  
#   lata="lata mediana"

# else:
  
#   lata="lata grande"

#   if sodio<5:
   
#    sod=""

#   elif 5<=sodio<=8:
   
#    sod="lata especial"

#   else:
   
#    sod="acorazada" 

#    if mercado ==1:

#     sticker=""

#    else:

#     sticker="con stcker saniario"

#     print(f"{lata} {sod} {mercado}")

  





































