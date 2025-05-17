import { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import Button from './Button';

const THEMES = ['light', 'dark', 'cupcake', 'emerald'] as const;
type Theme = (typeof THEMES)[number];

export default function ThemeSelector() {
  const { t } = useTranslation();
  const [theme, setTheme] = useState<Theme>(
    (localStorage.getItem('theme') as Theme) ?? 'light'
  );

  useEffect(() => {
    const html = document.documentElement;
    html.dataset.theme = theme;
    html.classList.toggle('dark', theme === 'dark');
    localStorage.setItem('theme', theme);
  }, [theme]);

  return (
    <div className="dropdown dropdown-end">
      <Button variant="secondary" asChild>
        <label tabIndex={0} className="cursor-pointer">
          {t('theme')}
        </label>
      </Button>

      <ul
        tabIndex={0}
        className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-40"
      >
        {THEMES.map((th) => (
          <li key={th}>
            <button
              className={theme === th ? 'active' : ''}
              onClick={() => setTheme(th)}
            >
              {th}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
