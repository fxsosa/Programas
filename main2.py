import Cursillo
import Convertidor

def leerArchivo( listaAlumnos ):
    """Lee el nombre del archivo para identificar el examen"""

    cadena = input( "Ingrese nombre del archivo( sin la extension .pdf ): " )
    etapa = identificaEtapa( cadena )
    examen = identificaExamen( cadena, etapa )

    Convertidor.PdfToCsv( cadena )
    guardarDatos( cadena, listaAlumnos, examen )

def guardarDatos( cadena, listaAlumnos, examen ):
    cursillo = { "I" : "Intensivo", "E" : "Extensivo" }
    with open( cadena + ".csv" ) as archivo:
        for line in archivo:
            datos = line.split( "," )
            alumno = Cursillo.Alumno( datos[ 0 ], datos[ 1 ], datos[ 2 ],
                                     cursillo[ cadena[ 5 ] ] )
            alumno.cargarNota( examen, int( datos[ 3 ] ) )
            print( alumno )
            if alumno not in listaAlumnos:
                listaAlumnos.append( alumno )
            else:
                listaAlumnos[ listaAlumnos.index( alumno ) ].cargarNota(
                    examen, int( datos[ 3 ] ) )

def identificaEtapa( examen ):
    """Identifica el tipo de etapa"""
    etapaD = { "Par" : "Parcial", "Fin" : "Final" }

    return Cursillo.Etapa( etapaD[ examen[ : 3 ] ], int( examen[ 3 ] ) )

def identificaExamen( examen, etapa ):
    materiasD = { "A" : "Anatomia", "B" : "Biologia", "C" : "Comprension", "M" :
                 "Matematica", "Q" : "Quimica" }

    return Cursillo.Examen( etapa, materiasD[ examen[ 4 ] ] )

listaAlumnos = [ ]
leerArchivo( listaAlumnos )
