# FastAPI Demo - Product Management System

A full-stack web application for managing products, built with FastAPI (backend) and React (frontend).

## Features

- 📦 Product CRUD operations
- 🔄 RESTful API with FastAPI
- ⚛️ React frontend
- 🗄️ Database integration with SQLAlchemy
- 🔌 CORS-enabled for local development

## Project Structure

```
fastapi_demo/
├── backend/           # FastAPI backend
│   ├── main.py       # Main application entry point
│   ├── models.py     # SQLAlchemy models
│   ├── schemas.py    # Pydantic schemas
│   ├── database.py   # Database configuration
│   ├── Pipfile       # Python dependencies (Pipenv)
│   └── requirements.txt  # Python dependencies (pip)
├── frontend/         # React frontend
│   ├── src/
│   │   ├── App.js
│   │   └── ...
│   └── package.json
└── README.md
```

## Prerequisites

- Python 3.13+
- Node.js 14+
- npm or yarn
- PostgreSQL or MySQL (optional, can use SQLite for development)

## Backend Setup

### Using pip

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Using Pipenv

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pipenv install
```

3. Activate the Pipenv shell:
```bash
pipenv shell
```

4. Run the FastAPI server:
```bash
uvicorn main:app --reload
```

## Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## API Endpoints

The FastAPI backend provides the following endpoints:

- `GET /products` - Get all products
- `GET /products/{id}` - Get a specific product
- `POST /products` - Create a new product
- `PUT /products/{id}` - Update a product
- `DELETE /products/{id}` - Delete a product

Visit `http://localhost:8000/docs` for interactive API documentation (Swagger UI).

## Database Configuration

The application uses SQLAlchemy ORM and supports multiple database backends:

- SQLite (default for development)
- PostgreSQL
- MySQL

Configure your database connection in `backend/database.py`.

## Development

### Backend

The backend is built with:
- FastAPI - Modern web framework for building APIs
- SQLAlchemy - SQL toolkit and ORM
- Pydantic - Data validation using Python type annotations
- Uvicorn - ASGI server

### Frontend

The frontend is built with:
- React - JavaScript library for building user interfaces
- Axios - Promise-based HTTP client

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License.
