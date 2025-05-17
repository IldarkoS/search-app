import { useState, useEffect, useRef } from 'react';
import { useDebounce } from 'use-debounce';
import { useSearch } from '../hooks/useSearch';
import DocCard from '../components/DocCard';
import Loader from '../components/Loader';
import Pagination from '../components/Pagination';
import Button from '../components/Button';
import QueryHistory from '../components/QueryHistory';
import { useTranslation } from 'react-i18next';
import { Link } from 'react-router-dom';

const HISTORY_KEY = 'recent_queries';
const MAX_HISTORY = 10;

export default function Home() {
  const { t } = useTranslation();

  const [query, setQuery] = useState('');
  const [file, setFile] = useState<File | null>(null);
  const [debounced] = useDebounce(query, 400);
  const [page, setPage] = useState(0);

  /* ---- поиск ---- */
  const startRef = useRef<number | null>(null);
  const [elapsed, setElapsed] = useState<number | null>(null);
  const { data, isLoading } = useSearch(debounced, page, file);

  useEffect(() => {
    if (isLoading) {
      startRef.current = Date.now();
      setElapsed(null);
    } else if (startRef.current) {
      setElapsed(Date.now() - startRef.current);
      startRef.current = null;
      if (debounced.trim()) addToHistory(debounced.trim());
    }
  }, [isLoading]);

  /* ---- история ---- */
  const [history, setHistory] = useState<string[]>(() => {
    const raw = localStorage.getItem(HISTORY_KEY);
    return raw ? JSON.parse(raw) : [];
  });
  const addToHistory = (q: string) => {
    const next = [q, ...history.filter((x) => x !== q)].slice(0, MAX_HISTORY);
    setHistory(next);
    localStorage.setItem(HISTORY_KEY, JSON.stringify(next));
  };
  const clearHistory = () => {
    setHistory([]);
    localStorage.removeItem(HISTORY_KEY);
  };

  return (
    <main className="container mx-auto px-6 py-8">
      <div className="flex justify-end gap-2 mb-4">
        <Link to="/health">
          <Button variant="success">{t('health')}</Button>
        </Link>
      </div>

      <input
        className="input input-bordered w-full mb-4"
        placeholder={t('search_placeholder')}
        value={query}
        onChange={(e) => {
          setQuery(e.target.value);
          setFile(null);
          setPage(0);
        }}
      />

      <div className="flex items-center gap-4 mb-6">
        <label className="btn btn-primary btn-sm">
          {t('file_btn')}
          <input
            type="file"
            hidden
            accept=".pdf,.docx,.txt"
            onChange={(e) => {
              const f = e.target.files?.[0] ?? null;
              setFile(f);
              setQuery('');
              setPage(0);
            }}
          />
        </label>

        {file && (
          <span className="text-sm">
            {t('file_chosen', { name: file.name })}
          </span>
        )}
      </div>

      <QueryHistory
        items={history}
        onSelect={(q) => {
          setQuery(q);
          setFile(null);
          setPage(0);
        }}
        onClear={clearHistory}
      />

      {elapsed != null && (
        <p className="text-sm mb-4">
          {t('search_time')}: <span className="font-medium">{elapsed} ms</span>
        </p>
      )}

      {isLoading && <Loader />}

      {data && data.results.length > 0 && (
        <>
          <div className="grid gap-6 md:grid-cols-3 lg:grid-cols-4">
            {data.results.map((r) => (
              <DocCard key={r.document_id} item={r} />
            ))}
          </div>
          <Pagination
            page={page}
            perPage={20}
            total={data.total}
            onChange={setPage}
          />
        </>
      )}
    </main>
  );
}
