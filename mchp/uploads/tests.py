from django.test import TestCase


class CreateUserTestCase(TestCase):
    """ Test creation of users.

    """
    # def testUserCreation(self):
    #     from utils import ensure_user_exists
    #
    #     email = 'test@example.com'
    #     user = ensure_user_exists(email)
    #     self.assertNotNull(user)
    #
    #     # e-mail address is required for this method, even though not for users
    #     self.assertRaises(ValueError, ensure_user_exists, 'test')

    def testSuffix(self):
        from .utils import suffix

        name = 'john.q.public'

        self.assertEqual(suffix(name, '', 2), 'jo')
        self.assertEqual(suffix(name, 'jr', 2), 'jr')
        self.assertEqual(suffix(name, '', 8), 'john.q.p')
        self.assertEqual(suffix(name, 'jr', 8), 'john.qjr')
        self.assertEqual(suffix(name, '', 16), 'john.q.public')
        self.assertEqual(suffix(name, 'jr', 16), 'john.q.publicjr')
        with self.assertRaises(ValueError):
            suffix(name, 'jr', 1)  # suffix length cannot exceed max length

    def testIncrementalSuffixes(self):
        from .utils import incremental_suffixes

        name = 'john.q.public'
        suffixes = incremental_suffixes(name, 8)
        self.assertEqual(next(suffixes), 'john.q.p')  # no suffix here
        self.assertEqual(next(suffixes), 'john.q.2')  # one digit now
        self.assertEqual(next(suffixes), 'john.q.3')  # "
        self.assertEqual(next(suffixes), 'john.q.4')  # "
        self.assertEqual(next(suffixes), 'john.q.5')  # "
        self.assertEqual(next(suffixes), 'john.q.6')  # "
        self.assertEqual(next(suffixes), 'john.q.7')  # "
        self.assertEqual(next(suffixes), 'john.q.8')  # "
        self.assertEqual(next(suffixes), 'john.q.9')  # "
        self.assertEqual(next(suffixes), 'john.q10')  # two digits now

        suffixes = incremental_suffixes(name, 16)
        self.assertEqual(next(suffixes), 'john.q.public')   # no suffix here
        self.assertEqual(next(suffixes), 'john.q.public2')  # one digit now
        self.assertEqual(next(suffixes), 'john.q.public3')  # "
        self.assertEqual(next(suffixes), 'john.q.public4')  # "
        self.assertEqual(next(suffixes), 'john.q.public5')  # "
        self.assertEqual(next(suffixes), 'john.q.public6')  # "
        self.assertEqual(next(suffixes), 'john.q.public7')  # "
        self.assertEqual(next(suffixes), 'john.q.public8')  # "
        self.assertEqual(next(suffixes), 'john.q.public9')  # "
        self.assertEqual(next(suffixes), 'john.q.public10')  # two digits now

        suffixes = incremental_suffixes(name, 1)
        self.assertEqual(next(suffixes), 'j')  # no suffix at first
        self.assertEqual(next(suffixes), '2')  # one digit now
        self.assertEqual(next(suffixes), '3')  # "
        self.assertEqual(next(suffixes), '4')  # "
        self.assertEqual(next(suffixes), '5')  # "
        self.assertEqual(next(suffixes), '6')  # "
        self.assertEqual(next(suffixes), '7')  # "
        self.assertEqual(next(suffixes), '8')  # "
        self.assertEqual(next(suffixes), '9')  # "
        with self.assertRaises(ValueError):
            next(suffixes)                     # can't do two digits
