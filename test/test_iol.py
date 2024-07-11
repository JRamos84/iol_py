import unittest
import os
from iol_py_package_joseph0001.iol_py import IOL
from dotenv import load_dotenv
load_dotenv()

class TestIOL(unittest.TestCase):
    def setUp(self):
        # Configurar las variables de entorno
        usuario = os.environ.get('USUARIO')
        clave = os.environ.get('CLAVE')

        # Crear una instancia de IOL usando las variables de entorno configuradas
        self.iol = IOL(usuario, clave)

    def test_obtener_bearer(self):
        bearer = self.iol.obtener_bearer()
        self.assertIn('Authorization', bearer)

    def test_estado_de_cuenta(self):
        self.assertIsNone(self.iol.obtener_estado_de_cuenta())

    def test_portafolio(self):
        df_portafolio = self.iol.mi_portafolio()
        self.assertIsNotNone(df_portafolio)

    def test_operaciones(self):
        df_operaciones = self.iol.mis_operaciones()
        self.assertIsNotNone(df_operaciones)

    def test_hist_precios(self):
        hist_precios = self.iol.hist_precio()
        self.assertIsNotNone(hist_precios)

if __name__ == '__main__':
    unittest.main()
