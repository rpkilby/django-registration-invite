from django.template.loader import get_template
from django.test import TestCase


class ImportTest(TestCase):

    def test_import(self):
        import registration_invite  # noqa

    def test_template_packaging(self):
        get_template('registration/invite/email/subject.txt')
        get_template('registration/invite/activation_form.html')
