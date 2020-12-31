from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter


def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/weathernlu', RasaNLUConfig('config_spacy.json'))
	print(interpreter.parse("I am planning my holiday to Barcelona. I wonder what is the weather out there."))


if __name__ == '__main__':
	run_nlu()
