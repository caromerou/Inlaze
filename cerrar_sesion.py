from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar el controlador de Chrome
driver = webdriver.Chrome()

try:
    # Abrir la página de inicio de sesión
    driver.get("https://test-qa.inlaze.com/auth/sign-in")

    # Esperar a que el campo de correo electrónico esté presente
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(EC.presence_of_element_located((By.XPATH,
        "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/div[1]/label/following-sibling::input")))

    # Escribir el correo electrónico
    email_field.send_keys("carolinaromeroulloa@gmail.com")

    # Esperar a que el campo de contraseña esté presente
    password_field = wait.until(EC.presence_of_element_located((By.XPATH,
        "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/div[2]/app-password")))

    # Usar ActionChains para enviar la contraseña
    actions = ActionChains(driver)
    password_input = password_field.find_element(By.XPATH, ".//input")  # Campo de entrada dentro de app-password
    actions.move_to_element(password_input).click().send_keys("Ab1234567890*").perform()

    # Esperar un poco para que la contraseña se ingrese correctamente
    time.sleep(1)

    # Hacer clic en el botón de inicio de sesión
    login_button = driver.find_element(By.XPATH,
        "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/button")
    actions.move_to_element(login_button).click().perform()

    # Esperar a que la página principal cargue
    time.sleep(3)

    # Hacer clic en la foto de perfil
    profile_picture = wait.until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/app-root/app-panel-root/app-navbar/div/div[2]/div/div/label/div/img")))
    actions.move_to_element(profile_picture).click().perform()

    # Esperar a que aparezca el menú desplegable y hacer clic en "Logout"
    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/app-root/app-panel-root/app-navbar/div/div[2]/div/ul/li[3]/a")))
    actions.move_to_element(logout_button).click().perform()

    # Mensaje de confirmación
    print("Sesión cerrada exitosamente.")

    # Esperar unos segundos antes de cerrar el navegador
    time.sleep(2)

finally:
    # Cerrar el navegador
    driver.quit()
