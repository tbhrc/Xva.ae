from sqlalchemy import Column, DateTime, Index, Integer, String, Text, func

from .database import Base


class Expert(Base):
    __tablename__ = "experts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    title = Column(String, nullable=False, index=True)
    summary = Column(Text, nullable=True)
    linked_in_url = Column(String, nullable=False)
    location = Column(String, nullable=True, index=True)
    expertise = Column(String, nullable=True, index=True)
    tools = Column(Text, nullable=True)
    vetted_status = Column(String, nullable=False, default="approved", index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        Index("idx_expert_name", "name"),
        Index("idx_expert_title", "title"),
        Index("idx_expert_location", "location"),
        Index("idx_expert_expertise", "expertise"),
    )
