from wtforms_alchemy import ModelForm

from torchbearer import app
from .models import FirstName, LastName, Skill, Trait, Wise


class FirstNameForm(ModelForm):

    class Meta:
        model = FirstName
        exclude = ["active"]


class GMAddFirstNameForm(FirstNameForm):
    # Buttons
    add = SubmitField("Add")


class LastNameForm(ModelForm):

    class Meta:
        model = LastName
        exclude = ["active"]


class GMAddLastNameForm(LastNameForm):
    # Buttons
    add = SubmitField("Add")


class SkillForm(ModelForm):

    class Meta:
        model = Skill
        exclude = ["active"]


class GMAddSkillForm(SkillForm):
    # Buttons
    add = SubmitField("Add")


class GMEditSkillForm(SkillForm):
    # Button
    save = SubmitField("Save")


class TraitForm(ModelForm):

    class Meta:
        model = Trait
        exclude = ["active"]


class GMAddTraitForm(TraitForm):
    # Buttons
    add = SubmitField("Add")


class GMEditTraitForm(TraitForm):
    # Buttons
    save = SubmitField("Save")


class WiseForm(ModelForm):

    class Meta:
        model = Wise
        exclude = ["active"]


class GMAddWiseForm(WiseForm):
    # Buttons
    add = SubmitField("Add")


class GMEditWiseForm(WiseForm):
    # Buttons
    save = SubmitField("Save")
