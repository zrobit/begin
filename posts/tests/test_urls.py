from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve


class UrlsTests(TestCase):

    def test_reverse_urls(self):
        #Test de urls simples, sin argumentos

        url = reverse('home')
        self.assertEqual(url, '/')

        # url = reverse('categories')
        # self.assertEqual(url, '/categories/')

        #Test de urls con argumentos

        url = reverse('detail', args=['2014', '01', 'Esto-es-un-titulo-111'])
        self.assertEqual(url, '/2014/01/Esto-es-un-titulo-111/')


    def test_resolve_urls(self):

        url_resolve = resolve('/')
        self.assertEqual(url_resolve.view_name, 'home')

        url_resolve = resolve('/2014/01/Esto-es-un-titulo-111/')
        self.assertEqual(url_resolve.view_name, 'detail')


