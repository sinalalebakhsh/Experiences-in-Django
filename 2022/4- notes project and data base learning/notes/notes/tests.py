from django.test import TestCase
from django.shortcuts import reverse

class ListViewTesting(TestCase):
    def test_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_list_view_by_name(self):
        response = self.client.get(reverse('list views'))
        self.assertEqual(response.status_code, 200)


