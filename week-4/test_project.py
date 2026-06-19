import pytest
from unittest.mock import patch
from project import checker, buyAmount, sellAmount, getPrice


def test_checker():
    # lowercase
    with patch("builtins.input", return_value="buy"):
        assert checker() == "Buy"
    with patch("builtins.input", return_value="sell"):
        assert checker() == "Sell"
    with patch("builtins.input", return_value="both"):
        assert checker() == "Both"
    with patch("builtins.input", return_value="chilling"):
        assert checker() == "Chilling"
    # uppercase
    with patch("builtins.input", return_value="BUY"):
        assert checker() == "Buy"
    with patch("builtins.input", return_value="SELL"):
        assert checker() == "Sell"
    with patch("builtins.input", return_value="BOTH"):
        assert checker() == "Both"
    # mixed case
    with patch("builtins.input", return_value="bUy"):
        assert checker() == "Buy"
    with patch("builtins.input", return_value="sElL"):
        assert checker() == "Sell"
    with patch("builtins.input", return_value="BoTh"):
        assert checker() == "Both"
    # leading/trailing spaces
    with patch("builtins.input", return_value="  buy  "):
        assert checker() == "Buy"
    with patch("builtins.input", return_value="   sell   "):
        assert checker() == "Sell"
    with patch("builtins.input", return_value="  both  "):
        assert checker() == "Both"
    # invalid input → retry → valid
    with patch("builtins.input", side_effect=["random", "123", "buy"]):
        assert checker() == "Buy"


def test_buyAmount():
    existing_ids = ["bitcoin", "ethereum"]
    rows = [
        {"ID": "bitcoin", "Holdings": "0.01", "Avg Price": "60000", "Balance": "600", "Today's Price": "60000"},
        {"ID": "ethereum", "Holdings": "0.5", "Avg Price": "2000", "Balance": "1000", "Today's Price": "2000"},
    ]
    # valid id not in existing → new position
    with patch("builtins.input", side_effect=["solana", "100"]):
        with patch("project.getPrice", return_value=100.0):
            id, entry, holding = buyAmount(existing_ids, rows)
            assert id == "solana"
            assert entry == 100.0
            assert holding == 1.0
    # valid id in existing → DCA
    with patch("builtins.input", side_effect=["bitcoin", "600"]):
        with patch("project.getPrice", return_value=60000.0):
            id, entry, holding = buyAmount(existing_ids, rows)
            assert id == "bitcoin"
    # invalid id → retry → valid
    with patch("builtins.input", side_effect=["notatoken", "solana", "200"]):
        with patch("project.getPrice", return_value=100.0):
            id, entry, holding = buyAmount(existing_ids, rows)
            assert id == "solana"
    # invalid amount → retry → valid
    with patch("builtins.input", side_effect=["solana", "abc", "solana", "100"]):
        with patch("project.getPrice", return_value=100.0):
            id, entry, holding = buyAmount(existing_ids, rows)
            assert id == "solana"


def test_sellAmount():
    existing_ids = ["bitcoin", "ethereum"]
    rows = [
        {"ID": "bitcoin", "Holdings": "0.1", "Avg Price": "60000", "Balance": "6000", "Today's Price": "60000"},
        {"ID": "ethereum", "Holdings": "1.0", "Avg Price": "2000", "Balance": "2000", "Today's Price": "2000"},
    ]
    # valid id + valid amount
    with patch("builtins.input", side_effect=["bitcoin", "1000"]):
        with patch("project.getPrice", return_value=60000.0):
            id, sLeft = sellAmount(existing_ids, rows)
            assert id == "bitcoin"
    # id not in existing → retry → valid
    with patch("builtins.input", side_effect=["solana", "bitcoin", "1000"]):
        with patch("project.getPrice", return_value=60000.0):
            id, sLeft = sellAmount(existing_ids, rows)
            assert id == "bitcoin"
    # insufficient balance → retry → valid
    with patch("builtins.input", side_effect=["bitcoin", "9999", "bitcoin", "1000"]):
        with patch("project.getPrice", return_value=60000.0):
            id, sLeft = sellAmount(existing_ids, rows)
            assert id == "bitcoin"
    # invalid amount → retry → valid
    with patch("builtins.input", side_effect=["bitcoin", "abc", "bitcoin", "1000"]):
        with patch("project.getPrice", return_value=60000.0):
            id, sLeft = sellAmount(existing_ids, rows)
            assert id == "bitcoin"


def test_getPrice():
    # valid id
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"bitcoin": {"usd": 62000.0}}
        assert getPrice("bitcoin") == 62000.0
    # valid id different price
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"ethereum": {"usd": 3000.5}}
        assert getPrice("ethereum") == 3000.5
    # price = 0
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"bitcoin": {"usd": 0}}
        assert getPrice("bitcoin") == 0
    # invalid id → KeyError
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {}
        with pytest.raises(KeyError):
            getPrice("notanid")
    # id not in response → KeyError
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"bitcoin": {"usd": 62000.0}}
        with pytest.raises(KeyError):
            getPrice("ethereum")
