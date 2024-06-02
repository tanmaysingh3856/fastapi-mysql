from sqlalchemy import text
from sqlalchemy.orm import Session

from app.users import models


def get_users(db: Session):
    """This function returns a list of users from the database

    Args:
        db (Session): The DB session

    Returns:
        list[models.User]: The user obj list
    """

    return db.query(models.User).all()
