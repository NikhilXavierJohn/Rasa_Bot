import logging
import pprint
# from rasa_nlu.training_data import training_data
# from rasa_nlu import config
from rasa.nlu import config
from rasa.nlu.training_data import load_data
from rasa.nlu.model import Trainer
from rasa.nlu.model import Interpreter
from rasa.nlu.test import run_evaluation

logfile='nlu_model.log'

def train_nlu(data_path, configs, model_path):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    training_data=load_data(data_path)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory= trainer.persist(model_path,fixed_model_name='nlu')
    run_evaluation(data_path,model_directory)
def run_nlu(nlu_path):
    logging.basicConfig(filename=logfile,level=logging.DEBUG)
    interpreter = Interpreter.load(nlu_path)
    pprint.pprint(interpreter.parse("Book me a hotel in Hoodi"))
    pprint.pprint(interpreter.parse("Find me a hotel in bangalore for 5 people"))

if __name__=="__main__":
    train_nlu('./data/nlu.md','config.yml','./models')
    run_nlu('./models/nlu/')