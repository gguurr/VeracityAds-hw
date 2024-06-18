from django.test import TestCase,Client
from .models import Recipe
import json

TEST_RECEPIE =json.dumps({"title": "Spaghetti Carbonara","description": "A classic Italian pasta dish with a creamy egg sauce.","ingredients": ["200g spaghetti","100g pancetta","2 large eggs","50g grated Parmesan cheese","Salt","Black pepper"],"instructions": ["do A", "now do B"],"category": "Pasta"})

class APITests(TestCase):
    def setUp(self):
        self.c = Client()

    def test_create_recipe(self):
        r = self.c.post("/recipes/", data=TEST_RECEPIE, content_type='application/json')
        
        self.assertEqual(r.status_code,200)
        r = self.c.post("/recipes/", {}, content_type='application/json')
        
        self.assertEqual(r.status_code,400)

    def test_list_recipes(self):
        r = self.c.post("/recipes/",data=TEST_RECEPIE, content_type='application/json')
        r = self.c.get("/recipes/")
        self.assertEqual(r.status_code,200)
        self.assertEqual(len(json.loads(r.content.decode())), 1)
    
    def test_get_recipe(self):
        r = self.c.post("/recipes/", data=TEST_RECEPIE, content_type='application/json')
        r = self.c.get("/recipes/1")
        self.assertEqual(r.status_code,200)
        self.assertEqual(len(json.loads(r.content.decode())), 5)

    def test_update_recipe(self):
        r = self.c.post("/recipes/", data=TEST_RECEPIE, content_type='application/json')
        r = self.c.put("/recipes/1", data='{"title":"Not Spaghetti Carbonara"}', content_type='application/json')
        r = self.c.get("/recipes/1")
        self.assertEqual(r.status_code,200)
        self.assertEqual((json.loads(r.content.decode()))["title"],"Not Spaghetti Carbonara")
    

    def test_delete_recipe(self):
        r = self.c.post("/recipes/",data=TEST_RECEPIE, content_type='application/json')
        r = self.c.delete("/recipes/1")
        self.assertEqual(r.status_code,200)
        r = self.c.get("/recipes/")
        self.assertEqual(len(json.loads(r.content.decode())),0)