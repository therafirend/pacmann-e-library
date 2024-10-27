import unittest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class TestMusicPlayer(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--headless")  # Run without a GUI
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                                       options = chrome_options)
        
        self.driver.get("http://localhost:5000")
        self.driver.implicitly_wait(30)
    
    def test_play_song(self):
        self.driver.find_element(By.XPATH, "//button[@onclick=\"playAudio(this.parentElement.getAttribute(\'data-url\'), this.parentElement)\"]").click()
        self.driver.implicitly_wait(30)
        
    def test_play_pause(self):
        self.driver.find_element(By.XPATH, "//button[@onclick=\'togglePlayPause()\']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//button[@onclick=\'togglePlayPause()\']").click()
        self.driver.implicitly_wait(30)

    def test_next_previous_song(self):
        self.driver.find_element(By.XPATH, "//button[@onclick=\'nextSong()\']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//button[@onclick=\'nextSong()\']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//button[@onclick=\'previousSong()\']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//button[@onclick=\'previousSong()\']").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()