from __future__ import annotations
from . import _register, BTN_SUPPORT, BTN_ABOUT, BTN_CHANGE_COUNTRY, BTN_MY_APPS, BTN_APPLY, BTN_BACK

L10N_BE = {
    "prompt_choose_region": "🌍 Абярыце рэгіён для падачы заяўкі:",
    "prompt_choose_country": "🌍 Абярыце краіну:",
    "after_country_selected": "✅ Краіна абраная: {country}\nМова інтэрфейсу наладжана аўтаматычна.",
    "menu_title": "Як працягнем?",
    "btn_apply": "📝 Падаць заяўку",
    "apply_text": "Пачынаем афармленне. Персанальны код можна ўвесці на першым кроку.",
    "btn_support": "🛟 Падтрымка",
    "btn_about": "ℹ️ Пра нас",
    "btn_change_country": "🌐 Змяніць краіну",
    "btn_my_apps": "🗂 Мае заяўкі",
    "support_text": "Напішыце нам: @{support_username}",
    "about_text": "WorldFlow Credit — міжнародны сэрвіс падачы крэдытных заявак.",
    "my_apps_stub": "Тут з'явяцца вашы заяўкі (скора).",
    "back_to_region": "↩️ Вяртанне да выбару рэгіёна.",
    "btn_back": "↩ Назад",
    "btn_website": "Сайт",
    "btn_tg_channel": "Канал у Telegram",
    "btn_instagram": "Instagram",
    "btn_x": "X / Twitter",
    "btn_linkedin": "LinkedIn",
    "btn_youtube": "YouTube",

    "ui": {
        "preview_title": "Статус анкеты",
        "step": "Поле",
        "status": "Статус",
        "value": "Значэнне",
        "done": "✅ Запоўнена",
        "todo": "❌ Не запоўнена",
        "share_phone": "📲 Падзяліцца нумарам",
        "type_manually": "✏️ Увесці ўручную",
        "completed_demo": "Анкета паспяхова запоўнена ✅",
    },

    "steps": {
        "access_code": (
            "🔐 У вас ёсць персанальны код доступу?\n\n"
            "Увядзіце яго ніжэй — і мы актывуем індывідуальныя ўмовы, якія адкрываюцца толькі па асаблівым запрашэнні."
        ),
        "full_name": (
            "✍️ Калі ласка, увядзіце ваша поўнае імя дакладна так, як у пашпарце.\n\n"
            "ℹ️ Усе адказы ўводзьце непасрэдна ў паведамленнях — так анкета будзе запоўнена карэктна."
        ),
        "phone": "📞 Укажыце нумар мабільнага тэлефона ў фармаце +375XXXXXXXXX.",
        "email": "📧 Укажыце ваш адрас электроннай пошты.",
        "loan_amount": "💰 Укажыце жаданую суму крэдыту.",
        "id_number": "🆔 Укажыце ваш персанальны нумар з пашпарта.",
        "reg_address": "🏠 Укажыце адрас вашай рэгістрацыі з пашпарта.",
        "actual_address": "🏠 Укажыце фактычны адрас пражывання.\nКалі супадае з рэгістрацыяй — напішыце «Супадае».",
        "dob": "📅 Укажыце дату нараджэння ў фармаце ДД.ММ.ГГГГ.",
        "marital_status": (
            "💬 Укажыце ваш сямейны стан.\n"
            "Варыянты:\n• Не жанаты / не замужам\n• У шлюбе\n• У разводзе\n• Удавец / удава"
        ),
        "workplace": "🏢 Укажыце поўную назву вашай арганізацыі (месца працы).",
        "inn_ru": "🔢 ІНН (для РФ) — пры неабходнасці.",
    },

    "labels": {
        "access_code": "Персанальны код",
        "full_name": "Поўнае імя",
        "phone": "Тэлефон",
        "email": "Email",
        "loan_amount": "Сума крэдыту",
        "id_number": "Ідэнтыфікатар",
        "inn_ru": "ІНН (для РФ)",
        "reg_address": "Адрас рэгістрацыі",
        "actual_address": "Фактычны адрас",
        "dob": "Дата нараджэння",
        "marital_status": "Сямейны стан",
        "workplace": "Месца працы",
    },

    "about_full": (
        "<b>WorldFlow Credit — Пра нас</b><br/><br/>"
        "Міжнародная платформа крэдытных заяў: уніфікаваны KYC, аўтаматычныя праверкі рызык "
        "і бяспечная перадача даных у ліцэнзаваныя фінарганізацыі.<br/><br/>"
        "• Празрыстыя ўмовы, без схаваных камісій<br/>"
        "• Шыфраванне даных пры перадачы і захоўванні<br/>"
        "• Хуткае разглядванне праз правераных партнёраў<br/>"
        "• Падтрымка па-англійску і на мясцовых мовах"
    ),
}

L10N_BE.update({
    BTN_SUPPORT: L10N_BE["btn_support"],
    BTN_ABOUT: L10N_BE["btn_about"],
    BTN_CHANGE_COUNTRY: L10N_BE["btn_change_country"],
    BTN_MY_APPS: L10N_BE["btn_my_apps"],
    BTN_APPLY: L10N_BE["btn_apply"],
    BTN_BACK: L10N_BE["btn_back"],
})
_register("be", L10N_BE)
