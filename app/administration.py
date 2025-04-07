from flask import Blueprint, render_template, session, redirect, url_for, flash
from app.db import db_execute
from functools import wraps

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "username" not in session or session.get("role") != "admin":
            flash("Přístup pouze pro administrátory.", "danger")
            return redirect(url_for("index"))
        return func(*args, **kwargs)
    return wrapper

@admin_bp.route("/")
@admin_required
def admin_dashboard():
    users = db_execute("SELECT * FROM users")
    return render_template("admin/dashboard.html", users=users)
