import pytest

from pages.betting_page import BettingPage
from utils.config import APP_URL


@pytest.mark.ui
def test_user_can_place_valid_single_bet(driver):
    """
    Critical E2E journey.

    This test verifies that a user can successfully place a valid single bet
    and that the receipt and account balance are updated correctly.
    """

    betting_page = BettingPage(driver)

    # Open application
    betting_page.open(APP_URL)

    # Capture starting balance
    initial_balance = betting_page.get_balance()

    # Select a valid HOME outcome
    odds = betting_page.select_first_home_odds()

    # Enter a valid stake
    stake = 10.00
    betting_page.enter_stake(stake)

    # Verify payout before placing the bet
    expected_payout = round(stake * odds, 2)
    displayed_payout = betting_page.get_potential_payout()

    assert displayed_payout == expected_payout, f"Expected payout €{expected_payout}, "f"but displayed €{displayed_payout}"

    # Place bet
    betting_page.click_place_bet()

    # Verify success receipt
    assert betting_page.is_success_receipt_displayed(), (
        "Success receipt was not displayed after placing the bet"
    )

    # Validate receipt values
    receipt_stake = betting_page.get_receipt_stake()
    receipt_odds = betting_page.get_receipt_odds()
    receipt_payout = betting_page.get_receipt_payout()

    assert receipt_stake == stake, f"Expected receipt stake €{stake}, "f"but got €{receipt_stake}"

    assert receipt_odds == odds, f"Expected receipt odds {odds}, "f"but got {receipt_odds}"

    assert receipt_payout == expected_payout, f"Expected receipt payout €{expected_payout}, "f"but got €{receipt_payout}"

    # Close receipt
    betting_page.close_receipt()

    # Verify balance was reduced by the stake
    updated_balance = betting_page.get_balance()
    expected_balance = round(initial_balance - stake, 2)

    assert updated_balance == expected_balance, (
        f"Expected balance €{expected_balance}, "
        f"but got €{updated_balance}"
    )