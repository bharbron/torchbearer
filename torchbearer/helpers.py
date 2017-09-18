from flask import flash


def flash_results(results):
    """Flash all the messages contained in the given results dictionary

    :param results: A dictionary formatted like {"successes": [list of success strings],
                    "errors": [list of error strings], "infos": [list of info strings]}
    """
    for error in results.get("errors") or []:
        flash(error, "danger")
    for warning in results.get("warnings") or []:
        flash(warning, "warning")
    for success in results.get("successes") or []:
        flash(success, "success")
    for info in results.get("infos") or []:
        flash(info, "info")


def flash_form_errors(form):
    """Flash any errors that were recorded in the form after validation

    :param form: A wtforms form object that we will parse through to find validation errors
    """
    for field in form:
        if field.errors:
            for error in field.errors:
                flash(u"{}: {}".format(field.label.text, error), "danger")
