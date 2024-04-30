from db import db
from flask_bcrypt import check_password_hash
from forms.auth_forms import login_form, register_form
from datetime import datetime, timezone
from db import User
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.routing import BuildError
from sqlalchemy.exc import IntegrityError, DataError, DatabaseError, InterfaceError, InvalidRequestError
from flask import render_template, redirect, flash, url_for, Blueprint, session


auth_bp = Blueprint('auth', __name__)


# Login
@auth_bp.route("/login/", methods=("GET", "POST"), strict_slashes=False)
def login():
    if current_user.is_authenticated:
        return redirect(url_for("chat"))
    form = login_form()
    if form.validate_on_submit():
        try:
            user: User = User.query.filter_by(email=form.email.data).first()
            if not user:
                flash(f"No account found for {form.email.data}", "danger")
                return redirect(url_for("auth.register"))
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                user.last_login = datetime.now(timezone.utc)
                db.session.commit()
                session['user_id'] = user.id
                return redirect(url_for('chat'))
            else:
                flash("Invalid Username or password!", "danger")
        except Exception as e:
            flash(e, "danger")

    return render_template("auth/login.html",
                           form=form,
                           text="Login",
                           title="Login",
                           btn_action="Login"
                           )


# Register route
@auth_bp.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = register_form()
    if form.validate_on_submit():
        from app import bcrypt
        try:
            email = form.email.data
            pwd = form.password.data
            username = form.username.data

            newuser = User(
                username=username,
                email=email,
                password=bcrypt.generate_password_hash(pwd),
            )
            db.session.add(newuser)
            db.session.commit()
            flash(f"Account Succesfully created", "success")
            return redirect(url_for("auth.login"))

        except InvalidRequestError:
            db.session.rollback()
            flash(f"Something went wrong!", "danger")
        except IntegrityError:
            db.session.rollback()
            flash(f"User already exists!.", "warning")
        except DataError:
            db.session.rollback()
            flash(f"Invalid Entry", "warning")
        except InterfaceError as e:
            print(e)
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except DatabaseError as e:
            print(e)
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except BuildError:
            db.session.rollback()
            flash(f"An error occured !", "danger")
            raise
    else:
        print(form.errors)
    return render_template("auth/register.html",
                           form=form,
                           text="Create account",
                           title="Register",
                           btn_action="Register account"
                           )


# Logout route
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
