import logging
import logging.handlers

#Available log levels:
     #logger.debug('debug message') console only.
     #logger.info('info message') console and file.
     #logger.warning('warn message') console and file.
     #logger.error('error message') console and file.
     #logger.critical('critical message') console and file.

#Instantiate a logger
def getLogger(scriptname):
     logger = logging.getLogger(scriptname)
     logger.setLevel(logging.DEBUG)

     fh = logging.handlers.RotatingFileHandler(scriptname + ".log", maxBytes=10485760, backupCount=10)
     fh.setLevel(logging.INFO)

     ch = logging.StreamHandler()
     ch.setLevel(logging.DEBUG)

     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
     ch.setFormatter(formatter)
     fh.setFormatter(formatter)

     logger.addHandler(ch)
     logger.addHandler(fh)

     return logger