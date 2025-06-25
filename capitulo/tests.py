from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from historia.models import Historia
from capitulo.models import Capitulo

class TestesViewCriarCapitulo(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='autor', password='123')
        self.client.force_login(self.user)
        self.historia = Historia.objects.create(
            titulo='História Teste', genero=1, autor=self.user, status=1
        )
        self.url = reverse('criar-capitulo', kwargs={'historia_id': self.historia.id})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        data = {
            'titulo': 'Capítulo 1',
            'descricao': 'Notas iniciais',
            'conteudo': 'Era uma vez...',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Capitulo.objects.count(), 1)
        self.assertEqual(Capitulo.objects.first().titulo, 'Capítulo 1')

class TesteViewDetalhesCapitulo(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='autor', password='123')
        self.client.force_login(self.user)
        self.historia = Historia.objects.create(titulo='História', genero=1, autor=self.user, status=1)
        self.capitulo = Capitulo.objects.create(
            titulo='Capítulo 1', descricao='Notas', conteudo='Texto...', historia=self.historia
        )
        self.url = reverse('ver-capitulo', kwargs={'pk': self.capitulo.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get('object').pk, self.capitulo.pk)

class TesteViewEditarCapitulo(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='autor', password='123')
        self.client.force_login(self.user)
        self.historia = Historia.objects.create(titulo='História', genero=1, autor=self.user, status=1)
        self.capitulo = Capitulo.objects.create(
            titulo='Original', descricao='...', conteudo='...', historia=self.historia
        )
        self.url = reverse('editar-capitulo', kwargs={'pk': self.capitulo.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        data = {
            'titulo': 'Editado',
            'descricao': 'Nova nota',
            'conteudo': 'Novo conteúdo',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.capitulo.refresh_from_db()
        self.assertEqual(self.capitulo.titulo, 'Editado')

class TesteViewDeletarCapitulo(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='autor', password='123')
        self.client.force_login(self.user)
        self.historia = Historia.objects.create(titulo='História', genero=1, autor=self.user, status=1)
        self.capitulo = Capitulo.objects.create(
            titulo='Capítulo', descricao='...', conteudo='...', historia=self.historia
        )
        self.url = reverse('deletar-capitulo', kwargs={'pk': self.capitulo.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get('object').pk, self.capitulo.pk)

    def test_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Capitulo.objects.count(), 0)
