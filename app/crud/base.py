from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
            self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def get_multi_filter(
            self, db: Session, *, filters=None, skip: int = 0, limit: int = 100
    ) -> list[Type[ModelType]]:
        query = db.query(self.model)
        if filters:
            for condition in filters:
                query = query.filter(condition)
        return query.offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj_in.__dict__)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # Todo: optimize it
    def create_multi(self, db: Session, *, objs_in: List[CreateSchemaType]) -> List[ModelType]:
        objs_in_data = [jsonable_encoder(obj) for obj in objs_in]
        db_objs = [self.model(**data) for data in objs_in_data]
        db.bulk_save_objects(db_objs)
        db.commit()
        return db_objs

    # Todo: optimize it
    def update(
            self,
            db: Session,
            *,
            db_obj: ModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update_by_id(
            self,
            db: Session,
            *,
            id: Any,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        if not isinstance(obj_in, dict):
            obj_in = obj_in.dict(exclude_unset=True)
        result = db.query(self.model).filter(self.model.id == id).update(obj_in)
        db.commit()
        return result

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
