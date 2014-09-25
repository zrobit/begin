from django.test import TestCase
from posts.models import Category, Tag

class CategoryTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Category Name')
        # self.category.save()

    def test_simple_create(self):
        self.assertEqual(self.category.name, 'Category Name')
        self.assertEqual(self.category.slug, 'category-name')
        category = Category.objects.get(pk=1)
        self.assertEqual(category.slug, 'category-name')


class TagTest(TestCase):

    def setUp(self):
        self.first_tag = Tag.objects.create(name='first tag')
        self.second_tag = Tag.objects.create(
            name='SecondTag', status='featured')

    def test_simple_create(self):
        self.assertEqual(self.first_tag.name, 'first tag')
        self.assertEqual(self.first_tag.slug, 'first-tag')
        first_tag = Tag.objects.get(pk=1)
        self.assertEqual(first_tag.slug, 'first-tag')
        self.assertEqual(first_tag.status, 'published')

        self.assertEqual(self.second_tag.name, 'SecondTag')
        self.assertEqual(self.second_tag.slug, 'secondtag')
        second_tag = Tag.objects.get(slug='secondtag')
        # self.assertEqual(second_tag.slug, 'secondtag')
        self.assertEqual(second_tag.status, 'featured')

