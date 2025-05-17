import { useQuery } from '@tanstack/react-query';
import { get } from '../api/client';

export interface DocDetails {
  document_id: string;
  title?: string;
  type?: string;
  pages?: number;
  text_preview?: string;
  download_url: string;
  thumb_url?: string;
  processing?: boolean;
}

const PUBLIC_MINIO_HOST = 'localhost:9000';

function normalizeUrl(url: string | undefined): string | undefined {
  if (!url) return url;
  return url.replace('minio:9000', PUBLIC_MINIO_HOST);
}

export const useDocument = (id: string) =>
  useQuery({
    queryKey: ['doc', id],
    enabled: !!id,
    queryFn: async () => {
      const doc = await get<DocDetails>(`/search/${id}`);
      return {
        ...doc,
        download_url: normalizeUrl(doc.download_url)!,
        thumb_url: normalizeUrl(doc.thumb_url)
      };
    },
    retry: 1
  });
