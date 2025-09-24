# locales/common.py

class COMMON_TEXT:
    WELCOME_BILINGUAL = (
        "*Let’s get you started*\n\n"
        "▶ To continue, select your country and start the application.\n\n"
        "🌍 Indicate the country for your application.\n"
        "📄 The form and language will adjust automatically.\n"
        "\n— — — — — — — — — —\n\n"
        "*Начнём оформление*\n\n"
        "▶ Чтобы продолжить, выберите страну и начните оформление.\n\n"
        "🌍 Укажите страну для подачи заявки.\n"
        "📄 Анкета и язык настроятся автоматически."
    )

    REGIONS = {
        "CIS": {"title": "🌐 CIS / СНГ", "code": "CIS"},
        "EU":  {"title": "🇪🇺 Europe / Европа",   "code": "EU"},
        "NA":  {"title": "🗽 North America / Северная Америка", "code": "NA"},
        "AS":  {"title": "🏯 Asia / Азия", "code": "AS"},
    }

    COUNTRIES_BY_REGION = {
        "CIS": [
            {"flag": "🇷🇺", "title": "Россия",    "code": "RU", "lang": "ru"},
            {"flag": "🇧🇾", "title": "Беларусь",  "code": "BY", "lang": "ru"},
            {"flag": "🇰🇿", "title": "Қазақстан", "code": "KZ", "lang": "ru"},
        ],
        "EU": [
            {"flag": "🇩🇪", "title": "Deutschland", "code": "DE", "lang": "de"},
            {"flag": "🇫🇷", "title": "France",      "code": "FR", "lang": "fr"},
            {"flag": "🇬🇷", "title": "Ελλάδα",      "code": "GR", "lang": "el"},
            {"flag": "🇬🇧", "title": "United Kingdom", "code": "GB", "lang": "en"},
        ],
        "NA": [
            {"flag": "🇺🇸", "title": "United States", "code": "US", "lang": "en"},
            {"flag": "🇨🇦", "title": "Canada",        "code": "CA", "lang": "en"},
        ],
        "AS": [
            {"flag": "🇮🇳", "title": "भारत (India)", "code": "IN", "lang": "hi"},
            {"flag": "🇦🇪", "title": "الإمارات (UAE)", "code": "AE", "lang": "ar"},
        ],
    }


__all__ = ["COMMON_TEXT"]