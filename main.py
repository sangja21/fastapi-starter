## 프로그램 진입점, 애플리케이션을 초기화하고 메인 윈도우를 실행한다.

# main.py

from fastapi import FastAPI
from routers import user  # 라우터 파일들을 import
from config.database import engine
from model import user_model

# 데이터베이스 테이블 생성하기
user_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 라우터 등록
app.include_router(user.router)


# 앱 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
