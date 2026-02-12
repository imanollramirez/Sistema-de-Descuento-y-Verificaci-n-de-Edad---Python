# Sistema de descuentos para un centro deportivo.
# Imanol Ramírez
"""
Reglas:
- Si un usuario es menor de 18 años, debe recibir un descuento del 20%
en la membresía. Si tiene entre 18 y 25 años, recibirá un descuento del 10%.

- Si tiene más de 25 años, no recibirá descuento.

- Si el usuario tiene más de 60 años, deberá pagar un precio reducido,
pero solo si es miembro del centro.

- Si el usuario no es miembro, se le cobrará el precio completo.

- Si el usuario no proporciona su edad o estado de membresía
(es decir, los campos están vacíos o no se proporcionan),
se debe mostrar un mensaje de error.

""" 
print("****************************************")
print("         B I E N V E N I D O / A        ")
print("           Calcular membresía           ")
print("**************************************")

name = input('Ingrese su nombre: ')

age = input(f'¡Un gusto atenderle {name}!, porfavor ingrese su edad: ')

member = input(f'Es miembro del centro (S/ N): ')

if(member.lower() == 's'):
    member = True
elif(member.lower() == 'n'): 
    member = False
else:
    member = None

#Validaciones
#1
if(name == None or age == 0 or member == None):
    print("Ingrese lo datos, porfavor.")
else:
    age = int(age)
    if(age < 18 and member):
        print(f'{name}, su descuento en la membresía es de 20%.')  
    elif(age >= 18 and age <= 25 and member):
        print(f'{name}, su descuento en la membresía es de 10%.')  
    elif(age > 60 and member):
        print(f'{name}, pague un cantidad reducida.')  
    elif(age > 25):
        print(f'{name}, le informamos que no aplican descuentos para su membresía, pague el total.')  
    elif(not member):
        print(f'{name}, no aplican descuentos.')

