import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from peaks.models import Pereval_added, CustomUser, Coords, Level, Images
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
            level=Level.objects.create(
                winter="1A",
                summer="1A",
                autumn="1A",
                spring="",
            ),
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
            level=Level.objects.create(
                winter="1b",
                summer="1b",
                autumn="12",
                spring="",
            ),
        )

    def test_get_list(self):
        url = reverse('pereval-list')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_test1, self.pereval_test2], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(first=2, second=len(serializer_data))

    # def test_get_detail(self):
    #     url = reverse('pereval-detail', kwargs={'pk': self.pereval_1.pk})
    #     response = self.client.get(url)
    #     serializer_data = PerevalSerializer(self.pereval_1).data
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, serializer_data)
