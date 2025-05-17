import { useState } from 'react';
import { post } from '../api/client';
import { toast } from 'react-toastify';

export const useUpload = () => {
  const [progress, setProgress] = useState<number | null>(null);

  const upload = async (file: File) => {
    try {
      setProgress(0);

      const form = new FormData();
      form.append('file', file);
      const res = await post<{ document_id: string; status: string }>('/upload/', form, {
        headers: { 'Content-Type': 'multipart/form-data' },
        onUploadProgress: (e: ProgressEvent) =>
          setProgress(Math.round(((e.loaded || 0) * 100) / (e.total || 1))),
      });

      toast.info('Загружено, документ обрабатывается…');
      return res.document_id;
    } catch (e) {
      toast.error('Ошибка загрузки');
      throw e;
    } finally {
      setProgress(null);
    }
  };

  return { upload, progress };
};
