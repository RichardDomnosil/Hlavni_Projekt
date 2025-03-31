from flask import Blueprint, render_template, session, flash, redirect, url_for
from app.login import log_required, login_required

bp = Blueprint('saloon', __name__, url_prefix='/saloon')

@bp.route('/')
@login_required
def index():
    return render_template("saloon.html")

