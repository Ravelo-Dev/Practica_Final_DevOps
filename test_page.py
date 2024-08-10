import unittest
import os

class TestRaveloDevPage(unittest.TestCase):
    def test_html_file_exists(self):
        # Verificar que el archivo HTML existe
        self.assertTrue(os.path.exists("index.html"))

    def test_html_content(self):
        # Verificar que ciertos elementos están presentes en el archivo HTML
        with open("index.html", "r", encoding="utf-8") as file:
            content = file.read()
        
        # Verifica que el título es correcto
        self.assertIn("<title>Ravelo-Dev</title>", content)
        
        # Verifica que el encabezado con tu nombre está presente
        self.assertIn("<h1 class=\"text-white font-weight-bold\">Marcos Miguel Ravelo</h1>", content)
        
        # Verifica que la sección de conocimientos está presente
        self.assertIn("<h2 class=\"text-white mt-0\">Conocimientos</h2>", content)
        self.assertIn("<li class=\"list-group-item\">Python</li>", content)

if __name__ == "__main__":
    unittest.main()
