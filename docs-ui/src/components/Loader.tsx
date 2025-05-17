export default function Loader() {
  return (
    <div className="flex justify-center py-10">
      <svg
        className="animate-spin h-6 w-6 text-blue-600"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
      >
        <circle cx="12" cy="12" r="10" strokeWidth="4" className="opacity-25" />
        <path
          d="M22 12a10 10 0 01-10 10"
          strokeWidth="4"
          strokeLinecap="round"
          className="opacity-75"
        />
      </svg>
    </div>
  );
}
