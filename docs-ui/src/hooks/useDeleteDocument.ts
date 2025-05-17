import { useMutation } from '@tanstack/react-query';
import { api } from '../api/client';

export const useDeleteDocument = () =>
  useMutation({
    mutationFn: async (id: string) => {
      await api.delete(`/search/${id}/delete/`);
    }
  });