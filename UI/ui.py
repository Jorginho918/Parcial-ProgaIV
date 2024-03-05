import os
from API.api import soil_variables


def menu():
    print("Que desea hacer?")
    print("1. Buscar")
    print("2. Salir")
    
    
def get_option():
    while True:
        op = int(input("Ingrese un valor: "))

        if op != 1 and op != 2:
            print("\n\tOpcion no valida\n")
            continue
        return op
        

def get_params():
    params = {}
    params_name = ("departamento", "municipio", "cultivo", "limit")
    print("\n\tIngrese los valores correspondientes\n")

    for param in params_name:
        while True:
            value = input(f"Ingrese el valor de {param}: ")
            if len(value) == 0:
                print("\t\n#######  Debe ingresar un valor #######\n")
            else:
                break
        if param == "limit":
            while True:
                try:
                    if int(value) > 1000:
                        print("Se tomará como limite 1000 porque el ingresado lo sobrepasa")
                        value = "1000"
                    break
                except ValueError as error:
                    print(f"Error: {error}\n\t\tIntenta de nuevo")
        params[param] = value

    return params
    
    
def print_table(data, medians):
    clean_terminal()
    
    columns_table = ["departamento", "municipio", "cultivo", "topografia"]
    soil_variable_table = ["ph", "potasio", "fosforo"]

    print(f"{' ':>18}", end="")
    for column_name in columns_table:
        print(f"{column_name.capitalize():<15}", end="")
    print("\n", "=" * 125)
    
    print(f"{' ':>18}", end="")
    for value in data.iloc[0][:4]:
        print(f"{value:<15}", end="")
    print("\n", "=" * 125)
    
    print(f"\n\n{'Medianas':>62}")
    print("\n", "=" * 125)
    
    print(f"{' ':>37}", end="")
    for column_name in soil_variable_table:
        print(f"{column_name.capitalize():<17}", end="")
    
    print(f"\n{' ':>37}", end="")
    
    for soil_variable in soil_variables:
        print(f"{medians[soil_variable]:.3f}", " " * 11, end="")

    print("\n\n")
    

def clean_terminal():
    os.system("cls" if os.name == "nt" else "clear")