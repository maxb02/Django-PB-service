from django.test import TestCase

# Create your tests here.
from django.utils.translation import activate

def test_uses_index_template(self):
    activate('en')
    response = self.client.get(reverse("home"))
    self.assertTemplateUsed(response, "technicalguides/base.html")