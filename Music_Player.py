
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MusicPlayer:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('executable_path=C:\\webdriver\\chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options)

    def play_video(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query=" + query)
        
        # Wait for the presence of search results
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "video-title"))
        )
        
        # Click the first video link
        first_video = self.driver.find_element(By.ID, "video-title")
        first_video.click()

# Run the MusicPlayer
if __name__ == "__main__":
    assist = MusicPlayer()
    video_query = input("Enter the video query: ")
    assist.play_video(video_query)
