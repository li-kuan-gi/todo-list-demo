FROM python:3.9-slim

WORKDIR /app

# 複製依賴文件
COPY requirements.txt .

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 複製源碼
COPY app.py .
COPY repositories .
COPY wait-for-it.sh .

# 暴露端口
EXPOSE 5000

# 設置環境變量
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# 啟動應用
CMD ["flask", "run", "--host=0.0.0.0"]