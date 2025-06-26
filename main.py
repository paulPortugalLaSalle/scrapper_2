from os import environ

from selenium.webdriver.common.by import By
import time

from src.config.driver_config import setup_driver
from src.constants.constants import SEACE_URL
from src.operations.user_operations import UserOperations

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


def list_user():
    users = UserOperations().list_users()
    if users.count() >= 1:
        for user in users:
            print(f"user: {user.email}, pass: {user.password}")
    user = UserOperations().create_user(
        first_name=f"user_test{users.count() + 1}",
        last_name=f"apellido_test{users.count() + 1}",
        email=f"test@cg{users.count() + 1}.com",
        password="q1w2e3r4"
    )


if __name__ == "__main__":
    list_user()
    main()
