# fastapi-starter
A boilerplate for quickly starting a FastAPI project, including essential configurations and best practices for building high-performance APIs.

## 프로젝트 구조

FastAPI 기반의 프로젝트로, **MVC 패턴**을 따르며 각 기능을 명확하게 분리하여 관리합니다. 이 구조는 API 중심의 애플리케이션에 적합하며, 각 폴더의 역할은 다음과 같습니다.


### 각 폴더 설명

- **`config/`**:  
  프로젝트의 설정 파일과 데이터베이스 연결 설정을 담당합니다.
  - `database.py`: SQLAlchemy를 사용한 데이터베이스 연결 설정과 세션 관리 코드가 포함되어 있습니다.

- **`controller/`**:  
  비즈니스 로직을 처리하는 파일들이 포함된 폴더입니다. 사용자의 요청을 처리하고 서비스 로직을 호출하는 역할을 합니다.
  - `user_controller.py`: 사용자 관련 비즈니스 로직을 처리하는 코드가 포함되어 있습니다.

- **`model/`**:  
  데이터베이스 테이블과 매핑되는 SQLAlchemy 모델 파일이 위치하는 폴더입니다.
  - `user_model.py`: `User` 테이블과 매핑되는 SQLAlchemy 모델을 정의합니다.

- **`routers/`**:  
  API 라우팅을 정의하는 파일들이 위치하는 폴더입니다. 각 엔드포인트에 대한 경로와 해당 경로에서 처리할 함수를 매핑합니다.
  - `user.py`: 사용자 관련 API 라우팅을 정의합니다.

- **`schemas/`**:  
  요청 및 응답 데이터의 구조를 정의하는 **Pydantic 스키마** 파일이 위치하는 폴더입니다. 데이터의 유효성을 검사하고 구조화된 응답을 제공합니다.
  - `schemas.py`: 사용자 데이터의 요청 및 응답에 필요한 Pydantic 모델을 정의합니다.

- **`service/`**:  
  데이터베이스와의 상호작용 및 비즈니스 로직을 처리하는 서비스 파일들이 위치한 폴더입니다.
  - `user_service.py`: 사용자 관련 데이터베이스 작업 및 로직을 처리하는 코드가 포함되어 있습니다.

- **`util/`**:  
  유틸리티 함수들이 위치하는 폴더로, 반복적으로 사용되는 기능을 별도로 관리합니다.

---

## 추가 파일 설명

- **`.gitignore`**:  
  Git에서 추적하지 않을 파일이나 디렉토리를 지정한 파일입니다. (예: `__pycache__/`, 환경 설정 파일, 데이터베이스 파일 등)

- **`README.md`**:  
  프로젝트에 대한 설명과 사용 방법 등을 제공하는 파일입니다.

- **`requirements.txt`**:  
  프로젝트에 필요한 Python 패키지들이 명시된 파일입니다. `pip install -r requirements.txt` 명령어로 설치할 수 있습니다.

---

## venv 가상환경 설정 및 실행 방법

1. **가상환경 설정**:
    ```bash
    conda create --name myenv python=3.10
    conda activate myenv
    ```

2. **필수 패키지 설치**:
    ```bash
    pip install -r requirements.txt
    ```

3. **서버 실행**:
    ```bash
    uvicorn main:app --reload
    ```



## anaconda 가상환경 설정 및 실행 방법

1. **Anaconda 가상환경 설정**:
    먼저 Anaconda를 사용해 가상환경을 생성하고 활성화합니다.

    ```bash
    conda create --name myenv python=3.10
    conda activate myenv
    ```

2. **필수 패키지 설치**:
    프로젝트에 필요한 패키지를 설치합니다. `requirements.txt` 파일을 사용하여 한 번에 모든 패키지를 설치할 수 있습니다.

    ```bash
    pip install -r requirements.txt
    ```

3. **서버 실행**:
    FastAPI 서버를 시작하여 API를 테스트할 수 있습니다.

    ```bash
    uvicorn main:app --reload
    ```