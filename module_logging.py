import logging

logger = logging.getLogger('Add_student')
logger.setLevel(logging.DEBUG)
inf = logging.StreamHandler()
inf.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
inf.setFormatter(formatter)
logger.addHandler(inf)


class LimitError(Exception):
    def __int__(self, message):
        self.message = message