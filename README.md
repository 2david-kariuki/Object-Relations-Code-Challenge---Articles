# Articles Code Challenge

A Python-based system designed to manage Authors, Articles, and their relationships. This project demonstrates the implementation of relational mappings and SQL queries using Python.

## Table of Contents

* [Features](#features)
* [Setup](#setup)
* [Running the Tests](#running-the-tests)
* [Technologies Used](#technologies-used)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

## Features

* **Author Management:** Create, read, update, and delete authors.
* **Article Management:** Create, read, update, and delete articles.
* **Relational Mappings:** Efficiently manage relationships between authors and articles.
* **SQL Queries:** Execute robust SQL queries for data retrieval and manipulation.
* **Interactive CLI:** A command-line interface for interacting with the database.

## Setup

Follow these steps to get your development environment set up and running:

1.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
2.  **Activate the virtual environment:**
    * On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    * On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (Ensure you have a `requirements.txt` file listing all project dependencies.)

4.  **Set up the database:**
    ```bash
    python -m venv scripture
    ```
    (This step seems unusual based on the screenshot. Please verify if `python -m venv scripture` is the correct command for setting up the database, or if it refers to something else. Often, database setup might involve migration commands like `python scriptname.py migrate` or similar. Adjust as needed.)

5.  **Seed the database (Optional but recommended):**
    ```bash
    python seed.py
    ```
    (This will populate your database with sample data for testing.)

6.  **Run queries (for interactive use):**
    ```bash
    python src/scripts/run_queries.py
    ```

7.  **Interactive CLI:**
    ```bash
    python src/scripts/cli.py
    ```
    (This launches the command-line interface for interacting with the application.)

8.  **Debugging:**
    ```bash
    python lib/debug.py
    ```
    

## Running the Tests

To ensure everything is working as expected, run the following tests:

1.  **Database setup and seeding tests:**
    ```bash
    python scripts/setup_db.py && python lib/seed.py && python scripts/run_queries.py
    ```
    (This command combines database setup, seeding, and running queries, likely as a comprehensive test.)

2.  **Debugging tests:**
    ```bash
    python lib/debug.py
    ```
    (This is likely a dedicated script for testing debugging functionalities.)

## Technologies Used

* **Python 3.x**
* **SQLAlchemy** (or other ORM if applicable, specify here)
* **SQLite** (or other database, specify here)
* (Add any other significant libraries or frameworks used)

## Contributing

We welcome contributions! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeatureName`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/YourFeatureName`).
6.  Open a Pull Request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the [MIT License](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for details.
