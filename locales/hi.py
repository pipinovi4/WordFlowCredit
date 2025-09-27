from __future__ import annotations
from locales.core import _register, BTN_SUPPORT, BTN_ABOUT, BTN_CHANGE_COUNTRY, BTN_MY_APPS, BTN_APPLY, BTN_BACK

L10N_HI = {
    "prompt_choose_region": "🌍 अपना आवेदन करने के लिए क्षेत्र चुनें:",
    "prompt_choose_country": "🌍 अपना देश चुनें:",
    "after_country_selected": "✅ बढ़िया, देश चुना गया है।\n अब आप आवेदन कर सकते हैं, सेवा के बारे में अधिक जान सकते हैं या अपनी सेटिंग्स बदल सकते हैं।",
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
        "<b>🌍 WorldFlow Credit — एक वैश्विक फिनटेक प्लेटफ़ॉर्म जो ऋण समाधान प्रदान करता है।</b>\n\n"
        "हम ग्राहकों को सीधे बैंकों से जोड़ते हैं, डिजिटल समाधानों और अंतरराष्ट्रीय ब्रोकरों, विश्लेषकों और सलाहकारों की विशेषज्ञता का उपयोग करके। "
        "हमारे साथ प्रक्रिया सरल, पारदर्शी और तेज़ हो जाती है।\n\n"
        "💼 हमारा इकोसिस्टम दुनिया भर के हज़ारों विशेषज्ञों और भागीदारों को एकजुट करता है, जो WorldFlow के डिजिटल स्पेस में काम करते हैं। "
        "हम बैंकिंग तकनीक को वित्तीय परामर्श से मिलाकर आपकी आवेदन प्रक्रिया को सहज बनाते हैं।\n\n"
        "<b>✅ हम प्रदान करते हैं:</b>\n"
        "— 💳 ऑनलाइन उपभोक्ता, गृह और वाहन ऋण;\n"
        "— 💼 व्यवसायों (एकल स्वामित्व / कंपनियों) के लिए डिजिटल समर्थन और विकास;\n"
        "— 📊 क्रेडिट स्कोरिंग की तैयारी और स्वीकृति की संभावना बढ़ाने के उपकरण;\n"
        "— 🤝 प्रत्येक चरण में व्यक्तिगत समर्थन — आवेदन से लेकर वितरण तक।\n\n"
        "⚡️ <b>WorldFlow Credit के साथ आपको केवल वित्तीय उत्पाद नहीं, बल्कि एक संपूर्ण डिजिटल बैंकिंग समाधान मिलता है।</b>"
    )
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

__all__ = ["L10N_HI"]