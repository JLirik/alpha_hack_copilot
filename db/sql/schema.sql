CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    login VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(20) UNIQUE NOT NULL,
    name TEXT NOT NULL,
    business_about TEXT
);

CREATE TABLE requests_story (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    prompt_in TEXT NOT NULL,
    answer_out TEXT NOT NULL,
    request_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
