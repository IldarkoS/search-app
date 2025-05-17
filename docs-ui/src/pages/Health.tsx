import { useQuery } from '@tanstack/react-query';
import { get } from '../api/client';
import Loader from '../components/Loader';
import { useTranslation } from 'react-i18next';

interface HealthResponse {
  status: string;
}

export default function Health() {
  const { t } = useTranslation();

  const { data, isLoading, isError } = useQuery({
    queryKey: ['health'],
    queryFn: () => get<HealthResponse>('/health/')
  });

  if (isLoading) return <Loader />;

  return (
    <main className="container mx-auto px-6 py-8">
      <h1 className="text-2xl font-semibold mb-6">{t('health')}</h1>

      {isError || !data || data.status !== 'ok' ? (
        <p className="text-lg text-error">{t('health_fail')}</p>
      ) : (
        <p className="text-lg text-success">{t('health_ok')}</p>
      )}
    </main>
  );
}
