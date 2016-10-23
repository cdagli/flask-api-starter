#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.model_author import Author, AuthorSchema

route_path_general = Blueprint("route_path_general", __name__)


@route_path_general.route('/v1.0/authors', methods=['POST'])
def create_author():
    """
    Create author endpoint
    ---
    parameters:
        - in: body
          name: body
          schema:
            id: Author
            required:
                - name
                - surname
                - books
            properties:
                name:
                    type: string
                    description: First name of the author
                    default: "John"
                surname:
                    type: string
                    description: Surname of the author
                    default: "Doe"
                books:
                    type: string
                    description: Book list of author
                    type: array
                    items:
                        schema:
                            id: BookSchema
                            properties:
                                title:
                                    type: string
                                    default: "My First Book"
                                year:
                                    type: date
                                    default: "1989-01-01"
    responses:
            200:
                description: Author successfully created
                schema:
                  id: AuthorCreated
                  properties:
                    code:
                      type: string
                    message:
                      type: string
                    value:
                      schema:
                        id: AuthorFull
                        properties:
                            name:
                                type: string
                            surname:
                                type: string
                            books:
                                type: array
                                items:
                                    schema:
                                        id: BookSchema
            422:
                description: Invalid input arguments
                schema:
                    id: invalidInput
                    properties:
                        code:
                            type: string
                        message:
                            type: string
    """
    try:
        data = request.get_json()
        author_schema = AuthorSchema()
        author, error = author_schema.load(data)
        result = author_schema.dump(author.create()).data
        return response_with(resp.SUCCESS_200, value={"author": result})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)


@route_path_general.route('/v1.0/authors', methods=['GET'])
def get_author_list():
    """
    Get author list
    ---
    responses:
            200:
                description: Returns author list
                schema:
                  id: AuthorList
                  properties:
                    code:
                      type: string
                    message:
                      type: string
                    authors:
                        type: array
                        items:
                            schema:
                                id: AuthorSummary
                                properties:
                                    name:
                                        type: string
                                    surname:
                                        type: string
    """
    fetched = Author.query.all()
    author_schema = AuthorSchema(many=True, only=['name', 'surname'])
    authors, error = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"authors": authors})


@route_path_general.route('/v1.0/authors/<int:author_id>', methods=['GET'])
def get_author_detail(author_id):
    """
    Get author detail
    ---
    parameters:
        - name: author_id
          in: path
          description: ID of the author
          required: true
          schema:
            type: integer

    responses:
            200:
                description: Returns author detail
                schema:
                  id: AuthorList
                  properties:
                    code:
                      type: string
                    message:
                      type: string
                    author:
                        id: AuthorFull
                        properties:
                            name:
                                type: string
                            surname:
                                type: string
                            books:
                                type: array
                                items:
                                    schema:
                                        id: BookSchema
                                        properties:
                                            title:
                                                type: string
                                            year:
                                                type: date
    """
    fetched = Author.query.filter_by(id=author_id).first()
    author_schema = AuthorSchema()
    author, error = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"author": author})
