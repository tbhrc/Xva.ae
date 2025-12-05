from typing import List, Optional

from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from . import models, schemas


SEARCHABLE_COLUMNS = [
    models.Expert.name,
    models.Expert.title,
    models.Expert.summary,
    models.Expert.expertise,
    models.Expert.location,
    models.Expert.tools,
]


def get_expert_by_id(db: Session, expert_id: int) -> Optional[models.Expert]:
    return db.query(models.Expert).filter(models.Expert.id == expert_id).first()


def list_experts(
    db: Session,
    q: Optional[str] = None,
    expertise: Optional[str] = None,
    location: Optional[str] = None,
    vetted_status: str = "approved",
    limit: int = 100,
    offset: int = 0,
) -> List[models.Expert]:
    query = db.query(models.Expert)

    if vetted_status:
        query = query.filter(models.Expert.vetted_status == vetted_status)

    if expertise:
        query = query.filter(func.lower(models.Expert.expertise) == expertise.lower())

    if location:
        query = query.filter(func.lower(models.Expert.location) == location.lower())

    if q:
        lowered = f"%{q.lower()}%"
        conditions = [func.lower(column).like(lowered) for column in SEARCHABLE_COLUMNS]
        query = query.filter(or_(*conditions))

    limit = min(max(limit, 1), 200)
    query = query.offset(offset).limit(limit)

    return query.all()


def create_expert(db: Session, expert: schemas.ExpertCreate) -> models.Expert:
    expert_data = expert.dict()
    if expert_data.get("linked_in_url"):
        expert_data["linked_in_url"] = str(expert_data["linked_in_url"])
        
    db_expert = models.Expert(**expert_data)
    db.add(db_expert)
    db.commit()
    db.refresh(db_expert)
    return db_expert


def update_expert(db: Session, expert_id: int, expert: schemas.ExpertUpdate) -> Optional[models.Expert]:
    db_expert = get_expert_by_id(db, expert_id)
    if not db_expert:
        return None

    update_data = expert.dict(exclude_unset=True)
    if update_data.get("linked_in_url"):
        update_data["linked_in_url"] = str(update_data["linked_in_url"])

    for key, value in update_data.items():
        setattr(db_expert, key, value)

    db.commit()
    db.refresh(db_expert)
    return db_expert
