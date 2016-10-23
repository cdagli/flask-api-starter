#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from api.models.model_book import BookSchema


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    created = db.Column(db.DateTime, server_default=db.func.now())
    books = db.relationship('Book', backref='Author')

    def __init__(self, name, surname, books=[]):
        self.name = name
        self.surname = surname
        self.books = books

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class AuthorSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Author
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    surname = fields.String(required=True)
    created = fields.String(dump_only=True)
    books = fields.Nested(BookSchema, many=True)
