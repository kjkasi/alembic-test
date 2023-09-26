from sqlalchemy import Boolean, Column, ForeignKey, Integer, MetaData, String
from sqlalchemy.orm import relationship, DeclarativeBase

metadata_obj = MetaData()

class Base(DeclarativeBase):
    metadata = metadata_obj
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    test_alembic = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True)