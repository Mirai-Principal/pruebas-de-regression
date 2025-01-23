import unittest

class Estudiantes:
    def __init__(self, id, nombre, edad, promedio):
        if not nombre:
            raise ValueError("nombre no puede ser nulo")
        if id < 0 or type(id) != int:
            raise ValueError("el id deber ser entero positivo")

        if edad < 0 or edad > 120:
            raise ValueError("la edad debe estar dentro de 0 a 120 años")

        if promedio < 0.0 or promedio > 4.0:
            raise ValueError("el promedio debe estar entre 0.0 y 4.0")

        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

# prueba N+
class TestEstudiantes( unittest.TestCase):
# Caso 1: Creación Exitosa: Valide que el constructor funcione correctamente al proporcionar datos válidos.
    def test_Creación_Exitosa(self):
        Estudiante = Estudiantes(1, "bell",20, 3)
        self.assertEqual(Estudiante.id, 1)
        self.assertEqual(Estudiante.nombre, "bell")
        self.assertEqual(Estudiante.edad, 20)
        self.assertEqual(Estudiante.promedio, 3)

# Caso 2: Nombre Inválido: Valide que se genere una excepción si el nombre es nulo o no es una cadena de texto.
    def test_Nombre_nulo_o_no_texto(self):
        with self.assertRaisesRegex(ValueError, "nombre no puede ser nulo"):
            Estudiantes(1, "", 20, 3)
        
# Caso 3: ID de Estudiante Inválido: Pruebe que el ID del estudiante sea un número entero positivo.
    def test_id_no_valido(self):
        with self.assertRaisesRegex(ValueError, "el id deber ser entero positivo"):
            Estudiantes(1.2, "bell", 20, 3)
            Estudiantes(-1, "bell", 20, 3)

# Caso 4: Edad Fuera de Rango: Valide que la edad esté dentro de un rango lógico (0-120 años).
    def test_fuera_de_rango(self):
        with self.assertRaisesRegex(ValueError, "la edad debe estar dentro de 0 a 120 años"):
            Estudiantes(1, "bell", -1, 3)
            Estudiantes(2, "bell", 121, 3)
        
# Caso 5: Promedio Inválido: Pruebe que el promedio de calificaciones esté entre 0.0 y 4.0.
    def test_promedio_valido(self):
        with self.assertRaisesRegex(ValueError, "el promedio debe estar entre 0.0 y 4.0"):
            Estudiantes(3, "bell", 10, -0.1)
            Estudiantes(4, "bell", 100, 4.1)

if __name__ == '__main__':
    unittest.main()