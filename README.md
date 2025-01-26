# SQLite Data Analysis Project

## Project Structure

- `src/notebooks/`: Jupyter notebooks for data analysis
- `src/database/`: Reusable database connection and ORM methods
- `src/data/`: SQLite database files
- `scripts/`: Utility scripts for project setup and management

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository
2. Run scripts/setup.sh to install dependencies and create the database
   2.1. To allow the script to run, you need to give it permission to run by running `chmod +x scripts/setup.sh`
   2.2. To run the script, you need to run `./scripts/setup.sh`

## Database Management

Refer to `src/database/connection.py` for database connection and ORM setup.

### Seeding the Database

The `src/notebooks/seed.ipynb` notebook fetches data from the REST Countries API and seeds a local SQLite database.
To seed the database:

1. Open the notebook in Jupyter
2. Run all cells to fetch and store country data locally

## Environment Variables

Create a `.env` file in the project root for sensitive configurations.
