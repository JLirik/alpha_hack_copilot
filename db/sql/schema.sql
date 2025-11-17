CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    login VARCHAR(40) UNIQUE NOT NULL,
    password VARCHAR(40) UNIQUE NOT NULL,
    city VARCHAR(40) NOT NULL,
    name TEXT NOT NULL,
    business_about TEXT
);

CREATE TABLE requests_story (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    prompt_in TEXT NOT NULL,
    answer_out TEXT NOT NULL,
    request_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE chunks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    text TEXT,
    embedding VECTOR(384),
    category VARCHAR(50)
);

CREATE TABLE law_base (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    law_name VARCHAR,
    text TEXT,
    code VARCHAR,
    embedding VECTOR(384)
);

CREATE INDEX ON chunks USING hnsw (embedding vector_cosine_ops);

