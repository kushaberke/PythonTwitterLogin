from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

username = "xxx"
password = "xxx"

ileri = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]'
giris = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
sifreinput = '[autocomplete="current-password"]'
# ChromeOptions oluştur
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Headless modu etkinleştir
driver = webdriver.Chrome(options=chrome_options)
url = 'https://www.twitter.com/login'
driver.get(url)
wait = WebDriverWait(driver, 20)

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[autocomplete="username"]'))).send_keys(username)

next_button = wait.until(EC.presence_of_element_located((By.XPATH, ileri)))
# İleri butonuna tıklayın
next_button.click()

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, sifreinput))).send_keys(password)

login_button = wait.until(EC.presence_of_element_located((By.XPATH, giris)))

login_button.click()