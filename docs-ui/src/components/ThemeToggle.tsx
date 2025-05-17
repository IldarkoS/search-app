import { useEffect, useState } from 'react';

export default function ThemeToggle() {
  const getInitial = () =>
    (localStorage.getItem('theme') as 'light' | 'dark' | null) ?? 'light';

  const [theme, setTheme] = useState<'light' | 'dark'>(getInitial);

  useEffect(() => {
    const html = document.documentElement;
    html.dataset.theme = theme;
    html.classList.toggle('dark', theme === 'dark');
    localStorage.setItem('theme', theme);
  }, [theme]);

  return (
    <button
      type="button"
      className="btn btn-ghost btn-sm"
      onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
      title="Toggle theme"
    >
      {theme === 'dark' ? '☀️' : '🌙'}
    </button>
  );
}
