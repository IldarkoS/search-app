import { useTranslation } from 'react-i18next';
import Button from './Button';

export default function QueryHistory({
  items,
  onSelect,
  onClear
}: {
  items: string[];
  onSelect: (q: string) => void;
  onClear: () => void;
}) {
  const { t } = useTranslation();
  if (items.length === 0) return null;

  return (
    <div className="mb-6 space-y-2">
      <div className="flex justify-between items-center">
        <span className="font-medium">{t('recent_queries')}</span>
        <Button variant="secondary" onClick={onClear}>
          {t('clear_history')}
        </Button>
      </div>

      <div className="flex flex-wrap gap-2">
        {items.map((q) => (
          <Button
            key={q}
            variant="secondary"
            onClick={() => onSelect(q)}
            extraClasses="truncate max-w-xs"
          >
            {q}
          </Button>
        ))}
      </div>
    </div>
  );
}
