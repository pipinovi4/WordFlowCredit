# --- new: keys for the application flow ---
APP_FLOW = "app_flow"
APP_STEPS = "steps"
APP_IDX = "idx"
APP_ANS = "answers"

# кроки: ключі (узгоджені з локалізаціями)
# якщо країна RU – буде додано extra "inn_ru"
BASE_STEP_ORDER = [
    "access_code",      # персональный код доступа (перший крок)
    "full_name",
    "phone",
    "telegram",
    "email",
    "loan_amount",
    "id_number",
    # RU: + inn_ru (окремо нижче)
    "reg_address",
    "actual_address",
    "dob",
    "marital_status",
    "workplace",
]

MARITAL_OPTIONS = {
    "en": ["Single", "Married", "Divorced", "Widowed"],
    "ru": ["Не женат / не замужем", "В браке", "В разводе", "Вдовец / вдова"],
}

# Прості тексти для кроку access_code (щоб не лізти у всі locale-файли)
ACCESS_CODE_PROMPTS = {
    "en": "🔐 Do you have a personal access code?\n\nEnter it below — optional. You can also type “No”.",
    "ru": "🔐 У вас есть персональный код доступа?\n\nВведите его ниже — необязательно. Можно написать «Нет».",
    "be": "🔐 У вас ёсць персанальны код доступу?\n\nУвядзіце яго ніжэй — неабавязкова.",
    "kk": "🔐 Жеке қолжетімділік кодыңыз бар ма?\n\nТөменде енгізіңіз — міндетті емес.",
    "hi": "🔐 क्या आपके पास व्यक्तिगत एक्सेस कोड है?\n\nनीचे दर्ज करें — वैकल्पिक.",
    "fr": "🔐 Avez-vous un code d’accès personnel ?\n\nSaisissez-le ci-dessous — facultatif.",
    "de": "🔐 Haben Sie einen persönlichen Zugangscode?\n\nUnten eingeben — optional.",
    "el": "🔐 Έχετε προσωπικό κωδικό πρόσβασης; \n\nΠληκτρολογήστε τον — προαιρετικό.",
    "ar": "🔐 هل لديك رمز وصول شخصي؟ \n\nأدخله أدناه — اختياري.",
}
