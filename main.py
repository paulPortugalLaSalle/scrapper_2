from selenium.webdriver.common.by import By
import time

from src.config.driver_config import setup_driver
from src.constants.constants import SEACE_URL

def main():
    try:
        driver = setup_driver()
        driver.get(SEACE_URL)
        time.sleep(2)

        title = driver.title
        print(f"Título de la página: {title}")

        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"Número de enlaces encontrados: {len(links)}")

        for link in links:
            print(f"Enlace: {link.get_attribute('href')}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    main()