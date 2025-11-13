CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    login VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(20) UNIQUE NOT NULL,
    name TEXT NOT NULL,
    business_about TEXT
);

CREATE TABLE requests_story (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    prompt_in TEXT NOT NULL,
    answer_out TEXT NOT NULL,
    request_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE chunks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    text TEXT,
    embedding VECTOR(384),
    category VARCHAR(50),
    metadata JSONB
);

CREATE TABLE vacancies (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    responsibilities JSONB NOT NULL,
    requirements JSONB NOT NULL,
    conditions TEXT NOT NULL,
    salary INT NOT NULL,
    work_type TEXT NULL,
    contact VARCHAR NOT NULL
);

CREATE INDEX ON chunks USING hnsw (embedding vector_cosine_ops);

