class ClinicaVeterinaria:
    def __init__(self, peso=0, nombre="", especie="", pelaje="", edad=0, sexo=""):
        self.estado_atencion = "NO REVISADO"
        self.peso = peso
        self.tamano = self.definir_tamano()
        self.nombre = nombre
        self.especie = especie  
        self.pelaje = pelaje
        self.edad = edad
        self.sexo = sexo

    def definir_tamano(self):
        if self.peso <= 10:
            return "Mascota Pequeña"
        else:
            return "Mascota Grande"

    def actualizar_estado(self):
        self.estado_atencion = "REVISADO"
        return self.estado_atencion

    def capturar_datos(self):
        self.nombre = input("Nombre de la Mascota: ")
        self.especie = input("Ingrese la raza de su mascota: ")
        self.pelaje = input("Ingrese el color del pelaje de su mascota: ")
        self.edad = int(input("Ingrese la edad de su mascota: "))
        self.peso = int(input("Ingrese el peso de su mascota en kg: "))
        self.sexo = input("Ingrese el sexo de su mascota: ")
        self.tamano = self.definir_tamano()  

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.especie}")
        print(f"Color del Pelaje: {self.pelaje}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Tamaño: {self.tamano}")
        print(f"Sexo: {self.sexo}")
        print(f"Estado de Atención: {self.estado_atencion}")

mascota = ClinicaVeterinaria()  # Se crea la instancia sin valores iniciales
mascota.capturar_datos()  # Se piden los datos al usuario
mascota.actualizar_estado()  # Cambia el estado a "REVISADO"
mascota.mostrar_datos()  # Muestra todos los datos de la mascota
