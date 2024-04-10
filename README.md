# Point of Sales System

## Overview

This Point of Sales (POS) system is developed using Python Django framework and Django Rest Framework for the backend, Vue.js for the frontend, and PostgreSQL as the database. It utilizes Poetry for package management.

## Installation

### Poetry

Poetry is used for managing Python dependencies. If you haven't installed Poetry yet, you can do so by following the instructions at [Poetry Installation](https://python-poetry.org/docs/#installation).

### Backend Setup

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the backend directory:

    ```bash
    cd backend
    ```

3. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

4. Set up the PostgreSQL database and configure the database settings in `backend/settings.py`.

5. Apply migrations:

    ```bash
    poetry run python manage.py migrate
    ```

6. Run the development server:

    ```bash
    poetry run python manage.py runserver
    ```

### Frontend Setup

1. Navigate to the frontend directory:

    ```bash
    cd frontend
    ```

2. Install dependencies:

    ```bash
    npm install
    ```

3. Run the development server:

    ```bash
    npm run serve
    ```

## Features

### Product Inventory

- Add, edit, and delete products.
- View product details including name, price, quantity, etc.

### Transaction

- View list of transactions.
- Each transaction includes details such as transaction ID, date, products purchased, total amount, etc.
- Filter transactions by date, user, or status.
- View detailed information for each transaction including individual product quantities and prices.
- Search transactions by transaction ID or customer name.

### User Management

- Admin panel for managing users.
- Add, edit, and delete users.
- Define user roles and permissions.

### Cashier

- Cashier interface for processing transactions.
- Authentication and authorization for cashiers.
- View transaction history.
