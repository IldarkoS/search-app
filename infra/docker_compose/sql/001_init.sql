CREATE TABLE IF NOT EXISTS documents (
    id          UUID PRIMARY KEY,
    title       TEXT,
    type        TEXT,
    pages       INT,
    file_path   TEXT NOT NULL,
    uploaded_at TIMESTAMPTZ DEFAULT now()
);