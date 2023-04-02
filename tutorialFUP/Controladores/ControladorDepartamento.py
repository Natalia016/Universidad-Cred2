from tutorialFUP.Modelos.Departamento import Departamento
from tutorialFUP.Repositorio.RepositorioDepartamento import RepositorioDepartamento
"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorDepartamento():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """
    def __init__(self):
        print("Creando Controlador Deptos")
        self.repositorioDepartamento = RepositorioDepartamento()

    def index(self):
         print("Listando todos los Deptos")
         return self.repositorioDepartamento.findAll()

    def create(self, infoDepartamento):
        print("Creando un depto")
        nuevoDepartamento = Departamento(infoDepartamento)
        return self.repositorioDepartamento.save(nuevoDepartamento)

    def show(self, id):
        print("Mostrando un depto con id ", id)
        elDepartamento = Departamento(self.repositorioDepartamento.findById(id))
        return elDepartamento.__dict__
    
    def update(self, id, infoDepartamento):
        print("Actualizando depto con id ", id)
        departamentoActual = Departamento(self.repositorioDepartamentoto.findById(id))
        departamentoActual.nombre = infoDepartamento["nombre"]
        departamentoActual.descripcion = infoDepartamento["descripcion"]
        return self.repositorioDepartamento.save(departamentoActual)

    def delete(self, id):
        return self.repositorioDepartamento.delete(id)
