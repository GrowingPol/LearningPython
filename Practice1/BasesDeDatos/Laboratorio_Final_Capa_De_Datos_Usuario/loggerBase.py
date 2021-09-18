import logging as log

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%Y-%m-%d %I:%M:%S %p',
                handlers= [log.FileHandler('capaDatosUsuario.log'),
                           log.StreamHandler()])