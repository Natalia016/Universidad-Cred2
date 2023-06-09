from tutorialFUP.Modelos.Estudiante import Estudiante
from tutorialFUP.Repositorio.RepositorioEstudiante import RepositorioEstudiante
"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorEstudiante():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """
    def __init__(self):
        self.repositorioEstudiante = RepositorioEstudiante()
        print("Creando Controlador Estudiante")

    def index(self):
        print("Listar todos los estudiantes")
        return self.repositorioEstudiante.findAll()

    def create(self, elEstudiante):
        print("Crear un estudiante")
        nuevoEstudiante = Estudiante(elEstudiante)
        return self.repositorioEstudiante.save(nuevoEstudiante)

    def show(self, id):
        elEstudiante = Estudiante(self.repositorioEstudiante.findById(id))
        return elEstudiante.__dict__

    def update(self, id, infoEstudiante):
        print("Actualizando estudiante con id ", id)
        estudianteActual = Estudiante(self.repositorioEstudiante.findById(id))
        estudianteActual.cedula = infoEstudiante["cedula"]
        estudianteActual.nombre = infoEstudiante["nombre"]
        estudianteActual.apellido = infoEstudiante["apellido"]
        return self.repositorioEstudiante.save(estudianteActual)

    def delete(self, id):
        print("Eliminando estudiante con id ", id)
        return self.repositorioEstudiante.delete(id)