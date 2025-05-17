import { useState } from 'react';
import { Link } from 'react-router-dom';
import FileDrop from '../components/FileDrop';
import { useTranslation } from 'react-i18next';

export default function Upload() {
  const { t } = useTranslation();
  const [done, setDone] = useState(false);

  return (
    <main className="container mx-auto px-6 py-8">
      <h1 className="text-2xl font-semibold mb-6">{t('upload')}</h1>

      {done ? (
        <div className="space-y-4">
          <p>{t('processing')}</p>
          <Link to="/" className="btn btn-primary">
            {t('back_home')}
          </Link>
        </div>
      ) : (
        <FileDrop onUploaded={() => setDone(true)} />
      )}
    </main>
  );
}
