# Backend AI Engineering -- Assignment

A lightweight Python backend server built with FastAPI featuring JSON endpoints for product data management. Developed for the **Backend AI Engineering** assignment sequence.

This project has been upgraded from a basic **In-Memory** data structure to a fully containerized **PostgreSQL production-ready architecture** without mutating the core application service and routing layers.

---

## 🚀 FEATURES

- **Robust Layered Architecture:** Decoupled data storage logic via the Repository Pattern.
- **Production-Ready Database:** Fully integrated with PostgreSQL containerized environment.
- **Database Automation:** Automatic schema initialization and data seeding on fresh setups.
- **Secure Configuration:** Environment Variable Management using `.env` parsing to separate secrets from code.
- **Containerization:** Single-command local infrastructure deployment using Docker Compose.

---

## 🛠️ ARCHITECTURAL EVOLUTION (REPOSITORIES)

To comply with strict clean code principles, the application isolates core business logic from database tech stacks:
1. **`InMemoryProductRepository` (Phase 1):** Served data temporarily from local volatile RAM structures.
2. **`PostgresProductRepository` (Phase 2):** Injected seamlessly to handle persistent relational data querying using `psycopg2` raw SQL safely parameters, **requiring zero modifications to your service layers or endpoint handlers.**

---

## 📦 INFRASTRUCTURE & ORCHESTRATION (DOCKER)

The database layer is orchestrated via Docker, maintaining an isolated subnet and volume binding for permanent local storage.

### Data Persistence Architecture
- **`data_for_flyrank` (Volume):** Mounts the container database footprint to the host local disk, guaranteeing that post-shutdown states (`docker compose down`) do not purge operational states.
- **`init.sql` (Automation Seeding):** Mounts directly into the internal PostgreSQL initial entry point (`/docker-entrypoint-initdb.d/`). When deployed on an entirely new machine, it automatically spins up the `products` table structures and plants initial dummy product datasets.

---

## ⚙️ SETTING UP ENVIRONMENT VARIABLES

Sensitive credentials are extracted out of the repository structure. 

1. Create a `.env` file in the project root directory (Refer to `.env.example` for empty structural layouts):
```env
DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
DB_NAME=

---

## ## ENDPOINTS & USAGE
The API provides endpoints to fetch, inspect, and mutate product data in JSON format:

### 1. Get All Products
URL: /

Method: GET

Description: Returns the complete list of all products available in the database (persistently seeded in the PostgreSQL state).

Response Format: JSON Array


### 2. Add New Product
URL: /add_product

Method: POST

Description: Consumes pure data structures safely inside the underlying repository context. Compiles an internal parameterized INSERT INTO query string to guard against SQL Injection vulnerabilities.

Response Format: Success Notification Array / Status Log

## TESTING PERSISTENCE (VERIFICATION)
To prove compliance with persistent storage conditions:

Fire a POST request to /add_product passing custom datasets.

Completely flush your local engine components by running: docker compose down

Bring the architecture back online: docker compose up -d

Query the baseline / GET endpoint. Your newly written entity will persist securely, fetched directly out of the mapped host volume space rather than restarting from flat baseline files.