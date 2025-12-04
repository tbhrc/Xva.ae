from backend import crud, schemas
from backend.database import SessionLocal, Base, engine
from backend.models import Expert


def seed_initial_experts():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    seed_data = [
        schemas.ExpertCreate(
            name="Jan de Wachter",
            title="Organizational Transformation & HR Strategy",
            summary=(
                "Seasoned HR expert with over 22 years of experience in organizational development and HR "
                "transformation across the Middle East. Specializes in aligning workforce strategy with technological adoption."
            ),
            linked_in_url="https://www.linkedin.com/in/jan-d-8840038/",
            location="Dubai, UAE",
            expertise="HR Transformation",
            tools="People analytics, change management",
            vetted_status="approved",
        ),
        schemas.ExpertCreate(
            name="Ignatius (Natie) Rautenbach",
            title="AI Strategy & Ethics",
            summary=(
                "Lead AI Strategist with 15+ years of experience. Expert in ethical AI, responsible AI implementation, "
                "and transforming complex data into actionable business insights."
            ),
            linked_in_url="https://www.linkedin.com/in/natierau/",
            location="Dubai, UAE",
            expertise="AI Strategy",
            tools="AI governance, data ethics",
            vetted_status="approved",
        ),
        schemas.ExpertCreate(
            name="Christopher Booth",
            title="Generative AI & Product Ownership",
            summary=(
                "Specialist in Generative AI and conversational agents. Brings deep expertise in product ownership for "
                "large-scale AI deployments, including banking sector chatbots."
            ),
            linked_in_url="https://www.linkedin.com/in/christopher--booth/",
            location="Dubai, UAE",
            expertise="Generative AI",
            tools="LLMs, conversational AI",
            vetted_status="approved",
        ),
    ]

    existing = {expert.name for expert in session.query(Expert).all()}
    for expert in seed_data:
        if expert.name in existing:
            continue
        crud.create_expert(session, expert)

    session.close()


if __name__ == "__main__":
    seed_initial_experts()
    print("Seed data inserted.")
