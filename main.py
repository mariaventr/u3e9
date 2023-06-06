from claseListaVehiculo import Concesionaria
from claseVehiculo import Vehiculo, VehiculoNuevo, VehiculoUsado
import unittest
from test import TestVehiculos


def menu():
    concesionaria = Concesionaria()
    # Cargar vehículos desde archivo
    concesionaria.cargar_vehiculos_desde_archivo("vehiculos.json")
    # Menú de opciones
    while True:
        print("\n=== MENÚ ===")
        print("1. Insertar un vehículo en la colección en una posición determinada.")
        print("2. Agregar un vehículo a la colección.")
        print("3. Mostrar qué tipo de objeto se encuentra almacenado en una posición de la lista.")
        print("4. Modificar el precio base de un vehículo usado por patente y mostrar el precio de venta.")
        print("5. Mostrar los datos, incluido el importe de venta, del vehículo más económico.")
        print("6. Mostrar los datos de todos los vehículos en venta.")
        print("7. Almacenar los objetos de la colección en el archivo 'vehiculos.json'.")
        print("0. Salir.")

        opcion = input("Ingrese el número de opción deseada: ")

        if opcion == "1":
            modelo = input("Ingrese el modelo del vehículo: ")
            puertas = input("Ingrese la cantidad de puertas: ")
            color = input("Ingrese el color: ")
            precio_base = float(input("Ingrese el precio base de venta: "))
            usado = input("¿El vehículo es usado? (S/N): ")
            if usado.upper() == "S":
                patente = input("Ingrese la patente del vehículo: ")
                marca = input("Ingrese la marca del vehículo: ")
                anio = int(input("Ingrese el año del vehículo: "))
                kilometraje = float(input("Ingrese el kilometraje del vehículo: "))
                vehiculo = VehiculoUsado(modelo, puertas, color, precio_base, marca, patente, anio, kilometraje)
                posicion = int(input("Ingrese la posición en la que desea insertar el vehículo: "))
                concesionaria.insertar_vehiculo(vehiculo, posicion)
                print("Vehículo insertado correctamente.")
            else:
                version = input("Ingresar version: ")
                vehiculo = VehiculoNuevo(modelo, puertas, color, precio_base, version)
                posicion = int(input("Ingrese la posición en la que desea insertar el vehículo: "))
                concesionaria.insertar_vehiculo(vehiculo, posicion)
                print("Vehículo insertado correctamente.")

        elif opcion == "2":
            modelo = input("Ingrese el modelo del vehículo: ")
            puertas = input("Ingrese la cantidad de puertas: ")
            color = input("Ingrese el color: ")
            precio_base = float(input("Ingrese el precio base de venta: "))

            tipo_vehiculo = input("Ingrese el tipo de vehículo (nuevo/usado): ")
            if tipo_vehiculo == "nuevo":
                version = input("Ingrese la versión del vehículo (base/full): ")
                vehiculo = VehiculoNuevo(modelo, puertas, color, precio_base, version)
            elif tipo_vehiculo == "usado":
                marca = input("Ingrese la marca del vehículo: ")
                patente = input("Ingrese la patente del vehículo: ")
                anio = int(input("Ingrese el año del vehículo: "))
                kilometraje = float(input("Ingrese el kilometraje del vehículo: "))
                vehiculo = VehiculoUsado(modelo, puertas, color, precio_base, marca, patente, anio, kilometraje)
            else:
                print("Tipo de vehículo inválido.")
                continue

            concesionaria.agregar_vehiculo(vehiculo)
            print("Vehículo agregado correctamente.")

        elif opcion == "3":
            posicion = int(input("Ingrese la posición de la lista que desea consultar: "))
            concesionaria.mostrar_tipo_vehiculo_en_posicion(posicion)

        elif opcion == "4":
            patente = input("Ingrese la patente del vehículo usado: ")
            nuevo_precio_base = float(input("Ingrese el nuevo precio base: "))
            concesionaria.modificar_precio_base_por_patente(patente, nuevo_precio_base)

        elif opcion == "5":
            concesionaria.mostrar_datos_vehiculo_mas_economico()

        elif opcion == "6":
            concesionaria.mostrar_datos_vehiculos()

        elif opcion == "7":
            concesionaria.almacenar_vehiculos_en_archivo("vehiculos.json")
            print("Vehículos almacenados en el archivo 'vehiculos.json' correctamente.")

        elif opcion == "0":
            break

        else:
            print("Opción inválida. Intente nuevamente.")

    print("¡Hasta luego!")

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVehiculos)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    run_tests()
    #menu()