#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from api.utils.factory import create_app
from api.utils.database import db
from api.utils.config import TestingConfig


class BaseTestCase(unittest.TestCase):
    """A base test case"""
    def setUp(self):
        app = create_app(TestingConfig)
        app.app_context().push()
        self.app = app.test_client()

    def tearDown(self):
        db.session.close_all()
        db.drop_all()
