# FastApi-Test-task

# Live Demo
Base URL: https://fastapi-test-task-v0-0-1.onrender.com

Swagger Docs: https://fastapi-test-task-v0-0-1.onrender.com/docs

ReDoc: https://fastapi-test-task-v0-0-1.onrender.com/redoc

# Steps
1. Clone this repository
   git clone https://github.com/Zhadi-1-s/FastApi-Test-task.git
   
2. Set up a virtual environment
   python -m venv <virtual_environment_name>
   /venv/Scripts/activate

3. Install Dependencies
   pip install -r requirements.txt

4.Set Environment Variables Create a .env file in the project root with the following content
  
  SECRET_KEY=your_jwt_secret_key
  
  ALGORITHM=HS256
  
  ACCESS_TOKEN_EXPIRE_MINUTES=30
  
  DATABASE_URL=sqlite:///./test.db
  
  EXTERNAL_API_URL=https://api.coingecko.com/api/v3

5. Run Database Migrations
   python -c "from app.database import init_db; init_db()"

6. Start the application
   uvicorn app.main:app --reload

# Endpoints
GET /api/v1/test
curl -X GET http://127.0.0.1:8000/api/v1/test

GET /api/v1/public
curl -X GET http://127.0.0.1:8000/api/v1/public




   
