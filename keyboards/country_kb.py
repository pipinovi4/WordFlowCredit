from __future__ import annotations
from typing import List
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from configs import COUNTRIES_BY_REGION
from .callbacks import cb_country, CB_START

def kb_countries(region_code: str) -> InlineKeyboardMarkup:
    rows: List[List[InlineKeyboardButton]] = []
    for c in COUNTRIES_BY_REGION[region_code]:
        rows.append([InlineKeyboardButton(f'{c["flag"]} {c["title"]}', callback_data=cb_country(c["code"]))])
    rows.append([InlineKeyboardButton("↩️ Back / Назад", callback_data=CB_START)])
    return InlineKeyboardMarkup(rows)
