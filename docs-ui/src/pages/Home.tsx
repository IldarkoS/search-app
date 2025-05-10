import React from 'react';
import Filters, { FilterState } from '../components/Filters';
import { useSearch } from '../hooks/useSearch';

export default function Home() {
  const [filters, setFilters] = React.useState<FilterState>({
    q: '',
    type: '',
    tags: [],
    page: 0,
  } as any);

  const { data, isFetching } = useSearch(filters);

  return (
    <main className="container mx-auto px-6 py-8">
      <Filters value={filters} onChange={(v) => setFilters({ ...v, page: 0 })} />

      {isFetching && <p className="my-4">Loading…</p>}

      <pre className="bg-gray-100 p-4 rounded">
        {JSON.stringify(data ?? {}, null, 2)}
      </pre>
    </main>
  );
}
