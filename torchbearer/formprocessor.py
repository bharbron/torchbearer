from torchbearer import app
from .database import db
from .models import Trait, Wise, Skill

def process_gm_add_trait(form):
    results = {"successes": [], "errors": [], "warnings": [], "infos": []}
    try:
        trait = Trait(name=form.name.data, description=form.description.data)
        db.session.add(trait)
    finally:
        db.session.commit()
    return results