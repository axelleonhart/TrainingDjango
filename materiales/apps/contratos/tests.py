from django.test import TestCase, Client
from apps.contratos.forms import ContratoForm
from apps.contratos.models import Contrato
from apps.proveedores.models import Proveedor


class TestModel(TestCase):
    """
    Prueba unitaria para el modelo
    """
    def setUp(self):
        Proveedor.objects.create(nombre="adrian",
                                 rfc="roman",
                                 domicilio="no se",
                                 telefono="88898",
                                 email="adrian@mail.com")

        Contrato.objects.create(id_contrato="1",
                                monto="200",
                                rfc=Proveedor.objects.get(nombre="adrian"),
                                fecha="1989-08-08")

    def test_proveedores_clientes(self):
        salomon = Proveedor.objects.get(rfc="roman")
        cliente = Contrato.objects.get(rfc="roman")
        self.assertEqual(salomon.domicilio, 'no se')
        self.assertEqual(cliente.pk, "1")


class TestForm(TestCase):
    """
    Prueba unitaria para el Form
    """
    def test_form(self):
        rfc = Proveedor.objects.create(rfc='Masti89')
        form_data = {'id_contrato': '2',
                     'monto': '200',
                     'rfc': rfc.rfc,
                     'fecha': '1989-01-02'}
        form = ContratoForm(data=form_data)
        self.assertTrue(form.is_valid())


class TestView(TestCase):
    """
    Prueba unitaria para la vista
    """
    def setUp(self):
        self.client = Client()

    def test_views(self):
        """
        Prueba la vista crear
        """
        response = self.client.get('/contrato/crear/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contrato/contrato_form.html')

    def test_viewsDel(self):
        """
        Prueba la vista eliminar
        """

        n = Contrato.objects.create(id_contrato='2',
                                    monto='200',
                                    rfc=Proveedor.objects.create(
                                        rfc='Masti50'),
                                    fecha='1989-09-08')

        response = self.client.get('/contrato/eliminar/'+n.id_contrato+'/')
        self.assertTemplateUsed(response, 'contrato/contrato_delete.html')
        self.assertEqual(response.status_code, 200)

    def test_viewsLis(self):
        """
        Prueba la vista listar
        """
        response = self.client.get('/contrato/listar/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contrato/contrato_lista.html')

    def test_add_client(self):
        """
        Prueba agregar un contrato en la vista crear
        """
        rfc = Proveedor.objects.create(rfc='Masti89')
        response = self.client.post('/contrato/crear/',
                                    {'id_contrato': '3',
                                     'monto': '400',
                                     'rfc': rfc.rfc,
                                     'fecha': '1989-09-08'})
        self.assertEqual(response.status_code, 302)
        self.assertEquals(response['Location'], '/contrato/listar/')

    def test_edi_client(self):
        """
        Prueba editar un contrato en la vista editar
        """
        rfc = Proveedor.objects.create(rfc='Masti89')
        n = Contrato.objects.create(id_contrato='2',
                                    monto='200',
                                    rfc=Proveedor.objects.create(
                                        rfc='Masti50'),
                                    fecha='1989-09-08')

        response = self.client.post('/contrato/editar/'+n.id_contrato+'/',
                                    {'id_contrato': '3',
                                     'monto': '400',
                                     'rfc': rfc.rfc,
                                     'fecha': '1989-10-08'})
        self.assertEqual(response.status_code, 302)
        self.assertEquals(response['Location'], '/contrato/listar/')

    def test_del_client(self):
        """
        Prueba eliminar un contrato en la vista eliminar
        """

        n = Contrato.objects.create(id_contrato='2',
                                    monto='200',
                                    rfc=Proveedor.objects.create(
                                        rfc='Masti50'),
                                    fecha='1989-09-08')

        response = self.client.post('/contrato/eliminar/'+n.id_contrato+'/')
        self.assertEqual(response.status_code, 302)
        self.assertEquals(response['Location'], '/contrato/listar/')
