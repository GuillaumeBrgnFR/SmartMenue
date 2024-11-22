import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';

// Traductions
const resources = {
  en: {
    translation: {
      menuTitle: "Menu",
      importMenu: "Import Menu",
      edit: "Edit",
      save: "Save",
      generateQRCode: "Generate QR Code",
    },
  },
  fr: {
    translation: {
      menuTitle: "Menu",
      importMenu: "Importer un menu",
      edit: "Édition",
      save: "Sauvegarder",
      generateQRCode: "Générer le QR Code",
    },
  },
  es: {
    translation: {
      menuTitle: "Menú",
      importMenu: "Importar menú",
      edit: "Editar",
      save: "Guardar",
      generateQRCode: "Generar código QR",
    },
  },
};

i18n
  .use(LanguageDetector) // Détecte automatiquement la langue du navigateur
  .use(initReactI18next) // Intègre i18next avec React
  .init({
    resources,
    fallbackLng: 'en', // Langue par défaut
    interpolation: {
      escapeValue: false, // React gère déjà l'échappement
    },
  });

export default i18n;