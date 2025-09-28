from __future__ import annotations
from locales.core import _register, BTN_SUPPORT, BTN_ABOUT, BTN_CHANGE_COUNTRY, BTN_MY_APPS, BTN_APPLY, BTN_BACK

L10N_DE = {
    "prompt_choose_region": "🌍 Wählen Sie die Region für Ihren Antrag:",
    "prompt_choose_country": "🌍 Wählen Sie Ihr Land:",
    "after_country_selected": "✅ Perfekt, Land ausgewählt.\n Sie können nun einen Antrag stellen, mehr über den Service erfahren oder Ihre Einstellungen ändern.",
    "menu_title": "🧭 WorldFlow Credit — Ihr Finanznavigator. Wählen Sie Ihre Richtung: Antrag, Support, Informationen oder Ihre Anträge.",
    "btn_apply": "📝 Antrag stellen",
    "apply_text": "Legen wir los. Einen persönlichen Code können Sie im ersten Schritt eingeben.",
    "btn_support": "🛟 Support",
    "btn_about": "ℹ️ Über uns",
    "btn_change_country": "🌐 Land ändern",
    "btn_my_apps": "🗂 Meine Anträge",
    "my_applications_text": (
        "<b>🗂 Meine Anträge</b>\n\n"
        "Hier erscheinen Ihre aktiven Anträge: Status, Dokumente, Kommentare und Chat mit einem Experten.\n"
    ),
    "support_text": (
        "<b>💬 WorldFlow Credit Support</b>\n\n"
        "Wir sind für Sie da, damit Entscheidungen schneller getroffen werden:\n"
        "— wir lösen komplexe Situationen,\n"
        "— zeigen optimale nächste Schritte,\n"
        "— verbinden Sie mit dem passenden Spezialisten.\n\n"
        "📲 Ihr persönlicher Support-Kanal: <b>@WorldFlowSupport</b>"
    ),
    "about_text": "WorldFlow Credit — internationaler Kredit-Antragsservice.",
    "my_apps_stub": "Ihre Anträge erscheinen hier (bald).",
    "back_to_region": (
        "<b>↩️ Region wechseln und fortfahren 🌐</b>\n\n"
        "💡 Geben Sie das Land an, in dem Sie sich gerade befinden — "
        "so zeigen wir Ihnen die relevantesten Produkte und Formulare."
    ),
    "btn_back": "↩ Zurück",
    "btn_website": "Webseite",
    "btn_tg_channel": "Telegram-Kanal",
    "btn_instagram": "Instagram",
    "btn_x": "X / Twitter",
    "btn_linkedin": "LinkedIn",
    "btn_youtube": "YouTube",

    "ui": {
        "preview_title": "Antragsstatus",
        "step": "Feld",
        "status": "Status",
        "value": "Wert",
        "done": "✅ Erledigt",
        "todo": "❌ Offen",
        "share_phone": "📲 Nummer teilen",
        "type_manually": "✏️ Manuell eingeben",
        "completed_demo": "Das Formular wurde erfolgreich ausgefüllt ✅",
    },

    "about_full": (
        "<b>🌍 WorldFlow Credit — eine globale Fintech-Plattform für Kreditlösungen.</b>\n\n"
        "Wir verbinden Kunden direkt mit Banken, durch digitale Lösungen und die Expertise internationaler Broker, Analysten und Berater. "
        "Mit uns wird der Prozess einfach, transparent und schnell.\n\n"
        "💼 Unser Ökosystem umfasst Tausende von Spezialisten und Partnern weltweit, die im digitalen Raum von WorldFlow zusammenarbeiten. "
        "Wir kombinieren Bankentechnologien mit Finanzberatung, damit Ihre Anträge ohne Hindernisse bearbeitet werden.\n\n"
        "<b>✅ Wir bieten:</b>\n"
        "— 💳 Online-Kredite für Konsum, Immobilien und Fahrzeuge;\n"
        "— 💼 digitale Unterstützung für Unternehmen (Einzelunternehmer / GmbH), Umsatzwachstum und Geschäftsbegleitung;\n"
        "— 📊 Algorithmen zur Vorbereitung auf Bonitätsscoring zur Steigerung der Genehmigungschancen;\n"
        "— 🤝 persönliche Begleitung in jeder Phase — von der Antragstellung bis zur Auszahlung.\n\n"
        "⚡️ <b>Mit WorldFlow Credit erhalten Sie nicht nur Zugang zu Finanzprodukten, "
        "sondern ein vollständiges digitales Banking-Tool, das Ihre Ziele unterstützt.</b>"
    ),

    "steps_by_country": {
        "DE": {
            "phone": "📞 Bitte geben Sie Ihre Handynummer im Format +49XXXXXXXXXX ein.",
            "id_number": "🆔 Bitte geben Sie Ihre Steuer-ID ein.",
            "dob": "📅 Bitte geben Sie Ihr Geburtsdatum im Format TT.MM.JJJJ ein.",
        }
    },
    "labels": {
        "access_code": "Zugangscode",
        "full_name": "Vollständiger Name",
        "phone": "Telefon",
        "email": "E-Mail",
        "loan_amount": "Kreditsumme",
        "id_number": "Steuer-ID",
        "inn_ru": "INN (nur Russland)",
        "reg_address": "Meldeadresse",
        "actual_address": "Aktuelle Adresse",
        "dob": "Geburtsdatum",
        "marital_status": "Familienstand",
        "workplace": "Arbeitgeber",
    },
}

# generic steps fallback are taken from English; DE has country specifics above.

L10N_DE.update({
    BTN_SUPPORT: L10N_DE["btn_support"],
    BTN_ABOUT: L10N_DE["btn_about"],
    BTN_CHANGE_COUNTRY: L10N_DE["btn_change_country"],
    BTN_MY_APPS: L10N_DE["btn_my_apps"],
    BTN_APPLY: L10N_DE["btn_apply"],
    BTN_BACK: L10N_DE["btn_back"],
})
_register("de", L10N_DE)

__all__ = ["L10N_DE"]