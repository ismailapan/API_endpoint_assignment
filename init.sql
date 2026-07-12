DROP TABLE IF EXISTS products;

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(100),
    price NUMERIC(10,2) NOT NULL,
    stock INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products(name, category, price, stock) VALUES
('MacBook Pro M3', 'Computer', 85000.00, 10),
('iPhone 15 Pro', 'Phone',72000.00, 15),
('AirPods Pro 2', 'Headphones', 9500.00, 40);