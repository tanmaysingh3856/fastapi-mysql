## FastAPI with MYSQL

FastAPI repository that uses MYSQL and Alembic.

### Getting Started

1. Setup Poetry

   Create the poetry environment

   ```
   poetry env use 3.11
   ```

   Start the poetry shell

   ```
   poetry shell
   ```

2. Install dependencies:

   ```
   poetry install
   ```

3. Create a `.env` file and input environment variables.

4. Initialize database tables:

   ```
   alembic upgrade head
   ```

5. Start the application in development mode:

   ```
   poetry run dev
   ```

6. Test the application by making requests to endpoints.

For detailed information, refer to the following resources:

- FastAPI documentation: https://fastapi.tiangolo.com/
- Alembic documentation: https://alembic.sqlalchemy.org/en/latest/
- Poetry documentation: https://python-poetry.org/docs/
