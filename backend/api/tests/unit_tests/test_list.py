from api.tests.unit_tests.utils import *


class ListTest(APITestCase):
    url = reverse("list-list")
    def setUp(self):
        hook_init_APITestCase(self)
    