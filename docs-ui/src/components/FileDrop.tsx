import { useState, useRef } from 'react';
import { useUpload } from '../hooks/useUpload';
import { toast } from 'react-toastify';
import { useTranslation } from 'react-i18next';

export default function FileDrop({
  onUploaded
}: {
  onUploaded: (id: string) => void;
}) {
  const { t } = useTranslation();
  const { upload } = useUpload();
  const [isDragging, setDragging] = useState(false);
  const inputRef = useRef<HTMLInputElement | null>(null);

  const handleFiles = async (files: FileList | null) => {
    const file = files?.[0];
    if (!file) return;

    if (!/\.(pdf|docx|txt)$/i.test(file.name)) {
      toast.error('Unsupported file type');
      return;
    }

    try {
      const id = await upload(file);
      toast.success('Uploaded');
      onUploaded(id);
    } catch {
      /* error toast уже показан в useUpload */
    }
  };

  return (
    <section
      onDragOver={(e) => {
        e.preventDefault();
        e.dataTransfer.dropEffect = 'copy';
      }}
      onDragEnter={(e) => {
        e.preventDefault();
        setDragging(true);
      }}
      onDragLeave={(e) => {
        e.preventDefault();
        setDragging(false);
      }}
      onDrop={(e) => {
        e.preventDefault();
        setDragging(false);
        handleFiles(e.dataTransfer.files);
      }}
      className={
        'border-2 border-dashed rounded p-10 text-center cursor-pointer transition ' +
        (isDragging
          ? 'border-blue-500 bg-blue-50'
          : 'border-gray-300 bg-transparent')
      }
      onClick={() => inputRef.current?.click()}
    >
      <input
        ref={inputRef}
        type="file"
        accept=".pdf,.docx,.txt"
        className="hidden"
        onChange={(e) => handleFiles(e.target.files)}
      />

      <p className="select-none">
        {isDragging ? t('drop_prompt') : t('drag_prompt')}
      </p>
    </section>
  );
}
