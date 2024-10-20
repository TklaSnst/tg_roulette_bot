from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int]
    name: Mapped[str] = mapped_column(default=None)
    balance: Mapped[float] = mapped_column(default=0)
