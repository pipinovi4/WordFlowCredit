from __future__ import annotations
from . import _register, BTN_SUPPORT, BTN_ABOUT, BTN_CHANGE_COUNTRY, BTN_MY_APPS, BTN_APPLY, BTN_BACK

L10N_AR = {
    "prompt_choose_region": "🌍 اختر المنطقة لتقديم طلبك:",
    "prompt_choose_country": "🌍 اختر دولتك:",
    "after_country_selected": "✅ تم اختيار الدولة: {country}\nتم ضبط اللغة تلقائيًا.",
    "menu_title": "بماذا نتابع؟",
    "btn_apply": "📝 تقديم طلب",
    "apply_text": "لنبدأ. يمكنك إدخال رمز وصول شخصي في الخطوة الأولى.",
    "btn_support": "🛟 الدعم",
    "btn_about": "ℹ️ من نحن",
    "btn_change_country": "🌐 تغيير الدولة",
    "btn_my_apps": "🗂 طلباتي",
    "support_text": "راسلنا: @{support_username}",
    "about_text": "WorldFlow Credit — خدمة دولية لتقديم طلبات الائتمان.",
    "my_apps_stub": "ستظهر طلباتك هنا (قريبًا).",
    "back_to_region": "↩️ الرجوع لاختيار المنطقة.",
    "btn_back": "↩ رجوع",
    "btn_website": "الموقع",
    "btn_tg_channel": "قناة تيليجرام",
    "btn_instagram": "إنستغرام",
    "btn_x": "X / تويتر",
    "btn_linkedin": "لينكدإن",
    "btn_youtube": "يوتيوب",

    "ui": {
        "preview_title": "تقدم الطلب",
        "step": "الحقل",
        "status": "الحالة",
        "value": "القيمة",
        "done": "✅ مكتمل",
        "todo": "❌ غير مكتمل",
        "share_phone": "📲 مشاركة الرقم",
        "type_manually": "✏️ إدخال يدوي",
        "completed_demo": "تم ملء النموذج بنجاح ✅",
    },

    "labels": {
        "access_code": "رمز الوصول",
        "full_name": "الاسم الكامل",
        "phone": "الهاتف",
        "email": "البريد الإلكتروني",
        "loan_amount": "مبلغ القرض",
        "id_number": "المعرف الوطني",
        "inn_ru": "INN (روسيا فقط)",
        "reg_address": "عنوان التسجيل",
        "actual_address": "العنوان الحالي",
        "dob": "تاريخ الميلاد",
        "marital_status": "الحالة الاجتماعية",
        "workplace": "جهة العمل",
    },

    "about_full": (
        "<b>WorldFlow Credit — من نحن</b><br/><br/>"
        "منصّة دولية لطلبات الائتمان: توحيد إجراءات KYC، فحوصات مخاطر آلية، "
        "وتوجيه آمن للطلبات إلى جهات مُرخّصة.<br/><br/>"
        "• شروط شفافة بلا رسوم خفية<br/>"
        "• تشفير للبيانات أثناء النقل والتخزين<br/>"
        "• دراسة سريعة عبر شركاء موثّقين<br/>"
        "• دعم بالإنجليزية واللغات المحلية"
    ),
}

L10N_AR.update({
    BTN_SUPPORT: L10N_AR["btn_support"],
    BTN_ABOUT: L10N_AR["btn_about"],
    BTN_CHANGE_COUNTRY: L10N_AR["btn_change_country"],
    BTN_MY_APPS: L10N_AR["btn_my_apps"],
    BTN_APPLY: L10N_AR["btn_apply"],
    BTN_BACK: L10N_AR["btn_back"],
})
_register("ar", L10N_AR)
