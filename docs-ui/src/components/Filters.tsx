import React from 'react';
import { useDebounce } from 'use-debounce';
import Select from 'react-select';

export interface FilterState {
  q: string;
  type: string;
  tags: string[];
  dateFrom?: string;
  dateTo?: string;
}

export default function Filters({
  value, onChange,
}: { value: FilterState; onChange: (v: FilterState) => void }) {
  const [search, setSearch] = React.useState(value.q);
  const [debounced] = useDebounce(search, 400);

  React.useEffect(() => {
    onChange({ ...value, q: debounced });
  }, [debounced]);

  return (
    <div className="flex flex-wrap gap-4 mb-6">
      <input
        className="input input-bordered flex-1"
        placeholder="Search…"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <select
        className="select"
        value={value.type}
        onChange={(e) => onChange({ ...value, type: e.target.value })}
      >
        <option value="">All types</option>
        <option value="pdf">PDF</option>
        <option value="docx">DOCX</option>
        <option value="txt">TXT</option>
      </select>

      <input
        type="date"
        className="input"
        value={value.dateFrom ?? ''}
        onChange={(e) => onChange({ ...value, dateFrom: e.target.value })}
      />
      <input
        type="date"
        className="input"
        value={value.dateTo ?? ''}
        onChange={(e) => onChange({ ...value, dateTo: e.target.value })}
      />

      <Select
        isMulti
        className="min-w-[200px]"
        placeholder="Tags…"
        options={[]}
        onChange={(val) =>
          onChange({ ...value, tags: val.map((v) => v.value) })
        }
      />
    </div>
  );
}
