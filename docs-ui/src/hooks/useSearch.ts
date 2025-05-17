import { useQuery } from '@tanstack/react-query';
import { api } from '../api/client';

export interface SearchResult {
  document_id: string;
  score: number;
  title?: string;
  type?: string;
  pages?: number;
  thumb_url?: string;
}
export interface SearchResponse {
  total: number;
  results: SearchResult[];
}

export const useSearch = (
  text: string,
  page: number,
  file?: File | null
) =>
  useQuery({
    queryKey: ['search', text, page, file?.name],
    enabled: (!!text.trim() || !!file) && page >= 0,
    queryFn: async () => {
      const qs = new URLSearchParams();
      if (text.trim()) qs.append('query', text.trim());
      qs.append('limit', '20');
      qs.append('offset', String(page * 20));

      const form = new FormData();
      if (file) form.append('file', file);

      const { data } = await api.post<SearchResponse>(`/search/?${qs}`, form);
      return data;
    },
    retry: 1
  });
