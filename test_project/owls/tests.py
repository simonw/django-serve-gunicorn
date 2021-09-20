from django.test import TestCase
from owls.models import Owl


class TestOwls(TestCase):
    def test_owls_loaded(self):
        self.assertEqual(Owl.objects.count(), 5)
