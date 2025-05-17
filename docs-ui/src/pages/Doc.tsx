import { useNavigate, useParams } from 'react-router-dom';
import { useDocument } from '../hooks/useDocument';
import Loader from '../components/Loader';
import Button from '../components/Button';
import { useTranslation } from 'react-i18next';
import { useDeleteDocument } from '../hooks/useDeleteDocument';
import { toast } from 'react-toastify';
import Swal from 'sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

export default function Doc() {
  const { t } = useTranslation();
  const nav = useNavigate();
  const { id = '' } = useParams();

  const { data, isLoading, isError } = useDocument(id);
  const deleteDoc = useDeleteDocument();

  const handleDelete = async () => {
    if (!id) return;

    const res = await Swal.fire({
      title: t('delete_btn') + '?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: t('delete_btn'),
      cancelButtonText: 'Cancel',
      confirmButtonColor: '#d33'
    });

    if (!res.isConfirmed) return;

    try {
      await deleteDoc.mutateAsync(id);
      toast.success('Deleted');
      nav('/');
    } catch {
      toast.error('Delete failed');
    }
  };

  if (isLoading) return <Loader />;
  if (isError || !data)
    return (
      <p className="text-center py-10 text-red-600">
        Не удалось загрузить документ
      </p>
    );

  return (
    <main className="container mx-auto px-6 py-8 space-y-6">
      <div className="flex justify-between items-center gap-2 flex-wrap">
        <h1 className="text-2xl font-semibold">{data.title ?? 'Untitled'}</h1>

        <div className="flex gap-2">
          {data.download_url && (
            <Button href={data.download_url}>{t('downloading')}</Button>
          )}

          <Button
            variant="error"
            onClick={handleDelete}
            disabled={deleteDoc.isPending}
          >
            {t('delete_btn')}
          </Button>
        </div>
      </div>

      {data.text_preview ? (
        <>
          <h2 className="font-medium">{t('text_preview')}</h2>
          <pre className="whitespace-pre-wrap bg-base-200 p-4 rounded max-h-[80vh] overflow-auto">
            {data.text_preview}
          </pre>
        </>
      ) : (
        <p className="italic">{t('preview_unavailable')}</p>
      )}
    </main>
  );
}
