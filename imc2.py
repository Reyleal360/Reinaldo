print("Bienvenido hoy vamos a calcular tu indice de masa carporal  ")
peso=input("Ingrese su peso en KG  :")
peso=float(peso)
altura=input("Ingrese su altura en metros  :")
altura=float(altura)
 

imc=peso/altura **2

print(f"tu indice de masa corporal es:  {imc}")