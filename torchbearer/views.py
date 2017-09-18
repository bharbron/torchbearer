from flask import render_template, request, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from torchbearer import app
from .database import db
from .formprocessor import process_gm_add_trait
from .forms import GMAddFirstNameForm, GMAddLastNameForm, GMAddSkillForm, GMAddTraitForm, GMAddWiseForm, GMEditSkillForm, GMEditTraitForm, GMEditWiseForm
from .helpers import flash_results, flash_form_errors
from .models import User, Trait, Wise, Skill


@app.route("/", methods=["GET"])
def get_home():
    """
    Main page of the site
    """
    return render_template("home.html")


@app.route("/gm", methods=["GET"])
def get_gm():
    """
    Top level gm page
    """
    return render_template("gm.html")


@app.route("/gm/traits_wises_skills", methods=["GET"])
def get_gm_traits_wises_skills():
    """
    GM page for managing Traits, Wises, and Skills
    """
    try:
        traits = db.session.query(Trait).filter_by(active=True).order_by(Trait.name.asc()).all()
        wises = db.session.query(Wise).filter_by(active=True).order_by(Wise.name.asc()).all()
        skills = db.session.query(Skill).filter_by(active=True).order_by(Skill.name.asc()).all()

        forms = {}
        forms["add_trait"] = GMAddTraitForm(request.form, prefix="add_trait")
        forms["add_wise"] = GMAddWiseForm(request.form, prefix="add_wise")
        forms["add_skill"] = GMAddSkillForm(request.form, prefix="add_wise")

        for trait in traits:
            forms["edit_trait_{}".format(trait.id)] = GMEditTraitForm(request.form, trait, prefix="edit_trait_{}".format(trait.id))

        for wise in wises:
            forms["edit_wise_{}".format(wise.id)] = GMEditWiseForm(request.form, wise, prefix="edit_wise_{}".format(wise.id))

        for skill in skills:
            forms["edit_skill_{}".format(skill.id)] = GMEditSkillForm(request.form, skill, prefix="edit_skill_{}".format(skill.id))

        return render_template("gm_traits_wises_skills.html", forms=forms, traits=traits, wises=wises, skills=skills)

    finally:
        db.session.commit()

@app.route("/gm/trait", methods=["POST"])
def post_gm_trait():
    form = GMAddTraitForm(request.form, prefix="add_trait")

    if form.validate_on_submit():
        results = process_gm_add_trait(form=form)
        flash_results(results)
        return redirect(url_for("get_gm_traits_wises_skills"))

    flash_form_errors(form)
    return redirect(url_for("get_gm_traits_wises_skills"))
