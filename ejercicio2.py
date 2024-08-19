class Papeleria:
    def __init__(self, boligrafo="", carpeta="", precio_compra=0):
        self.boligrafo = boligrafo
        self.carpeta = carpeta
        self.marca_boligrafo = "Escribano"
        self.marca_carpeta = "Archivador"
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.25  # 25% de ganancia sobre el precio de compra

    def recibir_datos(self):
        tipo_boligrafo = input("Seleccione el tipo de bolígrafo (1: Tinta Azul, 2: Tinta Negra, 3: Tinta Roja): ")
        if tipo_boligrafo == "1":
            self.boligrafo = "Tinta Azul"
        elif tipo_boligrafo == "2":
            self.boligrafo = "Tinta Negra"
        elif tipo_boligrafo == "3":
            self.boligrafo = "Tinta Roja"
        else:
            print("Opción no válida.")
        
        tipo_carpeta = input("Seleccione el tipo de carpeta (A: Cartón, B: Plástico): ").upper()
        if tipo_carpeta == "A":
            self.carpeta = "Carpeta de Cartón"
        elif tipo_carpeta == "B":
            self.carpeta = "Carpeta de Plástico"
        else:
            print("Opción no válida.")
        
        self.precio_compra = float(input("Ingrese el precio de compra del artículo: "))
        self.precio_venta = self.calcular_precio_venta()

    def mostrar_datos(self):
        print("\nDetalles del artículo registrado:")
        print(f"Marca de Bolígrafo: {self.marca_boligrafo}")
        print(f"Tipo de Bolígrafo: {self.boligrafo}")
        print(f"Marca de Carpeta: {self.marca_carpeta}")
        print(f"Tipo de Carpeta: {self.carpeta}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")


articulo1 = Papeleria()
articulo1.recibir_datos()
articulo1.mostrar_datos()

articulo2 = Papeleria()
articulo2.recibir_datos()
articulo2.mostrar_datos()
