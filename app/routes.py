from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.database import async_session
from app.models import Note
from app.schemas import NoteCreate, NoteOut

router = APIRouter()

async def get_session():
    async with async_session() as session:
        yield session


@router.post("/notes/", response_model=NoteOut)
async def create_note(note: NoteCreate, session: AsyncSession = Depends(get_session)):
    new_note = Note(text=note.text)
    session.add(new_note)
    await session.commit()
    await session.refresh(new_note)
    return new_note

@router.get("/notes/", response_model=list[NoteOut])
async def get_notes(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Note))
    return result.scalars().all()