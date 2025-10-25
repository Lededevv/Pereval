import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from peaks.models import Pereval_added, CustomUser, Coords, Level
from peaks.serializers import PerevalSerializer


class PerevalTestCase(APITestCase):
    def setUp(self):
        self.pereval_test1 = Pereval_added.objects.create(
            beauty_title="beauty_title_test1",
            title="title_test1",
            other_titles="other_title_test1",
            connect="connect_test1",
            add_time="2021-09-22T13:18:13Z",
            user=CustomUser.objects.create(
                email="emailtest1@mail.ru",
                last_name="fam_test1",
                first_name="name_test1",
                otc="otc_test1",
                phone="8900000001",
            ),
            coords=Coords.objects.create(
                latitude=123.00,
                longitude=456.00,
                height=1001,
            ),
        )
        self.level = Level.objects.create(
            winter="1A",
            summer="1A",
            autumn="1A",
            spring="",
            pereval=self.pereval_test1
        )

        self.pereval_test2 = Pereval_added.objects.create(
            beauty_title="beauty_title_test2",
            title="title_test2",
            other_titles="other_title_test2",
            connect="connect_test2",
            add_time="2021-09-22T13:18:13Z",
            user=CustomUser.objects.create(
                email="emailtest2@mail.ru",
                last_name="fam_test2",
                first_name="name_test2",
                otc="otc_test2",
                phone="8900000001",
            ),
            coords=Coords.objects.create(
                latitude=321.00,
                longitude=654.00,
                height=1001,
            ),
        )
        self.level = Level.objects.create(
            winter="1b",
            summer="1b",
            autumn="12",
            spring="",
            pereval=self.pereval_test2

        )

    def test_get_list(self):
        url = reverse('perevals-list')

        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_test1, self.pereval_test2], many=True,
                                            context={'request': response.wsgi_request}).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(first=2, second=len(serializer_data))

    def test_get_detail(self):
        url = reverse('perevals-detail', kwargs={'pk': self.pereval_test1.pk})
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_test1, context={'request': response.wsgi_request}).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)

    def test_post_perevals(self):
        url = reverse('perevals-list')
        data = {
            "beauty_title": "ПЕРЕВАЛ-ТЕСТ",
            "title": "ПЕРЕВАЛ-ТЕСТ",
            "other_titles": "ПЕРЕВАЛ-ТЕСТ",
            "connect": "",
            "add_time": "2021-09-22T13:18:13",
            "user": {
                "email": "test@test.com",
                "fam": "Пользователь",
                "name": "Пользователь",
                "otc": "Пользователь",
                "phone": "89000000003"
            },
            "coords": {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200"
            },
            "level": {
                "winter": "1B",
                "summer": "1B",
                "autumn": "1B",
                "spring": "1B"
            },
            "images": [
                {
                    "data": "КАРТИНКА1",
                    "title": "ЗАГОЛОВОК1"
                },
                {
                    "data": "КАРТИНКА2",
                    "title": "ЗАГОЛОВОК2"
                }
            ]
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json ')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Pereval_added.objects.all().count(), 3)

    def test_patch_perevals(self):
        url = reverse('perevals-detail', kwargs={'pk': self.pereval_test1.pk})
        data = {
            "beauty_title": "beauty_title_test_new",
            "title": "title_new",
            "other_titles": "other_titles_test_new",
            "connect": "connect_test_new",
            "add_time": "2021-09-22T13:18:13Z",
            "user": {
                "email": "emailtest1@mail.ru",
                "last_name": "fam_test1",
                "first_name": "name_test1",
                "otc": "otc_test1",
                "phone": "8900000001"
            },
            "coords": {
                "latitude": "123.00",
                "longitude": "321.00",
                "height": 1001
            },
            "level": {
                "winter": "1A",
                "summer": "1A",
                "autumn": "1A",
                "spring": "1C"
            },
            "images": [
                {
                    "title": "title_image_1_1",
                    "data": "data_image_1_1"
                },
                {
                    "title": "title_image_1_2",
                    "data": "data_image_1_2"
                }
            ]
        }
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')

        # Добавьте этот вывод
        self.pereval_test1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.pereval_test1.beauty_title, 'beauty_title_test_new')
        self.assertEqual(self.pereval_test1.title, 'title_new')
        self.assertEqual(self.pereval_test1.coords.latitude, 123.00)
        self.assertEqual(self.pereval_test1.coords.longitude, 321.00)
        self.assertEqual(self.pereval_test1.level.spring, '1C')
