from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# These options are to avoid opening the browser, it runs just the process in the background
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#Use this option if you want to change the browser window size/resolution
chrome_options.add_argument('window-size=1200x600')
#**********************************************************************************************************************************#
#Use this if you want to run the script with the options above without opening the browser
browser = webdriver.Chrome(options=chrome_options)
#Replace by this line below if you want to test the script opening the browser to see what is happening step by step on your machine
#browser = webdriver.Chrome()

#STEP 1: Opening the URL you want to capture the screen
url1 = ('https://time.is/')
browser.get(url1)
#STEP 2: Capturing the screen
browser.save_screenshot("screenshot.png")
#STEP 3: Closing browser
browser.quit()