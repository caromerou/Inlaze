from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar el controlador de Chrome
driver = webdriver.Chrome()

# Abrir la página de inicio de sesión
driver.get("https://test-qa.inlaze.com/auth/sign-in")

# Esperar a que el campo de correo electrónico esté presente
wait = WebDriverWait(driver, 10)
email_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/div[1]/label/following-sibling::input")))

# Escribir el correo electrónico
email_field.send_keys("carolinaromeroulloa@gmail.com")

# Esperar a que el campo de contraseña esté presente
password_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/div[2]/app-password")))

# Usar ActionChains para hacer clic en el campo de contraseña y enviar la contraseña
actions = ActionChains(driver)
actions.move_to_element(password_field).click().perform()  # Hacer clic en el campo de contraseña
password_input = password_field.find_element(By.XPATH, ".//input")  # Encontrar el campo de entrada dentro de app-password
actions.move_to_element(password_input).click().send_keys("Ab1234567890*").perform()  # Enviar la contraseña
time.sleep(2)  # Esperar un poco para que la contraseña se ingrese correctamente

# Confirmar si el valor se ingresó correctamente
print("Valor del campo de contraseña:", password_input.get_attribute("value"))

# Encontrar y hacer clic en el botón de inicio de sesión
login_button = driver.find_element(By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/button")
actions.move_to_element(login_button).click().perform()
time.sleep(5)  # Esperar unos segundos para observar el inicio de sesión

# Cerrar el navegador
driver.quit()
