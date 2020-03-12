import Cursillo
import Convertidor
import time

materias = { "A" : 0, "B" : 1, "C" : 2, "M" : 3, "Q" : 4 }
examenes = { "Par1": 0, "Par2": 1, "Par3": 2, "Fin1": 3 }
cursillos = { "I": "Intensivo", "E": "Extensivo" }

def ingresarManualmente( listaAlumnos, cadena, examen, materia, cursillo ):
    listaAlumnos.sort( key = Apellido )
    with open( cadena[ : 5 ] + "E.csv", "w" ) as archivoE:
        with open( cadena[ : 5 ] + "I.csv", "w" ) as archivoI:
            with open( cadena + "AUX.csv", "w" ) as archivo1:
                for i in range( len( listaAlumnos ) ):
                    if listaAlumnos[ i ].eliminado == False:

                        print( listaAlumnos[ i ].apellido, listaAlumnos[ i ].nombre )
                        nota = input( "Ingrese nota: " )

                        if nota.isnumeric( ):
                            nota = int( nota )
                        else:
                            nota = 0
                            
                            if listaAlumnos[ i ].cursillo == "Extensivo":
                                archivoE.write( f"{listaAlumnos[ i ].cedula},{listaAlumnos[ i ].apellido},{listaAlumnos[ i ].nombre},{nota},\n" )
                            elif listaAlumnos[ i ].cursillo == "Intensivo":
                                archivoI.write( f"{listaAlumnos[ i ].cedula},{listaAlumnos[ i ].apellido},{listaAlumnos[ i ].nombre},{nota},\n" )
                            

                        archivo1.write( f"{listaAlumnos[ i ].cedula},{listaAlumnos[ i ].apellido},{listaAlumnos[ i ].nombre},{nota},\n" )
def eliminacion( listaAlumnos, examen, materia ):
    if examen == 3:
        for i in range( len( listaAlumnos ) ):
            if( listaAlumnos[ i ].notas[ examen ][ materia ] < 36 ):
                listaAlumnos[ i ].eliminado = True


def leerArchivo( listaAlumnos ):
    """Lee el nombre del archivo para identificar el examen"""
    for i in examenes.keys( ):
        for j in materias.keys( ):
            for f in cursillos.keys( ):
                cadena = i + j + f

                print( f"Leyendo {cadena}" )
                examen = examenes[ cadena[ : 4 ] ]
                materia = materias[ cadena[ 4 ] ]
                cursillo = cursillos[ cadena[ 5 ] ]
                try:
                    guardarDatos( listaAlumnos, cadena, examen, materia, cursillo )
                    eliminacion( listaAlumnos, examen, materia )
                except FileNotFoundError: 
                    try:
                        Convertidor.PdfToCsv( cadena )
                        guardarDatos( listaAlumnos, cadena, examen, materia, cursillo )
                        eliminacion( listaAlumnos, examen, materia )
                    except FileNotFoundError:
                        print( f"No se encontro el archivo {cadena} .csv o pdf" )
                        opcion = input( "1 para Ingresar las notas manualmente o 2 para saltar:" )
                        if opcion == "1":
                            ingresarManualmente( listaAlumnos, cadena, examen, materia, cursillo )
                            guardarDatos( listaAlumnos, cadena, examen, materia, cursillo )
                            eliminacion( listaAlumnos, examen, materia )
                        elif opcion == "q":
                            return

def nota_total( alumno ):
    return not( alumno.eliminado ),alumno.nota_total, nota_materia( alumno, 0 ), nota_materia( alumno, 4), nota_materia( alumno, 1 ), nota_materia( alumno, 2 ), nota_materia( alumno, 3 )

def nota_materia( alumno, indice ):
    total = 0
    for i in range( len( alumno.notas ) ):
        total = total + alumno.notas[ i ][ indice ]
        return total

def Apellido( alumno ):
    return alumno.apellido, alumno.nombre

def guardarDatos( listaAlumnos, cadena, examen, materia, cursillo ):
    Convertidor.formatearCsv( cadena )
    with open( cadena + ".csv" ) as archivo:
        for line in archivo:
            datos = line.split( "," )
            alumno = Cursillo.Alumno( datos[ 0 ], datos[ 1 ], datos[ 2 ], cursillo )
            if alumno in listaAlumnos:
                indiceLista = listaAlumnos.index( alumno )
                listaAlumnos[ indiceLista ].cargar_nota( examen, materia, datos[ 3 ] )
            else:
                alumno.cargar_nota( examen, materia, datos[ 3 ] )
                listaAlumnos.append( alumno )

def imprimeNota( alumno, tope ):
    notas = ""
    for i in range( tope ):
        for j in range( len( alumno.notas[ i ] ) ):
            
            notas = notas + f"{alumno.notas[ i ][ j ]},"
    return notas

listaAlumnos = [ ]
leerArchivo( listaAlumnos )
listaAlumnos.sort( key = nota_total, reverse = True )
counter = 0
tope = int( input( "Ingrese cantidad de etapas a desplegar" ) )
print(
    f"Puesto,Eliminado,Cursillo,Apellidos,Nombres,A1,B1,C1,M1,Q1,TP1,A2,B2,C2,M2,Q2,TP2,A3,B3,C3,M3,Q3,TP3,FA,FB,FC,FM,FQ,TF,Total")
for alumno in listaAlumnos:
    counter += 1
    print( f"{counter},{alumno.eliminado},{alumno.cursillo},{alumno.apellido},{alumno.nombre},{imprimeNota( alumno, tope )}{alumno.nota_total}" )
