import classNames from 'classnames';

export default function Button({
  children,
  href,
  onClick,
  variant = 'primary',
  disabled = false
}: {
  children: React.ReactNode;
  href?: string;
  onClick?: () => void;
  variant?: 'primary' | 'secondary' | 'success' | 'error';
  disabled?: boolean;
}) {
  const base =
    'btn btn-sm text-white dark:text-black transition-colors border-0';

  const cls = classNames(
    base,
    variant === 'primary' && 'bg-blue-600 hover:bg-blue-700',
    variant === 'secondary' && 'bg-gray-300 hover:bg-gray-400 text-black',
    variant === 'success' && 'bg-green-600 hover:bg-green-700',
    variant === 'error' && 'bg-red-600 hover:bg-red-700',
    disabled && 'opacity-50 pointer-events-none'
  );

  return href ? (
    <a href={href} className={cls}>
      {children}
    </a>
  ) : (
    <button type="button" className={cls} onClick={onClick} disabled={disabled}>
      {children}
    </button>
  );
}
