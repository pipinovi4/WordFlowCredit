from __future__ import annotations
from locales.core import _register, BTN_SUPPORT, BTN_ABOUT, BTN_CHANGE_COUNTRY, BTN_MY_APPS, BTN_APPLY, BTN_BACK

L10N_EN_GB = {
    "prompt_choose_region": "🌍 Select the region for your application:",
    "after_country_selected": "✅ Great, country selected.\n You can now submit an application, learn more about the service, or adjust your settings.",
    "menu_title": "What would you like to do next?",
    "btn_apply": "📝 Submit application",
    "apply_text": "Let's begin. A personal access code can be entered on the first step.",
    "btn_support": "🛟 Support",
    "btn_about": "ℹ️ About us",
    "btn_change_country": "🌐 Change country",
    "btn_my_apps": "🗂 My applications",
    "my_applications_text": (
        "<b>🗂 My applications</b>\n\n"
        "Your active applications will appear here: status, documents, comments, and direct chat with an adviser.\n"
    ),
    "support_text": (
        "<b>💬 WorldFlow Credit Support</b>\n\n"
        "We stay connected to help decisions move quicker:\n"
        "— untangling complex cases,\n"
        "— guiding you through the best steps,\n"
        "— linking you with the right expert.\n\n"
        "📲 Your direct support channel: <b>@WorldFlowSupport</b>"
    ),
    "about_text": "WorldFlow Credit — international credit application service.",
    "my_apps_stub": "Your applications will appear here (soon).",
    "back_to_region": (
        "<b>↩️ Change region and continue 🌐</b>\n\n"
        "💡 Choose the country you are currently located in — "
        "so we can provide tailored products and forms."
    ),
    "btn_back": "↩ Back",
    "btn_website": "Website",
    "btn_tg_channel": "Telegram channel",
    "btn_instagram": "Instagram",
    "btn_x": "X / Twitter",
    "btn_linkedin": "LinkedIn",
    "btn_youtube": "YouTube",

    "ui": {
        "preview_title": "Application progress",
        "step": "Field",
        "status": "Status",
        "value": "Value",
        "done": "✅ Completed",
        "todo": "❌ Not filled",
        "share_phone": "📲 Share number (auto-fill from Telegram)",
        "type_manually": "✏️ Enter manually",
        "completed_demo": "The form has been successfully completed ✅",
    },

    "steps": {
        "access_code": (
            "🔐 Do you have a personal access code?\n\n"
            "Enter it below — and we’ll activate individual terms available only by special invitation."
        ),
        "full_name": (
            "✍️ Please enter your full name exactly as it appears in your passport.\n\n"
            "ℹ️ Enter all answers directly in messages — this ensures the form is completed correctly."
        ),
        "phone": "📞 Enter your mobile number in international format (e.g., +44XXXXXXXXXX).",
        "email": "📧 Enter your email address.",
        "loan_amount": "💰 Enter the desired loan amount.",
        "id_number": "🆔 Enter your National Insurance number (NINo).",
        "reg_address": "🏠 Enter your registered residential address (as in your ID).",
        "actual_address": "🏠 Enter your current residential address.\nIf it is the same as your registered address — write \"Same\".",
        "dob": "📅 Enter your date of birth (DD/MM/YYYY).",
        "marital_status": (
            "💬 Select your marital status.\nOptions:\n• Single\n• Married\n• Divorced\n• Widowed"
        ),
        "workplace": "🏢 Enter the full name of your organisation (place of work).",
        "inn_ru": "🔢 Enter your INN (Russia only).",
    },

    "about_full": (
        "<b>🌍 WorldFlow Credit — a global fintech platform for lending.</b>\n\n"
        "We connect clients directly with banks, using digital solutions and the expertise of international brokers, analysts, "
        "and consultants. With us, the process becomes simple, transparent, and fast.\n\n"
        "💼 Our ecosystem brings together thousands of specialists and partners worldwide, working in the unified digital space "
        "of WorldFlow. We merge banking technology with financial consulting to ensure your applications are processed without barriers.\n\n"
        "<b>✅ We provide:</b>\n"
        "— 💳 online consumer, mortgage, and auto loans;\n"
        "— 💼 digital support for businesses (sole traders/companies), turnover growth, and deal support;\n"
        "— 📊 tools to prepare for credit scoring and boost approval chances;\n"
        "— 🤝 personal support at every stage — from application to disbursement.\n\n"
        "⚡️ <b>With WorldFlow Credit, you gain not just access to financial products, but a full digital banking tool, "
        "where every solution scales to your goals.</b>"
    ),

    "steps_by_country": {
        "GB": {
            "phone": "📞 Enter your mobile number in the format +44XXXXXXXXXX.",
            "id_number": "🆔 Enter your NINo (National Insurance number).",
            "dob": "📅 Enter your date of birth in the format DD/MM/YYYY.",
        },
    },

    "labels": {
        "access_code": "Access code",
        "full_name": "Full name",
        "phone": "Phone",
        "email": "Email",
        "loan_amount": "Loan amount",
        "id_number": "Identifier",
        "inn_ru": "INN (Russia only)",
        "reg_address": "Registered address",
        "actual_address": "Current address",
        "dob": "Date of birth",
        "marital_status": "Marital status",
        "workplace": "Workplace",
    },
}

L10N_EN_GB.update({
    BTN_SUPPORT: L10N_EN_GB["btn_support"],
    BTN_ABOUT: L10N_EN_GB["btn_about"],
    BTN_CHANGE_COUNTRY: L10N_EN_GB["btn_change_country"],
    BTN_MY_APPS: L10N_EN_GB["btn_my_apps"],
    BTN_APPLY: L10N_EN_GB["btn_apply"],
    BTN_BACK: L10N_EN_GB["btn_back"],
})
_register("en-GB", L10N_EN_GB)

__all__ = ["L10N_EN_GB"]
