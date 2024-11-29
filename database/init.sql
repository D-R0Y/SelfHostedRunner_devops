CREATE TABLE IF NOT EXISTS app_info (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

INSERT INTO app_info (name, description) 
VALUES ('DevOps Demo', 'Simple Flask App with PostgreSQL')
ON CONFLICT DO NOTHING;
