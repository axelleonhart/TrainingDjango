from django.test import TestCase,Client
from apps.contratos.forms import ContratoForm
from apps.contratos.models import Contrato, Movimiento
from apps.proveedores.models import Proveedor

# Create your tests here.
"""
Prueba unitaria para el modelo
"""
class TestModel(TestCase):

    def setUp(self):
        Proveedor.objects.create(nombre="adrian", rfc="roman", domicilio="no se", telefono="88898", email="adrian@mail.com")
        Contrato.objects.create(id_contrato="1", monto="200", rfc=Proveedor.objects.get(nombre="adrian"), fecha="1989-08-08")
        
        

    def test_proveedores_clientes(self):
        salomon = Proveedor.objects.get(rfc="roman")
        cliente = Contrato.objects.get(rfc="roman")
        
        self.assertEqual(salomon.domicilio, 'no se')
        #self.assertEqual(cliente.rfc, salomon.nombre)
        self.assertEqual(salomon.pk, "roman")
        

"""
Prueba unitaria para el Form
"""
class TestForm(TestCase):
    def test_form(self):
        rfc = Proveedor.objects.create(rfc='Masti89')
        form_data = {'id_contrato': '2',
                    'monto': '200',
                    'rfc': rfc.rfc,
                    'fecha': '1989-01-02'}
        form = ContratoForm(data=form_data)
        self.assertTrue(form.is_valid())


"""
Prueba unitaria para la vista
"""
class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_views(self):
        """
        Prueba la vista crear
        """
        response = self.client.get('/contrato/crear/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contrato/contrato_form.html')
        #self.assertEqual(len(response.context['cliente']), 5)

    def test_viewsDel(self):
        """
        Prueba la vista eliminar
        """
        rfc = Proveedor.objects.create(rfc='Masti89')
        n =  Contrato.objects.create(id_contrato='2', monto='200', rfc=Proveedor.objects.get(rfc="Masti89"), fecha='1989-09-08')
        response = self.client.get('/contrato/eliminar/2/')
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
        Prueba agregar un contrato a la vista crear
        """
        rfc = Proveedor.objects.create(rfc='Masti89')
        response = self.client.post('/contrato/crear/', {'id_contrato': '3', 'monto': '400', 'rfc': rfc.rfc, 'fecha': '1989-09-08'})
        self.assertEqual(response.status_code, 302)
        self.assertEquals(response['Location'], '/contrato/listar/')
        #self.assertTrue(response.content)
