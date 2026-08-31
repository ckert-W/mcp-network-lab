from config import DEFAULT_TIMEOUT


def load_timeout(user_config: dict | None) -> int:
    if not user_config:
        return 10

    return user_config.get("timeout", DEFAULT_TIMEOUT)
