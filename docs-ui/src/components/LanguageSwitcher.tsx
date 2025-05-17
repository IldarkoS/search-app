import { useTranslation } from 'react-i18next';
export default function LanguageSwitcher() {
  const { i18n } = useTranslation();
  const next = i18n.language === 'ru' ? 'en' : 'ru';
  return (
    <button className="btn btn-ghost btn-sm" onClick={() => i18n.changeLanguage(next)}>
      {next.toUpperCase()}
    </button>
  );
}
