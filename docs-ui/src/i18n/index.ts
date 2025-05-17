import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';

const resources = {
  ru: {
    translation: {
      title: 'Сервис поиска документов',
      search_placeholder: 'Поиск документов…',
      search_time: 'Время поиска',
      recent_queries: 'Недавние запросы',
      clear_history: 'Очистить',
      upload: 'Загрузка',
      upload_btn: 'Загрузить',
      downloading: 'Скачать',
      processing: 'Файл отправлен на обработку…',
      preview_unavailable: 'Превью недоступно',
      pages_short: 'стр.',
      chars_short: 'символов',
      open: 'Открыть',
      untitled: 'Без названия',
      back_home: 'Вернуться на главную',
      text_preview: 'Превью текста файла',
      delete_btn: 'Удалить документ',
      health: 'Статус',
      health_ok: 'Приложение работает в штатном режиме',
      health_fail: 'Сервис недоступен',
      theme: 'Тема',
      drag_prompt: 'Перетащите PDF, DOCX или TXT сюда или кликните, чтобы выбрать',
      drop_prompt: 'Бросьте файл…',
      file_btn: 'Поиск по файлу',
      file_chosen: 'Файл: {{name}}',
    }
  },
  en: {
    translation: {
      title: 'Document Search Service',
      search_placeholder: 'Search documents…',
      search_time: 'Search time',
      recent_queries: 'Recent queries',
      clear_history: 'Clear',
      upload: 'Upload',
      upload_btn: 'Upload',
      downloading: 'Download',
      processing: 'File sent for processing…',
      preview_unavailable: 'Preview unavailable',
      pages_short: 'pages',
      chars_short: 'chars',
      open: 'Open',
      untitled: 'Untitled',
      back_home: 'Back to home',
      text_preview: 'File text preview',
      delete_btn: 'Delete document',
      health: 'Status',
      health_ok: 'Application is running normally',
      health_fail: 'Service unavailable',
      theme: 'Theme',
      drag_prompt: 'Drag & drop PDF, DOCX or TXT here or click to select',
      drop_prompt: 'Drop the file…',
      file_btn: 'Search by file',
      file_chosen: 'File: {{name}}',
    }
  }
};

i18n.use(LanguageDetector).use(initReactI18next).init({
  resources,
  fallbackLng: 'ru',
  interpolation: { escapeValue: false }
});

export default i18n;
