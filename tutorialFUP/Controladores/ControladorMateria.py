from tutorialFUP.Modelos.Materia import Materia
from tutorialFUP.Modelos.Departamento import Departamento
from tutorialFUP.Repositorio.RepositorioMateria import RepositorioMateria
from tutorialFUP.Repositorio.RepositorioDepartamento import RepositorioDepartamento


"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorMateria():

    def __init__(self):
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento = RepositorioDepartamento()

    def index(self):
        print("Listar todos los materia")
        return self.repositorioMateria.findAll()

    def create(self, infoMateria):
        nuevoMateria = Materia(infoMateria)
        return self.repositorioMateria.save(nuevoMateria)

    def show(self, id):
        print("Mostrando una materia con id ", id)
        laMateria = Materia(self.repositorioMateria.findById(id))
        return laMateria.__dict__

    def update(self, id,infoMateria):
        """print("Actualizando depto con id ", id)
        laMateria = Materia(laMateria)
        return Materia._dict_
        """
        materiaActual = Materia(self.repositorioMateria.findById(id))
        materiaActual.nombre = infoMateria["nombre"]
        materiaActual.creditos = infoMateria["creditos"]
        return self.repositorioMateria.save(materiaActual)

    def delete(self, id):
        return self.repositorioMateria.delete(id)

    """
    Relación departamento y materia
    """

    def asignarDepartamento(self,id,id_departamento):
        materiaActual = Materia(self.repositorioMateria.findById(id))
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
        materiaActual.departamento = departamentoActual
        return self.repositorioMateria.save(materiaActual)