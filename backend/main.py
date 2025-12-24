from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import Product
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create the database tables
models.Base.metadata.create_all(bind=engine)


products = [
    Product(
        id=1,
        name="Laptop",
        description="A high performance laptop",
        price=1200.50,
        quantity=10,
    ),
    Product(
        id=2,
        name="Smartphone",
        description="A latest model smartphone",
        price=800.00,
        quantity=25,
    ),
    Product(
        id=3,
        name="Headphones",
        description="Noise cancelling headphones",
        price=150.75,
        quantity=50,
    ),
    Product(
        id=4, name="Monitor", description="4K UHD Monitor", price=400.00, quantity=15
    ),
    Product(
        id=5,
        name="Keyboard",
        description="Mechanical keyboard",
        price=100.00,
        quantity=30,
    ),
]


# Get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# init DB
def init_db():
    db = SessionLocal()
    # Check if products already exist
    count = db.query(models.Product).count()
    if count > 0:
        db.close()
        return
    # Add sample products to the database
    for product in products:
        db.add(models.Product(**product.model_dump()))
    db.commit()
    db.close()


# Init DB with sample data
init_db()


# Root endpoint
@app.get("/")
def index():
    return {"message": "Hello World"}


# Endpoint to get all products
@app.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    # Get all products from the database
    db_products = db.query(models.Product).all()
    return db_products


# Endpoint to get a product by ID
@app.get("/products/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    # Get product by ID from the database
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    if db_product:
        return db_product
    return {"error": "Product not found"}


# Endpoint to add a new product
@app.post("/products/")
def add_product(new_db_product: Product, db: Session = Depends(get_db)):
    # Add a new product to the database
    db.add(models.Product(**new_db_product.model_dump()))
    db.commit()
    return {"message": "Product added successfully"}


# Endpoint to update a product by ID
@app.put("/products/{id}")
def update_product(id: int, updated_product: Product, db: Session = Depends(get_db)):
    # Update a product in the database
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    if db_product:
        for key, value in updated_product.model_dump().items():
            setattr(db_product, key, value)
        db.commit()
        return {"message": "Product updated successfully"}
    return {"error": "Product not found"}


# Endpoint to delete a product by ID
@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    # Delete a product from the database
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted successfully"}
    return {"error": "Product not found"}
