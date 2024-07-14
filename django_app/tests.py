from django.test import TestCase


from django.urls import reverse


from . models import Person

# Create your tests here.

class TestPersonModel(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.person = Person.objects.create(name='Limpo',
                                           age=12,
                                           nationality='Zambian')
        
        
    def test_url_used(self):
        
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        
        
    def test_model_content(self):
        
        self.assertEqual(self.person.name,"Limpo")
        self.assertEqual(self.person.age,12)
        self.assertEqual(self.person.nationality,"Zambian")
        
    def test_template_used(self):
        
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response,"Limpo")
        
        
        
        
        
        
    
