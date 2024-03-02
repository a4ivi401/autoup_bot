from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime as dt, time as t
import time
import random
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

restart_time = random.randint(3600, 4000)
current_time = dt.now().time()
target_time = t(9, 0)


while True:
    # Инициализация вебдрайвера
    driver = webdriver.Chrome(options=chrome_options)
    # Ссылка на логин
    driver.get('https://minecraft-inside.ru/forum/login')
    time.sleep(10)

    # Вход на форум
    username = driver.find_element(By.ID, 'auth')
    password = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'elSignIn_submit')

    username.send_keys('DreamShine')
    password.send_keys('U_TitBr43NaAjkG')
    login_button.click()

    time.sleep(6)

    # модуль отправки текста
    driver.get('https://minecraft-inside.ru/forum/topic/208737-dreamshine-1201-ванила-без-лицензии/')

    time.sleep(5)
    trigger_element = driver.find_element(By.CSS_SELECTOR, 'div.ipsType_normal.ipsType_richText.ipsType_break')
    trigger_element.click()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, 'cke_1_contents')))
    element.click()
    write = driver.find_element(By.CSS_SELECTOR, 'div.cke_wysiwyg_div.cke_reset.cke_enable_context_menu.cke_editable.cke_editable_themed.cke_contents_ltr')
    write.click()
    write.send_keys('up')
    time.sleep(10)
    send_button = driver.find_element(By.XPATH, '//button[text()="Отправить"]')
    send_button.click()

    print('Done!')

    driver.quit()

    if current_time < target_time:
        print('Run Long Timer')
        time.sleep(32400)
    else:
        print('Run Short Timer')
        time.sleep(restart_time)