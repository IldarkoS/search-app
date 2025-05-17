CREATE TABLE IF NOT EXISTS documents (
    id          UUID PRIMARY KEY,
    title       TEXT,
    type        TEXT,
    pages       INT,
    text_preview TEXT,
    file_path   TEXT NOT NULL,
    uploaded_at TIMESTAMPTZ DEFAULT now()
);