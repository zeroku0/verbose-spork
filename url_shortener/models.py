import random
from string import digits, ascii_letters
from url_shortener import db


class ShortUrl(db.Model):

    __tablename__ = "shortlinks"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String, unique=True, nullable=False)
    long_url = db.Column(db.String, nullable=False)

    def __init__(self, key, long_url):
        self.key = key
        self.long_url = long_url


def generate_key():
    length = random.randint(3, 8)
    return ''.join(random.choices(ascii_letters + digits + "_-", k=length))
