from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from app.db import db_execute, db_execute_one
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

@admin_bp.route("/add_user", methods=["GET", "POST"])
@admin_required
def add_user():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        role = request.form["role"]

        db_execute("INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)",
                   (username, password, email, role))
        flash("Uživatel přidán.", "success")
        return redirect(url_for("admin.admin_dashboard"))
    return render_template("admin/add_user.html")

@admin_bp.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
@admin_required
def edit_user(user_id):
    user = db_execute_one("SELECT * FROM users WHERE id = ?", (user_id,))
    if not user:
        flash("Uživatel neexistuje.", "danger")
        return redirect(url_for("admin.admin_dashboard"))

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        role = request.form["role"]

        db_execute("UPDATE users SET username = ?, email = ?, role = ? WHERE id = ?",
                   (username, email, role, user_id))
        flash("Uživatel upraven.", "success")
        return redirect(url_for("admin.admin_dashboard"))

    return render_template("admin/edit_user.html", user=user)

@admin_bp.route("/delete_user/<int:user_id>")
@admin_required
def delete_user(user_id):
    db_execute("DELETE FROM users WHERE id = ?", (user_id,))
    flash("Uživatel smazán.", "info")
    return redirect(url_for("admin.admin_dashboard"))
