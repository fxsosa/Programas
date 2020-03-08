class Alumno:
    """Clase alumno tendra los datos del alumno"""

    def __init__( self, cedula, apellido, nombre, cursillo ):
        """Inicializa el alumno con los datos dados"""
        self.cedula = int( cedula )
        self.apellido = apellido
        self.nombre = nombre
        self.cursillo = cursillo
        self.eliminado = False
        #el 6 es de las materias + uno de total y el 5 de la cantidad de examenes
        self.notas = [ ]
        for i in range( 5 ):
            self.notas.append( [ 0, 0, 0, 0, 0, 0 ] )
        self.nota_total = 0

    def cargar_nota( self, examen, materia, nota ):
        """Lee las notas ingresadas"""
        try:
            nota = int( nota )

            if examen > 3:
                if 2 * nota < 35:
                    self.eliminado = True

            self.notas[ examen ][ materia ] = nota 
            self.notas[ examen ][ -1 ] += nota
            self.nota_total += nota

        except ValueError:
            print( self.apellido )

    def __str__( self ):
        """Retorna una cadena del objeto"""
        return ( f"{self.cursillo},{self.apellido},{self.nombre},{self.nota_total}" )

    def __repr__( self ):
        return self.__str__( )

    def __eq__( self, other ):
        """Para comparar 2 objetos"""
        return self.cedula == other.cedula 

