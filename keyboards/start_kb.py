from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from configs import L10N_MIN

def start_keyboard() -> InlineKeyboardMarkup:
    text = f"{L10N_MIN['en']['start_cta']} / {L10N_MIN['ru']['start_cta']}"
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, callback_data="go_regions")]])
