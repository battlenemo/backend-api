# Backend CRUD API (FastAPI)

這是一個使用 **FastAPI + SQLAlchemy + SQLite** 建立的後端 RESTful API 專案，提供基本的 CRUD（Create / Read / Update / Delete）功能，作為後端開發練習與作品集展示。

---

## 技術棧

- Python 3
- FastAPI
- SQLAlchemy ORM
- SQLite
- Uvicorn
- Swagger UI

---

## 功能說明

- 新增 Item 資料
- 查詢所有 Item
- 更新 Item
- 刪除 Item
- 使用 SQLite 進行資料持久化
- 自動產生 API 文件（Swagger UI）

---

## 專案結構

```text
backend-api/
├─ app/
│  ├─ main.py
│  ├─ models/
│  ├─ schemas/
│  └─ db/
├─ requirements.txt
└─ README.md
```

## 啟動方式

### 建立虛擬環境
```bash
python -m venv venv
```

### 啟動虛擬環境
Windows：
```bash
venv\Scripts\activate
```

### 安裝套件
```bash
pip install -r requirements.txt
```

### 啟動伺服器
```bash
uvicorn app.main:app --reload
```

### 開啟瀏覽器
Swagger API 文件：
http://127.0.0.1:8000/docs
