""" Diccionarios (dict) en Python: 
Son estructuras de datos que almacenan pares de clave-valor."""

my_dict = dict()  # Crear un diccionario vacío usando el constructor dict()
my_dict2 = {}  # Crear un diccionario vacío usando llaves {}
print("----Diccionarios-----")
print(type(my_dict))  # Tipo de dato - dict

"""Diccionarios - mas conocido como mapas o hash en otros lenguajes de programacion
Los diccionarios no son estructuras ordenadas, no tienen indice, no se puede acceder 
a sus elementos por posicion. Se accede a los elementos por su clave (key)"""

dictionary1 = {
    "nombre": "Victor", 
    "apellido": "Rodriguez", 
    "edad": 21,
    }

dictionary = {
    "nombre": "Victor", 
    "apellido": "Rodriguez", 
    "edad": 21,
    "lenguajes": {"Python", "Java", "C++"} # viene a ser set
    }  # Diccionario con elementos

print(dictionary)
print(len(dictionary))  # Longitud del diccionario - 4
print(dictionary["nombre"])  # Acceder al valor de la clave "nombre" - Victor
dictionary["edad"] = 22  # Modificar el valor de la clave "edad"
print(dictionary["edad"])  # Acceder al valor de la clave "edad" - 22
print(dictionary.keys())  # Obtener todas las claves del diccionario
print(dictionary.values())  # Obtener todos los valores del diccionario
print(dictionary.items())  # Obtener todos los pares clave-valor del diccionario
print(dictionary )
print(dictionary["lenguajes"])  # Acceder al valor de la clave "lenguajes" - {'Python', 'Java', 'C++'}

dictionary["direccion"] = "Calle Falsa 123"  # Agregar un nuevo par clave-valor
print(dictionary)

del dictionary["direccion"]  # Eliminar el par clave-valor con clave "direccion"
print(dictionary)

"""comprobar si un elemento existe en el Diccioario"""
print( "nombre" in dictionary)

# crear diccioario vacio
my_new_dict = dictionary.fromkeys(("Nombre", "edad"))
print(my_new_dict)

my_new_dict["Nombre"] = "Jose"
print(my_new_dict)