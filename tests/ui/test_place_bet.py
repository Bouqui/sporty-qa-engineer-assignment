
from utils.config import APP_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_application_opens(driver):

    driver.get(APP_URL)

    assert driver.current_url is not None

    driver.quit()