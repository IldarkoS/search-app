const API = import.meta.env.VITE_API_URL ?? '';

export const get = <T>(url: string, params: Record<string, any> = {}) => {
  const clean: Record<string, any> = {};
  Object.entries(params).forEach(([k, v]) => {
    if (v !== undefined && v !== null && v !== '') clean[k] = v;
  });
  return fetch(`${API}${url}?${new URLSearchParams(clean)}`).then(
    (r) => r.json() as Promise<T>,
  );
};

export const post = <T>(url: string, body: any) =>
  fetch(`${API}${url}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  }).then((r) => r.json() as Promise<T>);
