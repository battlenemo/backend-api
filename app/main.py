from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal, engine, Base
from app.models.item import Item as ItemModel
from app.schemas.item import Item, ItemCreate
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 依賴：取得資料庫 session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET /items
@app.get("/items", response_model=List[Item])
def read_items(db: Session = Depends(get_db)):
    return db.query(ItemModel).all()

# POST /items
@app.post("/items", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = ItemModel(name=item.name, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# PUT /items/{id}
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    return db_item

# DELETE /items/{id}
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"detail": "Item deleted"}
