from typing import TypeVar, Generic
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.ext.declarative import DeclarativeMeta

ModelType = TypeVar("ModelType", bound=DeclarativeMeta)

class BaseDAO(Generic[ModelType]):
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: ModelType) -> ModelType:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_by_id(self, obj_id: int) -> ModelType:
        obj = self.db.query(self.model).filter(self.model.id == obj_id).first()
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{self.model.__name__} not found")
        return obj

    def get_all(self) -> list[ModelType]:
        return self.db.query(self.model).all()

    # def update(self, obj: ModelType) -> ModelType:
    #     self.db.add(obj)
    #     self.db.commit()
    #     self.db.refresh(obj)
    #     return obj


    def update(self, model: ModelType, **kwargs) -> ModelType:
        for key, value in kwargs.items():
            setattr(model, key, value)

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model

    def delete(self, obj_id: int) -> ModelType:
        obj = self.get_by_id(obj_id)
        self.db.delete(obj)
        self.db.commit()
        return obj
