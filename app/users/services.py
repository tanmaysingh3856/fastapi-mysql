from sqlalchemy.orm import Session

from app.users import schemas, models


def create_user(user: schemas.UserCreate, db: Session):
    """This function creates a new user entry in the database

    Args:
        user (schemas.UserCreate): The user schema obj
        db (Session): The DB session

    Returns:
        models.User: The created user obj
    """
    obj = models.User(**user.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
