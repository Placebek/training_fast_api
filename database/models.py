from sqlalchemy import Column, Integer, String, ForeignKey, Table, Text
from sqlalchemy.orm import relationship
from database.main import Base

roles_users = Table(
    "roles_users", 
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("role_id", Integer, ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True),
)

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=True)
    email = Column(String, unique=True, nullable=True)

    roles = relationship("Roles", secondary=roles_users, back_populates="users")

    trainer = relationship("Trainer", back_populates="user", uselist=False)


class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    role_title = Column(String, nullable=False)

    users = relationship("Users", secondary=roles_users, back_populates="roles")


class Trainer(Base):
    __tablename__ = "trainer"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    sur_name = Column(String, nullable=False)
    father_name = Column(String, nullable=False)
    avatar = Column(String, nullable=False)  
    achievements = Column(Text, nullable=True)  

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    user = relationship("Users", back_populates="trainer")
