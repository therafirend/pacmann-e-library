import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestMusicPlayer(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--headless")  # Run without a GUI
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        self.driver.get("http://localhost:5000")
        self.driver.implicitly_wait(10)

    def scroll_and_click(self, selector, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, selector))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, selector)))
        element.click()

    def js_click(self, selector, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, selector))
        )
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_obstruction_to_hide(self, obstruction_selector, wait_time=10):
        WebDriverWait(self.driver, wait_time).until(
            EC.invisibility_of_element_located((By.XPATH, obstruction_selector))
        )

    def test_play_song(self):
        self.wait_for_obstruction_to_hide("//div[@class='now-playing-bar']")
        self.scroll_and_click("//button[@onclick=\"playAudio(this.parentElement.getAttribute('data-url'), this.parentElement)\"]")

    def test_play_pause(self):
        self.wait_for_obstruction_to_hide("//div[@class='now-playing-bar']")
        self.scroll_and_click("//button[@onclick='togglePlayPause()']")
        self.scroll_and_click("//button[@onclick='togglePlayPause()']")

    def test_next_previous_song(self):
        self.wait_for_obstruction_to_hide("//div[@class='now-playing-bar']")
        self.scroll_and_click("//button[@onclick='nextSong()']")
        self.scroll_and_click("//button[@onclick='nextSong()']")
        self.scroll_and_click("//button[@onclick='previousSong()']")
        self.scroll_and_click("//button[@onclick='previousSong()']")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()