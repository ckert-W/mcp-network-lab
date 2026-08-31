from loader import load_timeout


def test_explicit_timeout():
    assert load_timeout({"timeout": 45}) == 45


def test_missing_timeout_key_uses_default():
    assert load_timeout({"retries": 3}) == 30
