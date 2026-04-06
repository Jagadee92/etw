from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models,schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_record(record:schemas.RecordCreate,db:Session=Depends(get_db)):

    new_record = models.FinancialRecord(
        user_id=1,
        amount=record.amount,
        type=record.type,
        category=record.category,
        record_date=record.record_date,
        notes=record.notes
    )

    db.add(new_record)
    db.commit()

    return {"message":"Record created"}


@router.get("/")
def get_records(db:Session=Depends(get_db)):

    data = db.query(models.FinancialRecord).all()

    return data