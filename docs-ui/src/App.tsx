import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/upload" element={<p>Upload page…</p>} />
        <Route path="/doc/:id" element={<p>Doc page…</p>} />
      </Routes>
    </BrowserRouter>
  );
}
