from __future__ import annotations

# Import core functions for avoid circular import
from locales.core import translate, _register, BTN_SUPPORT, BTN_ABOUT, BTN_CHANGE_COUNTRY, BTN_MY_APPS, BTN_APPLY, BTN_BACK

# import languages (registration side-effects)
from locales.en import L10N_EN
from locales.ru import L10N_RU
from locales.de import L10N_DE
from locales.fr import L10N_FR
from locales.el import L10N_EL
from locales.ar import L10N_AR
from locales.hi import L10N_HI
from locales.be import L10N_BE
from locales.kk import L10N_KK
from locales.common import COMMON_TEXT


__all__ = [
    "translate",
    "_register",
    "BTN_SUPPORT",
    "BTN_ABOUT",
    "BTN_CHANGE_COUNTRY",
    "BTN_MY_APPS",
    "BTN_APPLY",
    "BTN_BACK",
    "COMMON_TEXT",
]