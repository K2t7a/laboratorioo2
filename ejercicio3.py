class Vehiculo:
    def __init__(self):
        self.marca_auto = input("Ingrese la marca del auto: ")
        self.modelo_auto = input("Ingrese el modelo del auto: ")
        self.anio_auto = input("Ingrese el año del auto: ")
        self.color_auto = input("Ingrese el color del auto: ")
        self.tipo_combustible_auto = input("Ingrese el tipo de combustible (Gasolina/Diesel/Eléctrico): ")
        self.transmision_auto = input("Ingrese el tipo de transmisión (Automática/Manual): ")
        self.motor_auto = input("Ingrese el tipo de motor (e.g., 1.8L): ")
        self.origen_auto = input("Ingrese el origen del auto (Nacional/Importado): ")
        self.precio_compra_auto = float(input("Ingrese el precio de compra del auto: "))
        self.precio_venta_auto = self.calcular_precio_venta()
        self.numero_ruedas = 4  
        self.capacidad_pasajeros = 5  

    def calcular_precio_venta(self):
        return self.precio_compra_auto * 1.4

    def mostrar_datos(self):
        print("\nCaracterísticas del vehículo:")
        print(f"Marca: {self.marca_auto}")
        print(f"Modelo: {self.modelo_auto}")
        print(f"Año: {self.anio_auto}")
        print(f"Color: {self.color_auto}")
        print(f"Tipo de Combustible: {self.tipo_combustible_auto}")
        print(f"Transmisión: {self.transmision_auto}")
        print(f"Motor: {self.motor_auto}")
        print(f"Origen: {self.origen_auto}")
        print(f"Número de Ruedas: {self.numero_ruedas}")
        print(f"Capacidad de Pasajeros: {self.capacidad_pasajeros}")
        print(f"Precio de Compra: ${self.precio_compra_auto:.2f}")
        print(f"Precio de Venta: ${self.precio_venta_auto:.2f}")

print("Registro del primer vehículo:")
vehiculo1 = Vehiculo()
vehiculo1.mostrar_datos()

print("\nRegistro del segundo vehículo:")
vehiculo2 = Vehiculo()
vehiculo2.mostrar_datos()
