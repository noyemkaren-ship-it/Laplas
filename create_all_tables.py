from base import Base, engine
import models
from crud_repositories import UserCrudRepository
from crud_repositories import PrivateTutorRepository
from base import Session
from sqlalchemy import select

from schemas import PrivateTutorSchema

Base.metadata.create_all(engine)
UserCrudRepository.create_admin(2012, password="Kirov288A")
PrivateTutorRepository.create(pt=PrivateTutorSchema(
    name="Анна Матвесян",
    subject="english",
    description="Я учитель по английскому, могу помочь вам в любой проблеме, имею высшее образования и не маленький стаж",
    initials="Номер телефона +374 93 814054 есть в Whatsap и Telegram"

))
FIRST_LESSON_HTML = """
<h2>Introduction to English</h2>

<p>
    English is one of the most widely spoken languages in the world.
    It is the official language of more than 50 countries and is used
    as a global lingua franca in business, science, and technology.
</p>

<h3>Why learn English?</h3>

<ul>
    <li><strong>Global reach</strong> — over 1.5 billion people speak English.</li>
    <li><strong>Career opportunities</strong> — most international companies require it.</li>
    <li><strong>Access to knowledge</strong> — the majority of online content is in English.</li>
    <li><strong>Travel</strong> — English is the default language of tourism.</li>
</ul>

<h3>The English alphabet</h3>

<p>
    English uses the Latin alphabet with <strong>26 letters</strong>:
    <code>A B C D E F G H I J K L M N O P Q R S T U V W X Y Z</code>.
</p>

<h3>Basic grammar idea: Subject + Verb + Object</h3>

<p>
    Most English sentences follow the <em>SVO</em> pattern:
</p>

<pre><code>She   reads   books.
I     love    programming.
They  play    football.</code></pre>

<h3>Everyday phrases</h3>

<ul>
    <li><strong>Hello</strong> — a universal greeting.</li>
    <li><strong>Thank you</strong> — expresses gratitude.</li>
    <li><strong>Good morning</strong> — greeting before noon.</li>
    <li><strong>How are you?</strong> — asks about someone's well-being.</li>
</ul>

<blockquote>
    "The limits of my language mean the limits of my world."
    — Ludwig Wittgenstein
</blockquote>

<p>
    In the next lesson we will cover the verb <strong>to be</strong>
    and the present simple tense.
</p>
"""


def seed_first_lesson():
    with Session() as session:
        existing = session.execute(
            select(models.Lesson).where(
                models.Lesson.subject == "English",
                models.Lesson.num == 1,
            )
        ).scalars().first()

        if existing:
            print(f"⏩ Lesson already exists (id={existing.id}, num={existing.num})")
            return existing

        lesson = models.Lesson(
            name="Introduction to English",
            subject="English",
            num=1,
            lesson_html=FIRST_LESSON_HTML,
            lesson_type="text",
        )
        session.add(lesson)
        session.commit()
        session.refresh(lesson)
        print(f"✅ Lesson created: id={lesson.id}, num={lesson.num}, name={lesson.name!r}")
        return lesson


def seed_first_test():
    with Session() as session:
        question = "What is the first letter of the English alphabet?"
        existing = session.execute(
            select(models.Test).where(
                models.Test.subject == "English",
                models.Test.question == question,
            )
        ).scalars().first()

        if existing:
            print(f"⏩ Test already exists (id={existing.id})")
            return existing

        test = models.Test(
            subject="English",
            question=question,
            answer="A",
        )
        session.add(test)
        session.commit()
        session.refresh(test)
        print(f"✅ Test created: id={test.id}, subject={test.subject!r}")
        return test


seed_first_lesson()
seed_first_test()

print("\n🚀 Database is ready. Start the server: python3 main.py")