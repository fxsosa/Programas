import Cursillo
import Convertidor

materias = { "A" : 0, "B" : 1, "C" : 2, "M" : 3, "Q" : 4 }
examenes = { "Par1": 0, "Par2": 1, "Par3": 2, "Fin": 3 }
cursillos = { "I": "Intensivo", "E": "Extensivo" }
#Par2C1.csv
#CI apellido nombre puntaje

def guardarDatos( listaAlumnos, cadena, examen, materia, cursillo ):
    with open( cadena + ".csv" ) as archivo:
        for line in archivo:
            datos = line.split( "," )
            alumno = Cursillo.Alumno( int( datos[ 0 ] ), datos[ 1 ], datos[ 2 ], cursillo  ) 
            alumno.cargarNota( int( datos[ 3 ] ), examen, materia, cursillo )
            print( Alumno )

def leerArchivo( listaAlumnos ):
    """Lee el nombre del archivo para identificar el examen"""

    cadena = input( "Ingrese nombre del archivo( sin la extension .pdf ): " )
    examen = examenes[ cadena[ : 4 ] ]
    materia = materias[ cadena[ 4 ] ]
    cursillo = cursillos[ cadena[ 5 ] ]

    Convertidor.PdfToCsv( cadena )

    guardarDatos( listaAlumnos, cadena, examen, materia, cursillo )

listaAlumnos = [ ]
leerArchivo( listaAlumnos )
