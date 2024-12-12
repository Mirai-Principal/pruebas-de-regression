from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Inicializar el WebDriver
driver = webdriver.Chrome()  # Asegúrate de tener el driver correcto

# Navegar a la calculadora
driver.get("http://127.0.0.1:5000")  # URL de la calculadora

# Localizar los elementos
element1 = driver.find_element(By.ID, "number1")
element2 = driver.find_element(By.ID, "number2")
operation = Select(driver.find_element(By.ID, "operation"))
submit_button = driver.find_element(By.TAG_NAME, "button")

# Prueba: Raíz cuadrada de 16
element1.clear()
element1.send_keys("16")
element2.clear()  # No se usa el segundo número, pero se limpia
operation.select_by_value("raiz")  # Seleccionar "raiz"
esperado = "El resultado es: 4.0"
submit_button.click()

# Verificar el resultado
resultado = driver.find_element(By.TAG_NAME, "body").text
print(f"Prueba Raíz Cuadrada (16): {'Pasó' if resultado == esperado else 'Falló'}")
print(f"Esperado: {esperado}")
print(f"Obtenido: {resultado}\n")

# Cerrar el navegador
driver.quit()
