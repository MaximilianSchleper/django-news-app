from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class ArcticlePageTests(TestCase):

  def test_articles_page_status_code_when_logged_out(self):
    response = self.client.get('/articles')
    self.assertEqual(response.status_code, 301)

  def test_view_url_by_name(self):
    response = self.client.get(reverse('article_list'))
    self.assertEqual(response.status_code, 200)

  def test_view_uses_correct_template(self):
    response = self.client.get(reverse('article_list'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'article_list.html')
  
# class ArticleCRUDTests(TestCase):
  # todo: test article CRUD

# test article permissions