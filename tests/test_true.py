from unittest import TestCase


def test_success():
    assert 1 == 1


class Test(TestCase):

    def test_create_job_url(self):
        self.assertEquals(1, 1)
