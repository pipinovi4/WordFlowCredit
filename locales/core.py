# Action ids (must match main.py)
BTN_SUPPORT        = "support"
BTN_ABOUT          = "about"
BTN_CHANGE_COUNTRY = "change_country"
BTN_MY_APPS        = "my_apps"
BTN_APPLY          = "apply"
BTN_BACK           = "back"

_L10N: dict[str, dict] = {}

def _register(lang: str, data: dict) -> None:
    # merge (allow partial updates)
    _L10N[lang] = {**_L10N.get(lang, {}), **data}

def _lang_map(lang: str) -> dict:
    return _L10N.get(lang, _L10N.get("en", {}))

def _get_dotted(m: dict, dotted: str):
    cur = m
    for p in dotted.split("."):
        if isinstance(cur, dict) and p in cur:
            cur = cur[p]
        else:
            return None
    return cur if isinstance(cur, (str, int, float)) else None

def translate(lang: str, key: str, **kwargs) -> str:
    m = _lang_map(lang)
    s = m.get(key)
    if s is None:
        s = _get_dotted(m, key)
        if s is None:
            s = _lang_map("en").get(key, key)
    try:
        return str(s).format(**kwargs)
    except Exception:
        return str(s)

__all__ = [
    "translate",
    "_register",
    "BTN_SUPPORT",
    "BTN_ABOUT",
    "BTN_CHANGE_COUNTRY",
    "BTN_MY_APPS",
    "BTN_APPLY",
    "BTN_BACK",
]