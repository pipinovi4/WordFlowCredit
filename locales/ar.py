from __future__ import annotations
from locales.core import _register, BTN_SUPPORT, BTN_ABOUT, BTN_CHANGE_COUNTRY, BTN_MY_APPS, BTN_APPLY, BTN_BACK

L10N_AR = {
    "prompt_choose_region": "🌍 اختر المنطقة لتقديم طلبك:",
    "prompt_choose_country": "🌍 اختر دولتك:",
    "after_country_selected": "✅ تم اختيار الدولة بنجاح.\n يمكنك الآن تقديم طلب، معرفة المزيد عن الخدمة، أو تعديل الإعدادات الخاصة بك.",
    "menu_title": "🧭 WorldFlow Credit — دليلك المالي. اختر الاتجاه: تقديم طلب، الدعم، المعلومات أو طلباتك.",
    "btn_apply": "📝 تقديم طلب",
    "apply_text": "لنبدأ. يمكنك إدخال رمز وصول شخصي في الخطوة الأولى.",
    "btn_support": "🛟 الدعم",
    "btn_about": "ℹ️ من نحن",
    "btn_change_country": "🌐 تغيير الدولة",
    "btn_my_apps": "🗂 طلباتي",
    "my_applications_text": (
        "<b>🗂 طلباتي</b>\n\n"
        "ستظهر طلباتك النشطة هنا: الحالة، المستندات، التعليقات والدردشة مع خبير.\n"
    ),
    "support_text": (
        "<b>💬 دعم WorldFlow Credit</b>\n\n"
        "نحن هنا لتسريع قراراتك:\n"
        "— حل المواقف المعقدة،\n"
        "— اقتراح الخطوات المثلى،\n"
        "— ربطك بالخبير المناسب.\n\n"
        "📲 قناتك الشخصية للدعم: <b>@WorldFlowSupport</b>"
    ),
    "about_text": "WorldFlow Credit — خدمة دولية لتقديم طلبات الائتمان.",
    "my_apps_stub": "ستظهر طلباتك هنا (قريبًا).",
    "back_to_region": (
        "<b>↩️ غيّر المنطقة وتابع 🌐</b>\n\n"
        "💡 اختر الدولة التي تتواجد فيها حالياً — "
        "حتى نعرض لك المنتجات والنماذج الأكثر ملاءمة."
    ),
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
        "<b>🌍 WorldFlow Credit — منصة فينتك عالمية للتمويل.</b>\n\n"
        "نربط العملاء مباشرة بالبنوك باستخدام الحلول الرقمية وخبرة الوسطاء والمحللين والمستشارين الدوليين. "
        "معنا تصبح العملية بسيطة وشفافة وسريعة.\n\n"
        "💼 نظامنا البيئي يجمع بين آلاف المتخصصين والشركاء حول العالم، الذين يعملون ضمن الفضاء الرقمي لـ WorldFlow. "
        "نحن ندمج التكنولوجيا المصرفية مع الاستشارات المالية لضمان معالجة طلباتكم بسلاسة.\n\n"
        "<b>✅ نقدم:</b>\n"
        "— 💳 قروض استهلاكية وعقارية وسيارات عبر الإنترنت؛\n"
        "— 💼 دعم رقمي للأعمال (الملكية الفردية / الشركات)، وتنمية الإيرادات، والامتثال؛\n"
        "— 📊 أدوات التحضير للتقييم الائتماني وزيادة فرص الموافقة؛\n"
        "— 🤝 دعم شخصي في كل مرحلة — من تقديم الطلب إلى التمويل.\n\n"
        "⚡️ <b>مع WorldFlow Credit، لا تحصل فقط على منتجات مالية، بل على أداة مصرفية رقمية متكاملة.</b>"
    )
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

__all__ = ["L10N_AR"]