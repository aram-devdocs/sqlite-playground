# SQLite Data Analysis Project

## Project Structure
- `src/notebooks/`: Jupyter notebooks for data analysis
- `src/database/`: Reusable database connection and ORM methods
- `src/data/`: SQLite database files
- `src/tests/`: Unit tests for database and analysis functions
- `scripts/`: Utility scripts for project setup and management

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Notebooks
```bash
jupyter notebook
```

## Database Management
Refer to `src/database/connection.py` for database connection and ORM setup.

### Seeding the Database
The `src/notebooks/seed.ipynb` notebook fetches data from the REST Countries API and seeds a local SQLite database. 
To seed the database:
1. Open the notebook in Jupyter
2. Run all cells to fetch and store country data locally

## Environment Variables
Create a `.env` file in the project root for sensitive configurations. 