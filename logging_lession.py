import logging

logging.basicConfig(filename="my_app.log", 
                    filemode="a", 
                    format="%(asctime)s %(name)s %(levelname)s '%(message)s'", 
                    datefmt="%d - %B - %Y, %H:%M:%S")

my_logger = logging.getLogger("Racim")

my_logger.critical("by")
