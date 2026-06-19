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
    # valid id + valid amount
    with patch("builtins.input", side_effect=["bitcoin", "100"]):
        assert buyAmount() == ("bitcoin", 100.0)
    # valid id + decimal amount
    with patch("builtins.input", side_effect=["ethereum", "99.5"]):
        assert buyAmount() == ("ethereum", 99.5)
    # invalid amount → retry → valid
    with patch("builtins.input", side_effect=["bitcoin", "abc", "bitcoin", "100"]):
        assert buyAmount() == ("bitcoin", 100.0)

def test_sellAmount():
    existing_ids = ["solana", "bitcoin", "ethereum"]
    # valid id + valid amount
    with patch("builtins.input", side_effect=["solana", "50"]):
        assert sellAmount(existing_ids) == ("solana", 50.0)
    # valid id + decimal amount
    with patch("builtins.input", side_effect=["bitcoin", "150.75"]):
        assert sellAmount(existing_ids) == ("bitcoin", 150.75)
    # invalid amount → retry → valid
    with patch("builtins.input", side_effect=["bitcoin", "abc", "bitcoin", "300"]):
        assert sellAmount(existing_ids) == ("bitcoin", 300.0)


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