import tabula

def PdfToCsv( nombreExamen ):
    """Transforma el archivo.pdf a archivo.csv"""
    tabula.convert_into( nombreExamen + ".pdf", nombreExamen + ".csv",
                        output_format = "csv", pages = 'all' )

def formatearCsv( nombreExamen ):
    """Formatea el archivo csv"""
    #Abre el archivo y copia todas las lineas
    with open( nombreExamen + ".csv" ) as archivo:
        lines = archivo.readlines( )

    #Formatea el archivo saca espacios y puntos
    for i in range( len( lines ) ):
        while( " ," in lines[ i ] ) or ( ", " in lines[ i ] ):
            lines[ i ] = lines[ i ].replace( " ,", "," )
            lines[ i ] = lines[ i ].replace( ", ", "," )

        while( '"' in lines[ i ] ) or ( "." in lines[ i ] ):
            lines[ i ] = lines[ i ].replace( '"', "" )
            lines[ i ] = lines[ i ].replace( '.', "" )

        if lines[ i ][ -2 ] != ",":
            print( lines[ i ] )
            lines[ i ] = lines[ i ][ : -1 ]  + ",\n"
            print( lines[ i ] )

    #Escribe en el archivo los cambios
    with open( nombreExamen + ".csv", "w" ) as archivo:
        archivo.writelines( lines )
