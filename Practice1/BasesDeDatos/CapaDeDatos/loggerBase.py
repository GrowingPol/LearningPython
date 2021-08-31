import logging as log

#Handler-- mandar el mensaje a un archivo
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s', #agrega el tiempo (fecha y hora) al mensaje de log/nivel del log/archivo donde se dió el error/ numeor de linea que lanzó el error
                datefmt= '%I:%M:%S %p', #Hora:Minuto:Segundo AM/PM
                handlers=[
                    log.FileHandler('capaDatos.log'),
                    log.StreamHandler()
                ])

# se especifica desde qué nivel se quieren recibir los logs
#Si no se establece un nivel, por defecto se seleccionará WARNING

if __name__ == '__main__':
    # Esta es la jerarquía de loggings, dnde el más importante es CRITICAL
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critico')