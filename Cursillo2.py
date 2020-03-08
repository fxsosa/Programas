class Etapa:
    """Clase que contendra los detalles de la etapa"""

    def __init__( self, tipoEtapa, numeroEtapa ):
        """Guarda el tip ( parcial, final ), y el numero ( 1, 2, 3 )"""
        self.tipoEtapa = tipoEtapa
        self.numeroEtapa = numeroEtapa

    def __eq__( self, other ):
        """Comparar 2 etapas, si tienen los mismos valores retorna true, sino
        false"""
        return ( self.tipoEtapa == other.tipoEtapa and self.numeroEtapa ==
                other.numeroEtapa )

    def __str__( self ):
        """Para imprimir el objeto"""
        return ( f"Etapa = {self.tipoEtapa}, {self.numeroEtapa}" )

class Examen:
    """Clase de examen, tiene los datos del examen"""

    def __init__( self, etapa, materia ):
        """Inicializa la etapa y la materia"""
        self.etapa = etapa
        self.

    def __eq__( self, other ):
        """Comparar 2 examenes, si tienen los mismos valores retorna true, sino
        false"""
        return self.etapa( self.etapa, other.etapa )

    def __str__( self ):
        """Para imprimir el objeto"""
        return ( f"<Examen de {self.materia}, {self.etapa}>" )

    def __repr__(self):
        """Para imprimir como subdato"""
        return self.__str__( )

    def __hash__( self ):
        """Para asignar el objeto a tipos de datos mutables"""
        return hash( str( self ) )

class Persona:
    """Clase persona, contiene los datos basicos ( nombre, apellido, CI )"""

    def __init__( self, CI, nombre, apellido ):
        """Inicializa los datos de la persona"""
        self.nombre = nombre
        self.apellido = apellido
        self.CI = CI

    def __eq__( self, other ):
        """Compara si dos personas son la misma"""
        return ( self.CI == other.CI )

    def __str__( self ):
        """Convertir en cadena el objeto"""
        return ( f"Nombre = {self.nombre}\nApellido = {self.apellido}\nCedula = {self.CI}" )

class Alumno( Persona ):
    """Clase alumno contiene los datos del alumno"""

    def __init__( self, nombre, apellido, CI, cursillo ):
        """Inicializa los datos del alumno"""
        self.cursillo = cursillo
        super( ).__init__( nombre, apellido, CI )
        self.notas = { }

    def cargarNota( self, examen, nota ):
        """Se cargan las notes del examen"""
        self.notas[ examen ] = nota

    def __eq__( self, other ):
        """Para comparar con otros examenes"""
        return super.__eq__( self, other )

    def __str__( self ):
        """transforma a cadena"""
        return ( f"{super( ).__str__( )}\nNota:\n{self.notas}" )
