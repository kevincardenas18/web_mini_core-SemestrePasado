# Environment variables

## Description

Environment variables are useful for storing sensitive information, such as passwords, API keys, and more. In this project, environment variables are used to store the database credentials and the secret key for the Django project.

## Project environment variables

The following environment variables must be configured in the `.env` file inside the `web_mini_core` folder:

- `SECRET_KEY`: The secret key for the Django project (you can generate one [here](https://djecrety.ir/)).
- `DEBUG`: Whether the project is in debug mode or not (set to `True` or `False`). If you are in development, set this to `True`. If you are in production, set this to `False`.
- `DB_NAME`: The name of the database (e.g. `minicore_db`).
- `DB_USER`: The username of the database (e.g. `postgres`).
- `DB_PASSWORD`: The password of the database.
- `DB_HOST`: The host of the database (e.g. `localhost`).
- `DB_PORT`: The port of the database (commonly `5432`).

If you cloned the repository, you can copy the `.env.example` file, rename it to `.env` and configure the environment variables.

> **Note:** The `.env` file is ignored by Git, so you don't need to worry about exposing your credentials.
