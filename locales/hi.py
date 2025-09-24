from __future__ import annotations
from . import _register, BTN_SUPPORT, BTN_ABOUT, BTN_CHANGE_COUNTRY, BTN_MY_APPS, BTN_APPLY, BTN_BACK

L10N_HI = {
    "prompt_choose_region": "🌍 अपना आवेदन करने के लिए क्षेत्र चुनें:",
    "prompt_choose_country": "🌍 अपना देश चुनें:",
    "after_country_selected": "✅ देश चुना गया: {country}\nभाषा स्वतः सेट कर दी गई है।",
    "menu_title": "आगे क्या करना चाहेंगे?",
    "btn_apply": "📝 आवेदन जमा करें",
    "apply_text": "शुरू करते हैं। व्यक्तिगत कोड पहले चरण में डाला जा सकता है।",
    "btn_support": "🛟 सहायता",
    "btn_about": "ℹ️ हमारे बारे में",
    "btn_change_country": "🌐 देश बदलें",
    "btn_my_apps": "🗂 मेरे आवेदन",
    "support_text": "हमें लिखें: @{support_username}",
    "about_text": "WorldFlow Credit — अंतर्राष्ट्रीय क्रेडिट आवेदन सेवा।",
    "my_apps_stub": "आपके आवेदन यहाँ दिखेंगे (जल्द)।",
    "back_to_region": "↩️ क्षेत्र चयन पर लौटें.",
    "btn_back": "↩ वापस",
    "btn_website": "वेबसाइट",
    "btn_tg_channel": "टेलीग्राम चैनल",
    "btn_instagram": "इंस्टाग्राम",
    "btn_x": "X / ट्विटर",
    "btn_linkedin": "लिंक्डइन",
    "btn_youtube": "यूट्यूब",

    "ui": {
        "preview_title": "आवेदन प्रगति",
        "step": "फ़ील्ड",
        "status": "स्थिति",
        "value": "मान",
        "done": "✅ पूरा",
        "todo": "❌ अधूरा",
        "share_phone": "📲 नंबर साझा करें",
        "type_manually": "✏️ मैन्युअली दर्ज करें",
        "completed_demo": "फ़ॉर्म सफलतापूर्वक भरा गया ✅",
    },

    "labels": {
        "access_code": "एक्सेस कोड",
        "full_name": "पूरा नाम",
        "phone": "फ़ोन",
        "email": "ई-मेल",
        "loan_amount": "ऋण राशि",
        "id_number": "पहचान संख्या",
        "inn_ru": "INN (सिर्फ रूस)",
        "reg_address": "पंजीकृत पता",
        "actual_address": "वर्तमान पता",
        "dob": "जन्म तिथि",
        "marital_status": "वैवाहिक स्थिति",
        "workplace": "कार्यस्थल",
    },

    "about_full": (
        "<b>WorldFlow Credit — हमारे बारे में</b><br/><br/>"
        "सीमा-पार क्रेडिट आवेदन प्लेटफ़ॉर्म: मानकीकृत KYC, स्वचालित जोखिम जाँच, "
        "और लाइसेंस प्राप्त ऋणदाताओं तक सुरक्षित रूटिंग।<br/><br/>"
        "• पारदर्शी शर्तें, कोई छिपे शुल्क नहीं<br/>"
        "• ट्रांजिट और स्टोरेज दोनों में डेटा एन्क्रिप्शन<br/>"
        "• सत्यापित भागीदारों के माध्यम से तेज़ अंडरराइटिंग<br/>"
        "• अंग्रेज़ी व स्थानीय भाषाओं में सहायता"
    ),
}

L10N_HI.update({
    BTN_SUPPORT: L10N_HI["btn_support"],
    BTN_ABOUT: L10N_HI["btn_about"],
    BTN_CHANGE_COUNTRY: L10N_HI["btn_change_country"],
    BTN_MY_APPS: L10N_HI["btn_my_apps"],
    BTN_APPLY: L10N_HI["btn_apply"],
    BTN_BACK: L10N_HI["btn_back"],
})
_register("hi", L10N_HI)
