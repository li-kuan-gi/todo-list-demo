# Todo List 應用程式

一個使用 Flask (後端)、React (前端)、MongoDB (資料庫) 構建的全端待辦事項應用程式，並使用 Docker 進行容器化部署api。

## 功能特點

- 創建、讀取、更新和刪除待辦事項
- 資料持久化儲存
- 容器化部署。

## 技術架構

### 後端
- flask: Python Web 框架
- flask_pymongo: MongoDB Python 驅動
- flask_cors: 處理跨域請求

### 前端
- React.js
- Axios: HTTP 客戶端
- Tailwind

### 資料庫
- MongoDB

### 部署
- Docker
- Docker Compose

## 系統要求

- Docker
- Docker Compose
- Node.js (開發環境)
- Python 3.x (開發環境)

## 安裝步驟

1. 複製專案
```bash
git clone https://github.com/li-kuan-gi/todo-list-demo
cd todo-list-demo
```

2. 使用 Docker Compose 啟動api
```bash
docker-compose up --build
```

3. 啟動前端
```bash
cd frontend
npm start
```

應用程式將在以下地址運行：
- 前端: http://localhost:3000
- 後端 API: http://localhost:5000
- MongoDB: localhost:27017

## API 端點

### Todo 操作
- `GET /api/todos`: 獲取所有待辦事項
- `POST /api/todos`: 創建新待辦事項
- `PUT /api/todos/<id>`: 更新待辦事項
- `DELETE /api/todos/<id>`: 刪除待辦事項
