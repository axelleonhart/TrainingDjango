from django.test import TestCase, Client
from apps.clientes.models import Cliente, Notas
from apps.clientes.forms import ClienteForm
# Create your tests here.


class TestBasic(TestCase):
    """
    Prueba unitaria para el modelo
    """
    def setUp(self):
        Cliente.objects.create(nombre="Salomon",
                               sexo="m",
                               direccion="no se",
                               email="salomon@mail.com",
                               fecha_nac="1908-03-03")
        Cliente.objects.create(id="4", nombre="Yoline",
                               sexo="f",
                               direccion="algun lado",
                               email="yoline@mail.com",
                               fecha_nac="1956-06-06")

        Notas.objects.create(monto="500",
                             fecha_nota="1989-08-08",
                             cliente_id="4",
                             contenido="tubos")

    def test_animals_can_speak(self):
        salomon = Cliente.objects.get(nombre="Salomon")
        yoline = Cliente.objects.get(nombre="Yoline")
        nota = Notas.objects.get(monto="500")
        self.assertEqual(salomon.direccion, 'no se')
        self.assertEqual(yoline.id, 4)
        self.assertEqual(nota.cliente_id, yoline.id)


class TestForm(TestCase):
    """
    Prueba unitaria para el form
    """
    def test_form(self):
        """
        Prueba unitaria para ver si los datos se validan bien
        """
        form_data = {'nombre': 'adam wesker',
                     'sexo': 'M',
                     'direccion': 'no se por ahi',
                     'email': 'mail@mail.com',
                     'fecha_nac': '1989-09-09'}
        form = ClienteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_raiz(self):
        """
        Prueba para ver si carga bien la pagina principal de clientes
        """
        client = Client()
        res = client.get('/cliente')
        self.assertEqual(res.status_code, 404)


class TestView(TestCase):
    """
    Prueba unitaria para las vistas
    """
    def setUp(self):
        self.client = Client()

    def test_views(self):
        """
        Prueba unitaria para la vista crear
        """
        response = self.client.get('/cliente/crear/')
        self.assertEqual(response.status_code, 200)

    def test_viewsAc(self):
        """
        Prueba unitaria para la vista editar
        """
        cli = Cliente.objects.create(id='1',
                                     nombre='mandarino solis',
                                     sexo='M', direccion='nose por ahi',
                                     email='lo@mail.com',
                                     fecha_nac='1989-09-08')
        response = self.client.get('/cliente/editar/'+cli.id)
        self.assertEqual(response.status_code, 200)

    def test_add_user_view(self):
        """
        Prueba unitaria para ver si carga el
        formulario en la vista correctamente
        """
        response = self.client.get('/cliente/crear/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cliente/cliente_form.html')

    def test_add_client(self):
        """
        Prueba unitaria para mandar los datos por
        post en la vista crear
        """
        response = self.client.post('/cliente/crear/',
                                    {'nombre': 'alberto',
                                     'sexo': 'M',
                                     'direccion': 'no se',
                                     'email': 'alber@mial.com',
                                     'fecha_nac': '1989-03-08'})
        self.assertEqual(response.status_code, 302)
        self.assertEquals(response['Location'], '/cliente/listar/')

    def test_edi_client(self):
        """
        Prueba unitaria para mandar los datos por
        post en la vista editar
        """
        c = Cliente.objects.create(id='89',
                                   nombre='eduardo esdsunia',
                                   sexo='M',
                                   direccion='por ahi en manhattan',
                                   email='mail@mail.com',
                                   fecha_nac='1983-08-08')

        response = self.client.post('/cliente/crear/'+c.id+'/',
                                    {'nombre': 'alberto',
                                     'sexo': 'M',
                                     'direccion': 'no se puede asi',
                                     'email': 'alber@mial.com',
                                     'fecha_nac': '1989-03-08'})
        self.assertEqual(response.status_code, 302)
        self.assertEquals(response['Location'], '/cliente/listar/')

    def test_del_client(self):
        """
        Prueba unitaria para eliminarr los datos por
        post en la vista eliminar
        """
        c = Cliente.objects.create(id='89',
                                   nombre='eduardo esdsunia',
                                   sexo='M',
                                   direccion='por ahi en manhattan',
                                   email='mail@mail.com',
                                   fecha_nac='1983-08-08')

        response = self.client.post('/cliente/eliminar/'+c.id)
        self.assertEqual(response.status_code, 302)
        self.assertEquals(response['Location'], '/cliente/listar/')
