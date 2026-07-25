from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Text,
    ForeignKey
)

from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


# ==========================
# FUENTES
# ==========================

class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(200), nullable=False)

    url = Column(String(500), unique=True)

    country = Column(String(100))

    language = Column(String(50))

    category = Column(String(100))

    rss = Column(String(500))

    sitemap = Column(String(500))

    active = Column(Boolean, default=True)

    compatibility = Column(Integer, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)

    articles = relationship("Article", back_populates="source")


# ==========================
# ARTÍCULOS
# ==========================

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)

    source_id = Column(Integer, ForeignKey("sources.id"))

    title = Column(Text)

    subtitle = Column(Text)

    author = Column(String(300))

    url = Column(String(700), unique=True)

    published_date = Column(DateTime)

    captured_date = Column(DateTime, default=datetime.utcnow)

    category = Column(String(150))

    image = Column(Text)

    full_text = Column(Text)

    source = relationship("Source", back_populates="articles")