import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from url_shortener.forms import ShortForm, ReportForm


app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from url_shortener.models import ShortUrl, generate_key

with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def index():

    form = ShortForm()
    form2 = ReportForm()

    if form.validate_on_submit():

        long_url = form.url.data

        if ShortUrl.query.filter_by(long_url=long_url).first():
            t = ShortUrl.query.filter_by(long_url=long_url).first().key
            return render_template("report.html", form=form2, res=request.base_url+t)

        else:
            
            key = generate_key()
            while ShortUrl.query.filter_by(key=key).first():
                key = generate_key()
            new_record = ShortUrl(key, long_url)
            db.session.add(new_record)
            db.session.commit()
            return render_template("report.html", form=form2, res=request.base_url+key)

    return render_template("index.html", form=form)


@app.route("/<key>")
def redir(key):

    record = ShortUrl.query.filter_by(key=key).first()

    if record:
        return redirect(record.long_url)

    form2 = ReportForm()

    return render_template("404.html", form=form2), 404
