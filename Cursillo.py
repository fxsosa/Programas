materias = { "A" : 0, "B" : 1, "C" : 2, "M" : 3, "Q" : 4 }
numeroMaterias = len( materias )
examenes = { "Par1": 0, "Par2": 1, "Par3": 2, "Fin": 3 }
numeroParciales = 3
numeroFinales = 1

class Alumno:

    def __init__( self, CI, apellido, nombre, cursillo ):

        global numeroMaterias
        global numeroParciales
        global numeroFinales
        self.CI = CI
        self.nombre = nombre
        self.apellido = apellido
        self.notas = [ [ 0 ] * 6 ] * 5
        self.cursillo = cursillo
        self.puntajeTotal = 0

    def cargarNota( self, nota, examen, materia ):
        self.notas[ examen ][ materia ] = nota
        self.notas[ examen ][ -1 ] += nota
        self.puntajeTotal += nota

    def comparar( self, other, fila, columna ):
        return self.notas[ fila ][ columna ] > other.notas[ fila ][ columna ]

    def __eq__( self, other ):
        return ( self.CI == other.CI )
    def __str__( self, other ):
        return f"{self.nombre}, {self.notas}"

