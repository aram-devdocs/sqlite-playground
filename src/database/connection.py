import os
from typing import Optional, Generator
from sqlalchemy import create_engine, Engine, text
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Base(DeclarativeBase):
    """Base class for SQLAlchemy ORM models"""

    pass


class DatabaseManager:
    """
    Manages database connections and provides utility methods for database operations

    Attributes:
        _instance (Optional[DatabaseManager]): Singleton instance
        engine (Engine): SQLAlchemy database engine
        SessionLocal (Session): SQLAlchemy session factory
    """

    _instance = None

    def __new__(cls, db_name: str = "analysis.db"):
        print("Creating new DatabaseManager instance")

        # check the db_name to ensure it is only a name + .db
        if not db_name.endswith(".db"):
            raise ValueError("db_name must end with .db")

        """Singleton pattern implementation"""
        if not cls._instance:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance._initialize(db_name)
        return cls._instance

    def _initialize(self, db_name: str):
        """Initialize database connection"""
        # Default to a database in the src/data directory
        db_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", db_name
        )

        # Ensure data directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        # Create SQLite engine
        self.engine = create_engine(f"sqlite:///{db_path}", echo=False)

        # Create session factory
        self.SessionLocal = sessionmaker(bind=self.engine)

    def execute_query(self, query: str, params: Optional[dict] = None):
        """
        Execute a raw SQL query

        Args:
            query (str): The SQL query to execute
            params (Optional[dict]): Parameters for the SQL query

        Returns:
            ResultProxy: The result of the executed query
        """
        with self.SessionLocal() as session:
            result = session.execute(text(query), params or {})
            session.commit()
            return result

    def get_session(self) -> Session:
        """
        Create and return a new database session

        Returns:
            Session: A new database session
        """
        return self.SessionLocal()

    def create_tables(self):
        """Create all defined tables in the database"""
        Base.metadata.create_all(self.engine)

    def drop_tables(self):
        """Drop all defined tables in the database"""
        Base.metadata.drop_all(self.engine)


def get_db() -> Generator[Session, None, None]:
    """
    Dependency function to get a database session

    Yields:
        Session: A database session that will be closed after use
    """
    db = DatabaseManager().get_session()
    try:
        yield db
    finally:
        db.close()


# Example of how to define a model
# class ExampleModel(Base):
#     __tablename__ = 'example_table'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     # Add more columns as needed


def main():
    """
    Quick script to initialize the database
    Can be used to create tables or perform initial setup
    """
    db_manager = DatabaseManager()
    db_manager.create_tables()
    print("Database initialized successfully!")


if __name__ == "__main__":
    main()
