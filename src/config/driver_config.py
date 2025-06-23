from selenium import webdriver


def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')

    #chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--disable-setuid-sandbox")
    #chrome_options.add_argument("--headless=new")
    #chrome_options.add_extension("capsolver_extension.zip")
    #chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument("--disable-popup-blocking")
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.set_page_load_timeout(100)
    return driver