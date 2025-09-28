from __future__ import annotations
from locales.core import _register, BTN_SUPPORT, BTN_ABOUT, BTN_CHANGE_COUNTRY, BTN_MY_APPS, BTN_APPLY, BTN_BACK

L10N_FR = {
    "prompt_choose_region": "🌍 Sélectionnez la région pour votre demande :",
    "prompt_choose_country": "🌍 Sélectionnez votre pays :",
    "after_country_selected": "✅ Parfait, pays sélectionné.\n Vous pouvez maintenant soumettre une demande, en savoir plus sur le service ou modifier vos paramètres.",
    "menu_title": "🧭 WorldFlow Credit — votre navigateur financier. Choisissez votre direction : demande, support, informations ou vos dossiers.",
    "btn_apply": "📝 Déposer une demande",
    "apply_text": "C’est parti. Un code d’accès personnel peut être saisi à la première étape.",
    "btn_support": "🛟 Support",
    "btn_about": "ℹ️ À propos",
    "btn_change_country": "🌐 Changer de pays",
    "btn_my_apps": "🗂 Mes demandes",
    "my_applications_text": (
        "<b>🗂 Mes demandes</b>\n\n"
        "Vos demandes actives apparaîtront ici : statut, documents, commentaires et chat avec un conseiller.\n"
    ),
    "support_text": (
        "<b>💬 Assistance WorldFlow Credit</b>\n\n"
        "Nous sommes là pour accélérer vos décisions :\n"
        "— résoudre les situations complexes,\n"
        "— indiquer les meilleures étapes,\n"
        "— vous mettre en relation avec le bon spécialiste.\n\n"
        "📲 Votre canal d’assistance personnel : <b>@WorldFlowSupport</b>"
    ),
    "about_text": "WorldFlow Credit — service international de demande de crédit.",
    "my_apps_stub": "Vos demandes apparaîtront ici (bientôt).",
    "back_to_region": (
        "<b>↩️ Changer de région et continuer 🌐</b>\n\n"
        "💡 Indiquez le pays où vous vous trouvez actuellement — "
        "ainsi nous vous proposerons les produits et formulaires les plus pertinents."
    ),
    "btn_back": "↩ Retour",
    "btn_website": "Site web",
    "btn_tg_channel": "Chaîne Telegram",
    "btn_instagram": "Instagram",
    "btn_x": "X / Twitter",
    "btn_linkedin": "LinkedIn",
    "btn_youtube": "YouTube",

    "ui": {
        "preview_title": "Avancement de la demande",
        "step": "Champ",
        "status": "Statut",
        "value": "Valeur",
        "done": "✅ Terminé",
        "todo": "❌ À compléter",
        "share_phone": "📲 Partager le numéro",
        "type_manually": "✏️ Entrer manuellement",
        "completed_demo": "Le formulaire a été rempli avec succès ✅",
    },

    "about_full": (
        "<b>🌍 WorldFlow Credit — une plateforme fintech mondiale dédiée au crédit.</b>\n\n"
        "Nous connectons les clients directement aux banques, grâce à des solutions digitales et à l’expertise d’un réseau international "
        "de courtiers, analystes et conseillers financiers. Avec nous, le processus devient simple, transparent et rapide.\n\n"
        "💼 Notre écosystème rassemble des milliers de spécialistes et de partenaires dans le monde entier, travaillant au sein de l’espace numérique WorldFlow. "
        "Nous associons technologie bancaire et conseil financier pour garantir un traitement fluide des demandes.\n\n"
        "<b>✅ Nous proposons :</b>\n"
        "— 💳 crédits à la consommation, hypothécaires et automobiles en ligne ;\n"
        "— 💼 accompagnement digital des entreprises (auto-entrepreneurs / sociétés), croissance du chiffre d’affaires et conformité ;\n"
        "— 📊 outils de préparation au scoring de crédit pour maximiser vos chances d’approbation ;\n"
        "— 🤝 suivi personnalisé à chaque étape — de la demande au financement.\n\n"
        "⚡️ <b>Avec WorldFlow Credit, vous accédez non seulement à des produits financiers, "
        "mais à un véritable outil de banque digitale, adapté à vos objectifs.</b>"
    ),

    "steps_by_country": {
        "FR": {
            "phone": "📞 Indiquez votre numéro de mobile au format +33XXXXXXXXX.",
            "id_number": "🆔 Indiquez votre numéro de sécurité sociale (INSEE).",
            "dob": "📅 Veuillez indiquer votre date de naissance au format JJ/MM/AAAA.",
        }
    },

    "labels": {
        "access_code": "Code d’accès",
        "full_name": "Nom complet",
        "phone": "Téléphone",
        "email": "E-mail",
        "loan_amount": "Montant du prêt",
        "id_number": "Identifiant",
        "inn_ru": "INN (Russie uniquement)",
        "reg_address": "Adresse enregistrée",
        "actual_address": "Adresse actuelle",
        "dob": "Date de naissance",
        "marital_status": "État civil",
        "workplace": "Employeur",
    },
}

L10N_FR.update({
    BTN_SUPPORT: L10N_FR["btn_support"],
    BTN_ABOUT: L10N_FR["btn_about"],
    BTN_CHANGE_COUNTRY: L10N_FR["btn_change_country"],
    BTN_MY_APPS: L10N_FR["btn_my_apps"],
    BTN_APPLY: L10N_FR["btn_apply"],
    BTN_BACK: L10N_FR["btn_back"],
})
_register("fr", L10N_FR)

__all__ = ["L10N_FR"]