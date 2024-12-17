from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Inicializa el navegador
driver = webdriver.Chrome()

# Abre la página
driver.get("https://test-qa.inlaze.com/auth/sign-up")

# Espera hasta que el campo Full Name sea visible y clickeable
full_name = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[1]/label/span")))

# Asegura que el campo esté visible y lo selecciona
driver.execute_script("arguments[0].scrollIntoView();", full_name)  # Asegura que el campo esté visible
actions = ActionChains(driver)
actions.move_to_element(full_name).click().send_keys("Carolina Romero").perform()

# Pausa para ver el campo completo
time.sleep(2)

# Espera hasta que el campo Email sea visible y clickeable
email = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[2]/label")))
driver.execute_script("arguments[0].scrollIntoView();", email)  # Asegura que el campo esté visible
actions.move_to_element(email).click().send_keys("carolinaromeroulloa@gmail.com").perform()

# Pausa para ver el campo completo
time.sleep(2)

# Espera hasta que el campo Password sea visible y clickeable
password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[3]/app-password")))
driver.execute_script("arguments[0].scrollIntoView();", password)  # Asegura que el campo esté visible
actions.move_to_element(password).click().send_keys("Ab1234567890*").perform()

# Pausa para ver el campo completo
time.sleep(2)

# Espera hasta que el campo Repeat Password sea visible y clickeable
repeat_password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[4]/app-password")))
driver.execute_script("arguments[0].scrollIntoView();", repeat_password)  # Asegura que el campo esté visible
actions.move_to_element(repeat_password).click().send_keys("Ab1234567890*").perform()

# Pausa para ver el campo completo
time.sleep(2)

# Espera hasta que el botón Sign Up sea clickeable y haz clic en él
sign_up_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/button")))
driver.execute_script("arguments[0].scrollIntoView();", sign_up_button)  # Asegura que el botón esté visible
actions.move_to_element(sign_up_button).click().perform()

# Pausa adicional para observar el clic
time.sleep(5)

# Cierra el navegador después de completar el registro
driver.quit()
