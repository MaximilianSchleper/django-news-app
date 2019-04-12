from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class ArcticlePageTestsLoggedOut(TestCase):

  def test_articles_page_status_code(self):
    response = self.client.get('/articles')
    self.assertEqual(response.status_code, 301)

  def test_view_url_by_name(self):
    response = self.client.get(reverse('article_list'))
    self.assertEqual(response.status_code, 302)

  def test_article_creation_page_status_code(self):
    response = self.client.get(reverse('article_new'))
    self.assertEqual(response.status_code, 302)

# class ArticleCRUDTests(TestCase):
  # todo: test article CRUD

# test article permissions