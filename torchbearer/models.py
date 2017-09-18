from flask.ext.login import UserMixin

from .database import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), info={"label": "Name"})
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)


class Stock(db.Model):
    __tablename__ = "stock"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, info={"label": "Name"})
    description = db.Column(db.Text)
    nature_descriptor_1 = db.Column(db.String(32), nullable=False)
    nature_descriptor_2 = db.Column(db.String(32), nullable=False)
    nature_descriptor_3 = db.Column(db.String(32), nullable=False)
    active = db.Column(db.Boolean, default=True)

    # Relationships
    classes = db.relationship("Class", backref="stock")
    nature_questions = db.relationship("NatureQuestion", backref="stock")
    bonus_skills = db.relationship("Skill", secondary="stock_bonus_skills", backref="stocks")
    bonus_wises = db.relationship("Wise", secondary="stock_bonus_wises", backref="stocks")
    homelands = db.relationship("Homeland", secondary="stock_homelands", backref="stocks")


class StockBonusSkills(db.Model):
    __tablename__ = "stock_bonus_skills"

    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey("stock.id"))
    skill_id = db.Column(db.Integer, db.ForeignKey("skill.id"))


class StockBonusWises(db.Model):
    __tablename__ = "stock_bonus_wises"

    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey("stock.id"))
    wise_id = db.Column(db.Integer, db.ForeignKey("wise.id"))


class StockHomelands(db.Model):
    __tablename__ = "stock_homelands"

    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey("stock.id"))
    homeland_id = db.Column(db.Integer, db.ForeignKey("homeland.id"))


class Class(db.Model):
    __tablename__ = "class"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, info={"label": "Name"})
    description = db.Column(db.Text)
    max_health = db.Column(db.Integer, default=4)
    min_health = db.Column(db.Integer, default=4)
    max_will = db.Column(db.Integer, default=4)
    min_will = db.Column(db.Integer, default=4)
    active = db.Column(db.Boolean, default=True)

    # Relationships
    skills = db.relationship("Skill", secondary="class_skills", backref="classes")


class ClassSkills(db.Model):
    __tablename__ = "class_skills"

    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey("class.id"))
    skill_id = db.Column(db.Integer, db.ForeignKey("skill.id"))
    rating = db.Column(db.Integer)


class Homeland(db.Model):
    __tablename__ = "homeland"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, info={"label": "Name"})
    description = db.Column(db.Text)
    active = db.Column(db.Boolean, default=True)

    # Relationships
    hometowns = db.relationship("Hometown", secondary="homeland_hometowns", backref="homelands")
    skills = db.relationship("Skill", secondary="homeland_skills", backref="homelands")
    traits = db.relationship("Trait", secondary="homeland_traits", backref="homelands")


class HomelandHometowns(db.Model):
    __tablename__ = "homeland_hometowns"

    id = db.Column(db.Integer, primary_key=True)
    homeland_id = db.Column(db.Integer, db.ForeignKey("homeland.id"))
    hometown_id = db.Column(db.Integer, db.ForeignKey("hometown.id"))


class HomelandSkills(db.Model):
    __tablename__ = "homeland_skills"

    id = db.Column(db.Integer, primary_key=True)
    homeland_id = db.Column(db.Integer, db.ForeignKey("homeland.id"))
    skill_id = db.Column(db.Integer, db.ForeignKey("skill.id"))


class HomelandTraits(db.Model):
    __tablename__ = "homeland_traits"

    id = db.Column(db.Integer, primary_key=True)
    homeland_id = db.Column(db.Integer, db.ForeignKey("homeland.id"))
    trait_id = db.Column(db.Integer, db.ForeignKey("trait.id"))


class Hometown(db.Model):
    __tablename__ = "hometown"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, info={"label": "Name"})
    description = db.Column(db.Text)
    active = db.Column(db.Boolean, default=True)

    # Relationships
    sklls = db.relationship("Skill", secondary="hometown_skills", backref="hometowns")
    traits = db.relationship("Trait", secondary="hometown_traits", backref="hometowns")


class HometownSkills(db.Model):
    __tablename__ = "hometown_skills"

    id = db.Column(db.Integer, primary_key=True)
    hometown_id = db.Column(db.Integer, db.ForeignKey("hometown.id"))
    skill_id = db.Column(db.Integer, db.ForeignKey("skill.id"))


class HometownTraits(db.Model):
    __tablename__ = "hometown_traits"

    id = db.Column(db.Integer, primary_key=True)
    hometown_id = db.Column(db.Integer, db.ForeignKey("hometown.id"))
    trait_id = db.Column(db.Integer, db.ForeignKey("trait.id"))


class Skill(db.Model):
    __tablename__ = "skill"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, info={"label": "Name"})
    description = db.Column(db.Text)
    social_grace = db.Column(db.Boolean, default=False)
    speciality = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)


class Trait(db.Model):
    __tablename__ = "trait"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, info={"label": "Name"})
    description = db.Column(db.Text)
    active = db.Column(db.Boolean, default=True)


class Wise(db.Model):
    __tablename__ = "wise"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, info={"label": "Name"})
    active = db.Column(db.Boolean, default=True)


class NatureQuestion(db.Model):
    __tablename__ = "nature_question"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    active = db.Column(db.Boolean, default=True)

    # Relationships
    answers = db.relationship("NatureAnswer", backref="question")


class NatureAnswer(db.Model):
    __tablename__ = "nature_answer"

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text, nullable=False)
    increase_nature = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)

    # Relationships
    replacement_traits = db.relationship("Trait", secondary="nature_answer_replacement_traits", backref="nature_answers")
    decrease_skill = db.relationship("Skill", backref="nature_answers")


class FirstName(db.Model):
    __tablename__ = "first_name"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, info={"label": "First Name"})
    active = db.Column(db.Boolean, default=True)


class LastName(db.Model):
    __tablename__ = "last_name"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, info={"label": "Last Name"})
    active = db.Column(db.Boolean, default=True)
