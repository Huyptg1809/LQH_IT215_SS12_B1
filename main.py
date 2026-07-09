from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base
from discount_services import delete_discount_service

Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.delete('/discounts/{discount_id}')
def delete_discount(discount_id: int, db: Session = Depends(get_db)):
    result = delete_discount_service(discount_id, db)
    return result
