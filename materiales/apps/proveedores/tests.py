from django.test import TestCase, Client
from apps.proveedores.forms import ProveedorForm
from apps.proveedores.models import Proveedor
# Create your tests here.


class TestModel(TestCase):
    """
    Prueba unitaria para el modelo
    """
    def setUp(self):
        Proveedor.objects.create(nombre="drake",
                                 rfc="romano",
                                 domicilio="barcelona #32",
                                 telefono="569382",
                                 email="drake@mail.com")

        Proveedor.objects.create(nombre="sully",
                                 rfc="suizo",
                                 domicilio="sargoza #43",
                                 telefono="930839",
                                 email="sully@mail.com")

    def test_proveedores_model(self):
        prove1 = Proveedor.objects.get(rfc="romano")
        prove2 = Proveedor.objects.get(rfc="suizo")
        self.assertEqual(prove1.domicilio, 'barcelona #32')
        # self.assertEqual(cliente.rfc, salomon.nombre)
        self.assertEqual(prove2.pk, "suizo")


class TestForm(TestCase):
    """
    Prueba unitaria para el form
    """
    def test_form(self):
        form_data = {'nombre': 'drake dominguez',
                     'rfc': 'romano',
                     'domicilio': 'barcelona #32',
                     'telefono': '9283782823',
                     'email': 'drake@mail.com'}
        form = ProveedorForm(data=form_data)
        self.assertTrue(form.is_valid())


class TestView(TestCase):
    """
    Prueba unitaria para la vista
    """
    def setUp(self):
        self.client = Client()

    def test_views(self):
        """
        Prueba la vista nuevo
        """
        response = self.client.get('/proveedor/nuevo/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proveedor/proveedor_form.html')
        # self.assertEqual(len(response.context['cliente']), 5)

    def test_viewsDel(self):
        """
        Prueba la vista eliminar
        """
        rfc = Proveedor.objects.create(rfc='Masti89')
        response = self.client.get('/proveedor/eliminar/'+rfc.rfc+'/')
        self.assertTemplateUsed(response, 'proveedor/proveedor_delete.html')
        self.assertEqual(response.status_code, 200)

    def test_viewsEd(self):
        """
        Prueba la vista editar
        """
        rfc = Proveedor.objects.create(rfc='Masti89')
        response = self.client.get('/proveedor/editar/'+rfc.rfc+'/')
        self.assertTemplateUsed(response, 'proveedor/proveedor_form.html')
        self.assertEqual(response.status_code, 200)

    def test_viewsLis(self):
        """
        Prueba la vista listar
        """
        response = self.client.get('/proveedor/listar/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proveedor/proveedor_lista.html')

    def test_add_client(self):
        """
        Prueba agregar un proveedor a la vista nuevo
        """

        response = self.client.post('/proveedor/nuevo/',
                                    {'nombre': 'arellano',
                                     'rfc': 'romano',
                                     'domicilio': 'francia #23',
                                     'telefono': '1993931245',
                                     'email': 'arellamp@mail.com'})
        self.assertEqual(response.status_code, 302)
        self.assertEquals(response['Location'], '/proveedor/listar/')

    def test_edi_client(self):
        """
        Prueba editar un proveedor en la vista editar
        """
        rfc = Proveedor.objects.create(rfc='Masti89')

        response = self.client.post('/proveedor/editar/'+rfc.rfc+'/',
                                    {'nombre': 'alberto soriano',
                                     'rfc': rfc.rfc,
                                     'domicilio': 'españa suecia',
                                     'telefono': '1989863459',
                                     'email': 'alberto@mail.com'})
        self.assertEqual(response.status_code, 302)
        self.assertEquals(response['Location'], '/proveedor/listar/')

    def test_del_client(self):
        """
        Prueba eliminar un proveedor
        """
        rfc = Proveedor.objects.create(rfc='Masti89')

        response = self.client.post('/proveedor/eliminar/'+rfc.rfc+'/')
        self.assertEqual(response.status_code, 302)
        self.assertEquals(response['Location'], '/proveedor/listar/')
