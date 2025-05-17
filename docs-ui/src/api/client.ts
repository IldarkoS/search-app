import axios from 'axios';

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL ?? '',
  timeout: 30_000,
});

api.interceptors.response.use(
  (r) => r,
  (e) => {
    console.error(e);
    throw e;
  },
);

export const get = <T>(url: string) => api.get<T>(url).then((r) => r.data);
export const post = <T>(url: string, body: any, config = {}) =>
  api.post<T>(url, body, config).then((r) => r.data);
