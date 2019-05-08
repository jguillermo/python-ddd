# -*- coding: utf-8 -*-

import unittest

from tests.unit.user import TestUserCreateService


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(TestUserCreateService))
    return suite


if __name__ == '_main_':
    unittest.TextTestRunner(verbosity=2).run(suite())
