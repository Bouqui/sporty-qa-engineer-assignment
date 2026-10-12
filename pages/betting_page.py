import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BettingPage:

    # ---------- Locators ----------

    BALANCE = (By.XPATH,"//div[@id='header-balance']//span[contains(., 'Balance:')]")

    FIRST_HOME_ODDS = (By.XPATH, '//button[@id="odds-premier-league-manutd-chelsea-home"]//span[contains(@class,"oddsButtonValue")]')

    STAKE_INPUT = (By.ID,"bet-slip-stake-input")

    POTENTIAL_PAYOUT = (By.ID,"bet-slip-potential-payout")

    PLACE_BET_BUTTON = (By.ID,"bet-slip-place-bet")

    SUCCESS_RECEIPT = (By.CSS_SELECTOR,".modalTitle"
    )

    RECEIPT_STAKE = (By.ID,"modal-success-stake")

    RECEIPT_ODDS = (By.ID,"modal-success-odds")

    RECEIPT_PAYOUT = (By.ID,"modal-success-payout")

    CLOSE_RECEIPT_BUTTON = (By.CSS_SELECTOR,".modalCloseButton")

    # ---------- Constructor ----------

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---------- Navigation ----------

    def open(self, url):
        self.driver.get(url)

    # ---------- Actions ----------

    def select_first_home_odds(self):
        odds_element = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_HOME_ODDS)
        )
        odds = self._convert_to_float(odds_element.text)
        odds_element.click()
        return odds

    def enter_stake(self, stake):
        stake_input = self.wait.until(
            EC.visibility_of_element_located(self.STAKE_INPUT)
        )
        stake_input.clear()
        stake_input.send_keys(str(stake))

    def click_place_bet(self):
        place_bet_button = self.wait.until(
            EC.element_to_be_clickable(self.PLACE_BET_BUTTON)
        )

        place_bet_button.click()

    def close_receipt(self):
        close_button = self.wait.until(
            EC.element_to_be_clickable(self.CLOSE_RECEIPT_BUTTON)
        )
        close_button.click()

    # ---------- Getters ----------

    def get_balance(self):
        self.wait.until(
            lambda driver: "€0.00" not in driver.find_element(*self.BALANCE).text
        )

        balance_text = self.driver.find_element(*self.BALANCE).text

        print(f"Balance text found: {balance_text}")

        amount = (
            balance_text
            .replace("Balance:", "")
            .replace("€", "")
            .replace(",", "")
            .strip()
        )

        return float(amount)

    def get_potential_payout(self):
        payout_element = self.wait.until(
            EC.visibility_of_element_located(self.POTENTIAL_PAYOUT)
        )
        return self._convert_to_float(payout_element.text)

    def get_receipt_stake(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.RECEIPT_STAKE)
        )

        return self._convert_to_float(element.text)

    def get_receipt_odds(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.RECEIPT_ODDS)
        )

        return self._convert_to_float(element.text)

    def get_receipt_payout(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.RECEIPT_PAYOUT)
        )

        return self._convert_to_float(element.text)

    def is_success_receipt_displayed(self):
        receipt = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_RECEIPT)
        )

        return receipt.is_displayed()

    # ---------- Helpers ----------


    @staticmethod
    def _convert_to_float(value):
        """
        Extracts a numeric value from UI text such as:
        '€125.50'
        'Balance: €125.50'
        'account_balance_wallet\\nBalance: €125.50'
        '2.45'
        """

        match = re.search(r"-?\d+(?:,\d{3})*(?:\.\d+)?", value)

        if not match:
            raise ValueError(f"No numeric value found in: {value}")

        numeric_value = match.group().replace(",", "")

        return float(numeric_value)