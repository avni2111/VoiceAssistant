from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class infow():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('C:/webdrive/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")
        search = self.driver.find_element("xpath", '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        search.send_keys(Keys.RETURN)

        try:
            # Wait for the search results to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]/div/p')))
            
            # Extract the first four paragraphs from the search results
            paragraphs = self.driver.find_elements("xpath", '//*[@id="mw-content-text"]/div/p')[:4]
            result = "\n".join([paragraph.text for paragraph in paragraphs])
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            # Close the browser window
            self.driver.quit()

            


