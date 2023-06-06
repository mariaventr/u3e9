class Vehiculo:
    def __init__(self, modelo, puertas, color, precio_base):
        self.__modelo = modelo
        self.__puertas = puertas
        self.__color = color
        self.__precio_base = precio_base

    def calcular_precio_venta(self):
        pass

    def getModelo(self):
        return self.__modelo

    def getPuertas(self):
        return self.__puertas

    def getColor(self):
        return self.__color

    def getPrecioBase(self):
        return self.__precio_base
    
    def setPrecioBase(self, precio_base):
        self.__precio_base = precio_base

class VehiculoNuevo(Vehiculo):
    def __init__(self, modelo, puertas, color, precio_base, version):
        super().__init__(modelo, puertas, color, precio_base)
        self.__version = version

    def calcular_precio_venta(self):
        gastos_patentamiento = self.getPrecioBase() * 0.1
        precio_venta = self.getPrecioBase() + gastos_patentamiento

        if self.__version == "full":
            precio_venta += self.getPrecioBase() * 0.02

        return precio_venta
    
    def getVersion(self):
        return self.__version


class VehiculoUsado(Vehiculo):
    def __init__(self, modelo, puertas, color, precio_base, marca, patente, anio, kilometraje):
        super().__init__(modelo, puertas, color, precio_base)
        self.__marca = marca
        self.__patente = patente
        self.__anio = anio
        self.__kilometraje = kilometraje

    def calcular_precio_venta(self):
        antiguedad = 2023 - self.__anio
        porcentaje_antiguedad = antiguedad * 0.01

        porcentaje_kilometraje = 0
        if self.__kilometraje > 100000:
            porcentaje_kilometraje = 0.02

        descuento = self.getPrecioBase() * (porcentaje_antiguedad + porcentaje_kilometraje)
        precio_venta = self.getPrecioBase() - descuento

        return precio_venta
    
    def getMarca(self):
        return self.__marca

    def getPatente(self):
        return self.__patente

    def getAnio(self):
        return self.__año

    def getKilom(self):
        return self.__kilometraje
