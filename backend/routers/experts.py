import os
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Header, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/experts", tags=["experts"])


ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "admin-secret")


def get_admin_token(x_admin_token: Optional[str] = Header(default=None)):
    if x_admin_token != ADMIN_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )


@router.get("/", response_model=List[schemas.ExpertOut])
def list_experts(
    q: Optional[str] = None,
    expertise: Optional[str] = None,
    location: Optional[str] = None,
    vetted_status: str = "approved",
    limit: int = 100,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    experts = crud.list_experts(
        db,
        q=q,
        expertise=expertise,
        location=location,
        vetted_status=vetted_status or "approved",
        limit=limit,
        offset=offset,
    )
    return experts


@router.get("/{expert_id}", response_model=schemas.ExpertOut)
def get_expert(expert_id: int, db: Session = Depends(get_db)):
    expert = crud.get_expert_by_id(db, expert_id)
    if not expert:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expert not found")
    return expert


@router.post("/", response_model=schemas.ExpertOut, status_code=status.HTTP_201_CREATED)
def create_expert(
    payload: schemas.ExpertCreate,
    db: Session = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    return crud.create_expert(db, payload)


@router.patch("/{expert_id}", response_model=schemas.ExpertOut)
def update_expert(
    expert_id: int,
    payload: schemas.ExpertUpdate,
    db: Session = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    expert = crud.update_expert(db, expert_id, payload)
    if not expert:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expert not found")
    return expert
