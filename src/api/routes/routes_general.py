#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.model_author import AuthorSchema

route_path_general = Blueprint("route_path_general", __name__)


@route_path_general.route('/v1.0/author', methods=['POST'])
def create_author():
    try:
        data = request.get_json()
        author_schema = AuthorSchema()
        author, error = author_schema.load(data)
        result = author_schema.dump(author.create()).data
        return response_with(resp.SUCCESS_200, value={"value": result})
    except Exception:
        return response_with(resp.BAD_REQUEST_400)
