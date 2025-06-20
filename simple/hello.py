from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

# グローバルロック
lock = asyncio.Lock()

@app.get("/hello")
async def hello():
    start = time.time()
    async with lock:  # ロックを取得
        await asyncio.sleep(2)  # 模擬的な処理
    end = time.time()
    return {"message": "Hello, world!", "time": end - start}
    
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
if __name__ == "__main__":
    main()
