class SistemaUsuarios:
    def __init__(self):
        self.usuarios = {}
    
    def registrar_usuarios(self, username, password):
        if username in self.usuarios: 
            return "Error: Usuario ya existe"
        self.usuarios[username] = password
        return "Usuario registrado"

    def autenticar(self, username, password):
        if username in self.usuarios and self.usuarios[username] == password:
            return "Acceso concedido"
        return "Acceso denegado"


import unittest
class TestSistemaUsuarios(unittest.TestCase):
    def setUp(self):
        # Configuración inicial: se crea una instancia de SistemaUsuarios para cada prueba
        self.sistema = SistemaUsuarios()

    def test_registrar_usuario_nuevo(self):
        # Caso: registrar un usuario nuevo exitosamente
        resultado = self.sistema.registrar_usuarios("user1", "password123")
        self.assertEqual(resultado, "Usuario registrado")
        self.assertIn("user1", self.sistema.usuarios)

    def test_registrar_usuario_existente(self):
        # Caso: intentar registrar un usuario ya existente
        self.sistema.registrar_usuarios("user1", "password123")
        resultado = self.sistema.registrar_usuarios("user1", "password456")
        self.assertEqual(resultado, "Error: Usuario ya existe")
        self.assertEqual(self.sistema.usuarios["user1"], "password123")  # Contraseña no cambia

    def test_autenticar_usuario_correcto(self):
        # Caso: autenticación exitosa con credenciales correctas
        self.sistema.registrar_usuarios("user1", "password123")
        resultado = self.sistema.autenticar("user1", "password123")
        self.assertEqual(resultado, "Acceso concedido")

    def test_autenticar_usuario_no_registrado(self):
        # Caso: intento de autenticación con un usuario no registrado
        resultado = self.sistema.autenticar("user2", "password123")
        self.assertEqual(resultado, "Acceso denegado")

    def test_autenticar_usuario_contraseña_incorrecta(self):
        # Caso: intento de autenticación con una contraseña incorrecta
        self.sistema.registrar_usuarios("user1", "password123")
        resultado = self.sistema.autenticar("user1", "wrongpassword")
        self.assertEqual(resultado, "Acceso denegado")

    def test_estado_sistema_sin_usuarios(self):
        # Caso: validar que inicialmente no hay usuarios registrados
        self.assertEqual(len(self.sistema.usuarios), 0)

if __name__ == '__main__':
    unittest.main()