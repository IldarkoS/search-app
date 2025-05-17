import { SearchResult } from '../hooks/useSearch';
import { useTranslation } from 'react-i18next';

function FileIcon({ type }: { type?: string }) {
  const defs = {
    pdf: { color: '#dc2626', label: 'PDF' },
    docx: { color: '#2563eb', label: 'DOCX' },
    txt: { color: '#059669', label: 'TXT' }
  };
  const { color, label } =
    defs[(type ?? 'txt').toLowerCase() as keyof typeof defs] ?? defs.txt;

  return (
    <svg width="32" height="40" viewBox="0 0 24 24" aria-hidden role="img">
      <rect x="4" y="2" width="16" height="20" rx="2" fill={color} />
      <text
        x="12"
        y="15"
        textAnchor="middle"
        fontSize="6"
        fontWeight="bold"
        fill="#fff"
        fontFamily="sans-serif"
      >
        {label}
      </text>
    </svg>
  );
}

export default function DocCard({ item }: { item: SearchResult }) {
  const { t } = useTranslation();

  const meta = `${item.pages ?? '-'} ${t('chars_short')}`;

  return (
    <article className="card bg-base-100 shadow hover:shadow-lg transition flex flex-col">
      <div className="flex justify-center pt-4">
        <FileIcon type={item.type} />
      </div>

      <div className="card-body p-4 gap-2">
        <h3 className="font-medium text-base line-clamp-2">
          {item.title ?? t('untitled')}
        </h3>

        <p className="text-xs text-base-content/60">
          {(item.type ?? 'file').toUpperCase()} · {meta}
        </p>

        <a href={`/doc/${item.document_id}`} className="link link-primary">
          {t('open')} →
        </a>
      </div>
    </article>
  );
}
