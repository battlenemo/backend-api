from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 模擬資料庫
items = []

# 資料模型
class Item(BaseModel):
    id: int
    name: str
    price: float

# GET /items → 查全部
@app.get("/items", response_model=List[Item])
def get_items():
    return items

# POST /items → 新增
@app.post("/items", response_model=Item)
def create_item(item: Item):
    for i in items:
        if i.id == item.id:
            raise HTTPException(status_code=400, detail="Item ID already exists")
    items.append(item)
    return item

# PUT /items/{id} → 更新
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for index, i in enumerate(items):
        if i.id == item_id:
            items[index] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE /items/{id} → 刪除
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, i in enumerate(items):
        if i.id == item_id:
            del items[index]
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
