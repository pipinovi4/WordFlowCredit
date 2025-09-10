# Регіони (4 розділи) і країни з дефолт-мовою (мова фіксується країною)
REGION_CIS = "region_cis"
REGION_EUROPE = "region_europe"
REGION_NA = "region_na"
REGION_ASIA = "region_asia"

COUNTRIES = {
    # СНГ
    "RU": {"flag": "🇷🇺", "name": "Россия", "lang": "ru"},
    "BY": {"flag": "🇧🇾", "name": "Беларусь", "lang": "ru"},  # дефолт RU
    "KZ": {"flag": "🇰🇿", "name": "Казахстан", "lang": "ru"},  # дефолт RU
    # Європа
    "DE": {"flag": "🇩🇪", "name": "Германия", "lang": "de"},
    "FR": {"flag": "🇫🇷", "name": "Франция", "lang": "fr"},
    "GR": {"flag": "🇬🇷", "name": "Греция", "lang": "el"},
    "GB": {"flag": "🇬🇧", "name": "Великобритания", "lang": "en"},
    # Північна Америка
    "US": {"flag": "🇺🇸", "name": "США", "lang": "en"},
    "CA": {"flag": "🇨🇦", "name": "Канада", "lang": "en"},  # старт EN
    # Азія
    "IN": {"flag": "🇮🇳", "name": "Индия", "lang": "en"},   # старт EN
    "AE": {"flag": "🇦🇪", "name": "ОАЭ", "lang": "en"},     # старт EN
}

REGION_TO_COUNTRIES = {
    REGION_CIS: ["RU", "BY", "KZ"],
    REGION_EUROPE: ["DE", "FR", "GR", "GB"],
    REGION_NA: ["US", "CA"],
    REGION_ASIA: ["IN", "AE"],
}

# Базові тексти (мінімум) — решта лежить у locales/<lang>.py
L10N_MIN = {
    "en": {
        "welcome": (
            "🌍 Welcome to WorldFlow Credit\n\n"
            "An international credit application service.\n"
            "Choose your country, complete the form, and upload your credit report.\n\n"
            "We’ll take care of the rest."
        ),
        "start_cta": "▶ Start",
        "choose_region": "🌍 Choose a region:",
        "choose_country": "🌍 Select your country:",
        "menu.title": "You're all set. What would you like to do next?",
        "menu.btn.support": "🛡 Support",
        "menu.btn.about": "ℹ️ About us",
        "menu.btn.change_country": "🌐 Change country",
        "menu.btn.apps": "📂 My applications",
        "support.text": "Support: {username}",
        "about.text": "WorldFlow Credit — international credit application service. More info coming soon.",
        "apps.empty": "You have no applications yet.",
        "region.cis": "СНГ / CIS",
        "region.europe": "Европа / Europe",
        "region.na": "Северная Америка / North America",
        "region.asia": "Азия / Asia",
    },
    "ru": {
        "welcome": (
            "🌍 Добро пожаловать в WorldFlow Credit\n\n"
            "Международный сервис подачи кредитных заявок.\n"
            "Выберите страну, заполните анкету и прикрепите отчёт.\n\n"
            "Всё остальное мы возьмём на себя."
        ),
        "start_cta": "▶ Начать",
        "choose_region": "🌍 Выберите регион:",
        "choose_country": "🌍 Выберите страну:",
        "menu.title": "Готово. Что делаем дальше?",
        "menu.btn.support": "🛡 Поддержка",
        "menu.btn.about": "ℹ️ О нас",
        "menu.btn.change_country": "🌐 Изменить страну",
        "menu.btn.apps": "📂 Мои заявки",
        "support.text": "Поддержка: {username}",
        "about.text": "WorldFlow Credit — международный сервис кредитных заявок. Скоро добавим подробности.",
        "apps.empty": "У вас пока нет заявок.",
        "region.cis": "СНГ / CIS",
        "region.europe": "Европа / Europe",
        "region.na": "Северная Америка / North America",
        "region.asia": "Азия / Asia",
    },
}
