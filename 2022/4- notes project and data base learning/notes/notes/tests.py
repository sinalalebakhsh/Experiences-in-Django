from django.test import TestCase

class ListViewTesting(TestCase):
    def test_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


