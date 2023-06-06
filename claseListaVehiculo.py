import json
from claseVehiculo import Vehiculo, VehiculoNuevo, VehiculoUsado


class Concesionaria:
    def __init__(self):
        self.vehiculos = []

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.vehiculos):
            raise StopIteration
        vehiculo = self.vehiculos[self.index]
        self.index += 1
        return vehiculo

    def cargar_vehiculos_desde_archivo(self, archivo):
        with open(archivo) as file:
            data = json.load(file)

        for vehiculo_data in data:
            if vehiculo_data["tipo"] == "vehiculonuevo":
                vehiculo = VehiculoNuevo(
                    vehiculo_data["modelo"],
                    vehiculo_data["puertas"],
                    vehiculo_data["color"],
                    vehiculo_data["precio_base"],
                    vehiculo_data["version"]
                )
            elif vehiculo_data["tipo"] == "vehiculousado":
                vehiculo = VehiculoUsado(
                    vehiculo_data["modelo"],
                    vehiculo_data["puertas"],
                    vehiculo_data["color"],
                    vehiculo_data["precio_base"],
                    vehiculo_data["marca"],
                    vehiculo_data["patente"],
                    vehiculo_data["anio"],
                    vehiculo_data["kilometraje"]
                )
            else:
                continue

            self.vehiculos.append(vehiculo)
    
    def insertarVehiculo(self, posicion, vehiculo):
        if isinstance(vehiculo, Vehiculo):  # Verificar si es un objeto de tipo Vehiculo
            self.vehiculos.insert(posicion, vehiculo)
        else:
            print("Error: El objeto no es una instancia de la clase Vehiculo")

    def insertar_vehiculo(self, vehiculo, posicion):
        self.vehiculos.insert(posicion, vehiculo)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrarElemento(self, posicion):
        if posicion < 0 or posicion >= len(self.vehiculos):
            raise IndexError("La posición dada no es válida para mostrar el elemento")
        return self.vehiculos[posicion]

    def mostrar_tipo_vehiculo_en_posicion(self, posicion):
        if 0 <= posicion < len(self.vehiculos):
            tipo = type(self.vehiculos[posicion]).__name__
            print(f"Tipo de objeto en la posición {posicion}: {tipo}")
        else:
            print("Posición inválida.")

    def modificar_precio_base_por_patente(self, patente, nuevo_precio_base):
        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, VehiculoUsado) and vehiculo.getPatente() == patente:
                vehiculo.setPrecioBase(nuevo_precio_base)
                print(f"Precio base modificado para el vehículo con patente {patente}.")
                return

        print(f"No se encontró un vehículo usado con la patente {patente}.")

    def mostrar_precio_venta_por_patente(self, patente):
        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, VehiculoUsado) and vehiculo.getPatente() == patente:
                precio_venta = vehiculo.calcular_precio_venta()
                print(f"El precio de venta del vehículo con patente {patente} es: {precio_venta}")
                return

        print(f"No se encontró un vehículo usado con la patente {patente}.")

    def mostrar_datos_vehiculo_mas_economico(self):
        if len(self.vehiculos) == 0:
            print("No hay vehículos en la concesionaria.")
            return

        vehiculo_mas_economico = min(self.vehiculos, key=lambda v: v.calcular_precio_venta())
        precio_venta = vehiculo_mas_economico.calcular_precio_venta()

        print("Datos del vehículo más económico:")
        print(f"Modelo: {vehiculo_mas_economico.getModelo()}")
        print(f"Puertas: {vehiculo_mas_economico.getPuertas()}")
        print(f"Color: {vehiculo_mas_economico.getColor()}")
        print(f"Precio de venta: {precio_venta}")

    def mostrar_datos_vehiculos(self):
        if len(self.vehiculos) == 0:
            print("No hay vehículos en la concesionaria.")
            return

        print("Datos de todos los vehículos en venta:")
        for vehiculo in self.vehiculos:
            precio_venta = vehiculo.calcular_precio_venta()
            print(f"Modelo: {vehiculo.getModelo()}")
            print(f"Puertas: {vehiculo.getPuertas()}")
            print(f"Importe de venta: {precio_venta:.2f}")
            print("---")

    def almacenar_vehiculos_en_archivo(self, archivo):
        vehiculos_data = []

        for vehiculo in self.vehiculos:
            vehiculo_data = {
                "tipo": type(vehiculo).__name__.lower(),
                "modelo": vehiculo.getModelo(),
                "puertas": vehiculo.getPuertas(),
                "color": vehiculo.getColor(),
                "precio_base": vehiculo.getPrecioBase()
            }

            if isinstance(vehiculo, VehiculoNuevo):
                vehiculo_data["version"] = vehiculo.getVersion()
            elif isinstance(vehiculo, VehiculoUsado):
                vehiculo_data["marca"] = vehiculo.getMarca()
                vehiculo_data["patente"] = vehiculo.getPatente()
                vehiculo_data["anio"] = vehiculo.getAnio()
                vehiculo_data["kilometraje"] = vehiculo.getKilom()

            vehiculos_data.append(vehiculo_data)

        with open(archivo, "w") as file:
            json.dump(vehiculos_data, file, indent=2)
