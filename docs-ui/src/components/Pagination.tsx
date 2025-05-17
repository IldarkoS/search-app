import Button from './Button';
export default function Pagination({
  page,
  total,
  perPage,
  onChange,
}: {
  page: number;
  total: number;
  perPage: number;
  onChange: (p: number) => void;
}) {
  const last = Math.max(0, Math.ceil(total / perPage) - 1);
  if (total <= perPage) return null;
  return (
    <div className="flex justify-center items-center gap-4 my-8">
      <Button variant="secondary" onClick={() => onChange(page - 1)} disabled={page === 0}>
        ←
      </Button>
      <span>
        {page + 1}/{last + 1}
      </span>
      <Button variant="secondary" onClick={() => onChange(page + 1)} disabled={page >= last}>
        →
      </Button>
    </div>
  );
}
