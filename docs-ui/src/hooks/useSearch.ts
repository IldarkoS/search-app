import { useQuery } from '@tanstack/react-query';
import { post } from '../api/client';

export interface SearchItem {
  document_id: string;
  score: number;
  title?: string;
  type?: string;
  pages?: number;
  thumb_url?: string;
}
interface SearchResponse { total: number; results: SearchItem[] }

interface Filters {
  q: string;
  type: string;
  tags: string[];
  dateFrom?: string;
  dateTo?: string;
  page: number;
}

export const useSearch = (f: Filters) =>
  useQuery({
    queryKey: ['search', f],
    enabled: f.q.trim().length > 0,
    queryFn: () => {
      const qs: Record<string, any> = {
        query: f.q.trim(),
        type: f.type || undefined,
        tags: f.tags.length ? f.tags.join(',') : undefined,
        date_from: f.dateFrom || undefined,
        date_to: f.dateTo || undefined,
        limit: 20,
        offset: f.page * 20,
      };
      Object.keys(qs).forEach((k) => (qs[k] == null || qs[k] === '') && delete qs[k]);

      return post<SearchResponse>(`/search/?${new URLSearchParams(qs)}`, {});
    },
    keepPreviousData: true,
  });