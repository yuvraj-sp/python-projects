from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = 'YOUR TWITTER EMAIL'
TWITTER_PASSWORD = 'YOUR TWITTER PASSWORD'


class InternetSpeedTwitterBot:
    def __init__(self ):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        try:
                    accept_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
                    )
                    accept_button.click()
        except:
            print("No popup found, continuing...")

        time.sleep(3)

        go_button = self.driver.find_element(By.XPATH, value='//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button')
        go_button.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, value="py-2 font-mono text-5xl MuiBox-root css-s31qlv").text
        self.up = self.driver.find_element(By.CLASS_NAME, value='<h3 class="py-2 font-mono text-5xl MuiBox-root css-s31qlv">0.52</h3>').text

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

