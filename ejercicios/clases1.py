class Alumno():
    """
    
    """
    def __init__(self, nombre, apellido_paterno, apellido_materno, anio, mes, dia):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.anio = anio
        self.mes = mes
        self.dia = dia

    def imprimir_info(self):
        """
        Función que permite imprimir la información del Alumno
        """
        print(self.nombre)
        print(self.apellido_paterno)
        print(self.apellido_materno)
        print(self.anio)
        print(self.mes)
        print(self.dia)

    def generar_rfc(self):
        """
        Función para generar el RFC de una persona
        """
        print("{}{}{}{}{}{}".format(self.apellido_paterno[:2],
                                    self.apellido_materno[:1],
                                    self.nombre[:1],
                                    str(self.anio)[-2:],
                                    self.mes,
                                    self.dia))


# alumno = Alumno("jorge", "mauricio", "ruvalcaba", 85, 10,25)
#
# print(alumno.nombre)
#
# alumno.nombre = "Ernesto"
#
# print(alumno.nombre)
