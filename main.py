from fastapi import FastAPI, HTTPException, Request
from database.database import get_db_connection
from routes.presencesTeacher import router as presencesTeacher_router
from routes.activitiesTeacher import router as activitiesTeacher_router
from routes.activitiesPresencesTeacher import router as activitiesPresencesTeacher_router
from routes.authToken import router as authToken_router

app = FastAPI()

# Middleware para verificar o token
@app.middleware("http")
async def verify_token(request: Request, call_next):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=403, detail="Token is missing")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM authToken WHERE token = %s", (token,))
    authToken = cursor.fetchone()
    cursor.close()
    connection.close()
    if(authToken):
      response = await call_next(request)
      return response
    else:
       HTTPException(status_code=403, detail="Token is missing")


# Inclui as rotas
app.include_router(presencesTeacher_router)
app.include_router(activitiesTeacher_router)
app.include_router(activitiesPresencesTeacher_router)
app.include_router(authToken_router)
