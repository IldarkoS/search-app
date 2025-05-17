import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Upload from './pages/Upload';
import Doc from './pages/Doc';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import LanguageSwitcher from './components/LanguageSwitcher';
import ThemeToggle from './components/ThemeToggle';
import { useTranslation } from 'react-i18next';
import Health from './pages/Health';
import ThemeSelector from './components/ThemeSelector';

export default function App() {
  const { t } = useTranslation();

  return (
    <>
      <BrowserRouter>
        <div className="min-h-screen flex flex-col">
          <header className="navbar bg-base-100 border-b px-4">
            <a href="/" className="btn btn-ghost normal-case text-xl">
              {t('title')}
            </a>

            <div className="flex-1" />

            {/*<ThemeToggle />*/}
            <LanguageSwitcher />
            <ThemeSelector />

            <a href="/upload" className="btn btn-primary btn-sm ml-2">
              {t('upload_btn')}
            </a>
          </header>

          <main className="flex-1">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/upload" element={<Upload />} />
              <Route path="/doc/:id" element={<Doc />} />
              <Route path="/health" element={<Health />} />
            </Routes>
          </main>

          <footer className="footer p-4 bg-base-200 text-xs justify-center">
            © 2025
          </footer>
        </div>
      </BrowserRouter>

      <ToastContainer position="bottom-right" />
    </>
  );
}
