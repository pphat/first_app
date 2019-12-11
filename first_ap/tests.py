from django.test import TestCase
from first_ap.models import First_A
	
class First_ApHomePage(TestCase):
	def test_first_ap_home_page(self):
		request = self.client.get('/first_ap/')
		self.assertEqual(request.status_code, 200)
	def test_first_ap_list(self):
		request = self.client.get('/first_ap/list/')
		self.assertEqual(request.status_code, 200)
	def test_first_ap_create(self):
		request = self.client.get('/first_ap/create/')
		self.assertEqual(request.status_code, 200)
	def test_first_ap_detail(self):
		name = 'Test Name'
		first_ap = First_A.objects.create(name=name)
		request = self.client.get('/first_ap/detail/test-name/')
		self.assertEqual(request.status_code, 200)
	def test_first_ap_update(self):
		name = 'Test Name'
		first_ap = First_A.objects.create(name=name)
		request = self.client.get('/first_ap/update/test-name/')
		self.assertEqual(request.status_code, 200)
	def test_first_ap_delete(self):
		name = 'Test Name'
		first_ap = First_A.objects.create(name=name)
		request = self.client.get('/first_ap/delete/test-name/')
		self.assertEqual(request.status_code, 200)
	