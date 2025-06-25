from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from historia.models import Historia
from historia.forms import FormularioHistoria
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class TestesModelHistoria(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='autor', password='123456')
        self.historia = Historia(
            titulo='História Teste',
            genero=1,
            estilo=1,
            status=1,
            autor=self.user
        )

    def test_str_repr(self):
        self.assertEqual(str(self.historia), 'História Teste (Fantasia)') 


class TestesViewListarHistorias(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('listar-historias')
        Historia.objects.create(
            titulo='Teste 1',
            genero=1,
            status=1,
            estilo=1,
            autor=self.user
        )

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context.get('historias')), 1)


class TestesViewCriarHistoria(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('criar-historias')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioHistoria)

    def test_post(self):
        data = {
            'titulo': 'Nova História',
            'genero': 1,
            'estilo': 1,
            'status': 1,
            'sinopse': 'Exemplo de sinopse...'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-historias'))
        self.assertEqual(Historia.objects.count(), 1)
        self.assertEqual(Historia.objects.first().titulo, 'Nova História')


class TestesViewEditarHistoria(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='12345')
        self.client.force_login(self.user)
        self.historia = Historia.objects.create(
            titulo='Original',
            genero=1,
            estilo=1,
            status=1,
            autor=self.user
        )
        self.url = reverse('editar-historia', kwargs={'pk': self.historia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].instance.pk, self.historia.pk)

    def test_post(self):
        data = {
            'titulo': 'Editado',
            'genero': 2,
            'estilo': 2,
            'status': 2,
            'sinopse': 'Editada...'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.historia.refresh_from_db()
        self.assertEqual(self.historia.titulo, 'Editado')
        self.assertEqual(self.historia.genero, 2)


class TestesViewDeletarHistoria(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='12345')
        self.client.force_login(self.user)
        self.historia = Historia.objects.create(
            titulo='Deletável',
            genero=1,
            estilo=1,
            status=1,
            autor=self.user
        )
        self.url = reverse('deletar-historia', kwargs={'pk': self.historia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get('object').pk, self.historia.pk)

    def test_post(self):
        response = self.client.post(self.url)
        self.assertRedirects(response, reverse('listar-historias'))
        self.assertEqual(Historia.objects.count(), 0)

class TestesAPIListarHistorias(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        Historia.objects.create(titulo='História 1', genero=1, autor=self.user, status=1)

    def test_listar_historias_api(self):
        url = reverse('api-historias')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

class TestesAPIDeletarHistoria(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.historia = Historia.objects.create(titulo='Para Deletar', genero=1, autor=self.user, status=1)

    def test_deletar_historia_api(self):
        url = reverse('api-deletar-historia', kwargs={'pk': self.historia.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Historia.objects.count(), 0)

class TesteViewDetalhesHistoria(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='123')
        self.client.force_login(self.user)
        self.historia = Historia.objects.create(titulo='Detalhes Teste', genero=1, autor=self.user, status=1)

    def test_detalhes_historia(self):
        url = reverse('detalhes-historia', kwargs={'pk': self.historia.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get('object').pk, self.historia.pk)
