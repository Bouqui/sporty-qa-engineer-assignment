import requests

from utils.config import BASE_URL, USER_ID


def test_place_bet_rejected_without_user_id():
    """
    Verify that POST /api/place-bet rejects a request
    when x-user-id is missing.
    """

    # get an existing match using a valid user
    match_response = requests.get(
        f"{BASE_URL}/api/matches",
        headers={
            "x-user-id": USER_ID
        }
    )

    assert match_response.status_code == 200

    matches = match_response.json()

    assert len(matches) > 0, "No matches returned by the API"

    # get the id of the first match returned from the previous request
    match_id = matches[0]["id"]

    payload = {
        "matchId": match_id,
        "selection": "HOME",
        "stake": 10.00
    }

    # intentionally omit x-user-id
    response = requests.post(
        f"{BASE_URL}/api/place-bet",
        json=payload
    )

    # Assert
    assert response.status_code == 401, (
        f"Expected 401 when x-user-id is missing, "
        f"but got {response.status_code}. "
        f"Response body: {response.text}"
    )