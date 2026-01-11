# app/db/init_db.py
from app.db.database import Base, engine
from app.models.item import Item

def init_db():
    Base.metadata.create_all(bind=engine)
    print("資料表建立完成!")

if __name__ == "__main__":
    init_db()
