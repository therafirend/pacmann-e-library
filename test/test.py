import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestMusicPlayer(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--headless")  # Run without a GUI
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        self.driver.get("http://localhost:5000")
        self.driver.implicitly_wait(10)  # Reduced implicit wait

    def wait_and_click(self, selector, wait_time=10):
        """Utility method to wait for an element and click it."""
        element = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, selector))
        )
        element.click()

    def test_play_song(self):
        self.wait_and_click("//button[@onclick=\"playAudio(this.parentElement.getAttribute('data-url'), this.parentElement)\"]")

    def test_play_pause(self):
        self.wait_and_click("//button[@onclick='togglePlayPause()']")
        self.wait_and_click("//button[@onclick='togglePlayPause()']")

    def test_next_previous_song(self):
        self.wait_and_click("//button[@onclick='nextSong()']")
        self.wait_and_click("//button[@onclick='nextSong()']")
        self.wait_and_click("//button[@onclick='previousSong()']")
        self.wait_and_click("//button[@onclick='previousSong()']")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()