from __future__ import annotations
from locales.core import _register, BTN_SUPPORT, BTN_ABOUT, BTN_CHANGE_COUNTRY, BTN_MY_APPS, BTN_APPLY, BTN_BACK

L10N_KK = {
    "prompt_choose_region": "🌍 Өтінім беру үшін өңірді таңдаңыз:",
    "prompt_choose_country": "🌍 Елді таңдаңыз:",
    "after_country_selected": "✅ Ел таңдалды: {country}\nИнтерфейс тілі автоматты түрде орнатылды.",
    "menu_title": "Қалай жалғастырамыз?",
    "btn_apply": "📝 Өтінім жіберу",
    "apply_text": "Бастайық. Жеке кодты бірінші қадамда енгізуге болады.",
    "btn_support": "🛟 Қолдау",
    "btn_about": "ℹ️ Біз туралы",
    "btn_change_country": "🌐 Елді өзгерту",
    "btn_my_apps": "🗂 Менің өтінімдерім",
    "support_text": "Бізге жазыңыз: @{support_username}",
    "about_text": "WorldFlow Credit — халықаралық несие өтінім қызметі.",
    "my_apps_stub": "Мұнда сіздің өтінімдеріңіз көрсетіледі (жақында).",
    "back_to_region": "↩️ Өңір таңдауына қайту.",
    "btn_back": "↩ Артқа",
    "btn_website": "Веб-сайт",
    "btn_tg_channel": "Telegram арнасы",
    "btn_instagram": "Instagram",
    "btn_x": "X / Twitter",
    "btn_linkedin": "LinkedIn",
    "btn_youtube": "YouTube",

    "ui": {
        "preview_title": "Анкета күйі",
        "step": "Өріс",
        "status": "Күйі",
        "value": "Мәні",
        "done": "✅ Толтырылған",
        "todo": "❌ Толтырылмаған",
        "share_phone": "📲 Нөмірді бөлісу",
        "type_manually": "✏️ Қолмен енгізу",
        "completed_demo": "Анкета сәтті толтырылды ✅",
    },

    "steps": {
        "access_code": (
            "🔐 Сізде жеке қол жеткізу коды бар ма?\n\n"
            "Оны төменде енгізіңіз — біз тек арнайы шақыру арқылы ашылатын жеке шарттарды қосамыз."
        ),
        "full_name": (
            "✍️ Өтініш, толық атыңызды құжаттағыдай дәл енгізіңіз.\n\n"
            "ℹ️ Барлық жауаптарды тікелей хабарламаларда енгізіңіз — сонда анкета дұрыс толтырылады."
        ),
        "phone": "📞 Ұялы телефон нөмірін +7XXXXXXXXXX форматында енгізіңіз.",
        "email": "📧 Электрондық пошта мекенжайыңызды көрсетіңіз.",
        "loan_amount": "💰 Қалаған несие сомасын көрсетіңіз.",
        "id_number": "🆔 ИИН (ЖСН) нөміріңізді енгізіңіз.",
        "reg_address": "🏠 Паспорттағы тіркелген мекенжайыңызды көрсетіңіз.",
        "actual_address": "🏠 Нақты тұратын мекенжайыңызды көрсетіңіз.\nЕгер тіркелген мекенжаймен сәйкес болса — «Сәйкес».",
        "dob": "📅 Туған күніңізді КК.АА.ЖЖЖЖ форматында енгізіңіз.",
        "marital_status": (
            "💬 Отбасылық жағдайыңызды көрсетіңіз.\nТаңдау:\n• Үйленбеген / тұрмыс құрмаған\n• Үйленген / тұрмыста\n• Ажырасқан\n• Жесір"
        ),
        "workplace": "🏢 Жұмыс орныңыздың толық атауын көрсетіңіз (ұйым атауы).",
        "inn_ru": "🔢 РФ үшін ИНН (10 немесе 12 сан).",
    },

    "labels": {
        "access_code": "Жеке код",
        "full_name": "Толық аты",
        "phone": "Телефон",
        "email": "Email",
        "loan_amount": "Несие сомасы",
        "id_number": "ИИН (ЖСН)",
        "inn_ru": "ИНН (РФ)",
        "reg_address": "Тіркелген мекенжай",
        "actual_address": "Нақты мекенжай",
        "dob": "Туған күні",
        "marital_status": "Отбасы жағдайы",
        "workplace": "Жұмыс орны",
    },

    "about_full": (
        "<b>WorldFlow Credit — Біз туралы</b><br/><br/>"
        "Халықаралық несие өтінім платформасы: біріздендірілген KYC, тәуекелдерді автоматты тексеру "
        "және лицензияланған кредиторларға қауіпсіз жеткізу.<br/><br/>"
        "• Жасырын комиссиясыз, ашық талаптар<br/>"
        "• Мәліметтерді беру және сақтау кезінде шифрлау<br/>"
        "• Тексерілген серіктестер арқылы жедел қарау<br/>"
        "• Ағылшын және жергілікті тілдерде қолдау"
    ),
}

L10N_KK.update({
    BTN_SUPPORT: L10N_KK["btn_support"],
    BTN_ABOUT: L10N_KK["btn_about"],
    BTN_CHANGE_COUNTRY: L10N_KK["btn_change_country"],
    BTN_MY_APPS: L10N_KK["btn_my_apps"],
    BTN_APPLY: L10N_KK["btn_apply"],
    BTN_BACK: L10N_KK["btn_back"],
})
_register("kk", L10N_KK)

__all__ = ["L10N_KK"]