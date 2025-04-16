from sqlalchemy.orm import Session
from . import models, schemas
from . import auth
# USERS
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.hash_password(user.password)
    db_user = models.User(name=user.name, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

def update_user(db: Session, user_id: int, user_update: schemas.UserCreate):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.name = user_update.name
        user.email = user_update.email
        user.password = user_update.password
        db.commit()
        db.refresh(user)
    return user

# ITEMS
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session):
    return db.query(models.Item).all()

def delete_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item

def update_item(db: Session, item_id: int, item_update: schemas.ItemCreate):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        item.title = item_update.title
        item.description = item_update.description
        db.commit()
        db.refresh(item)
    return item