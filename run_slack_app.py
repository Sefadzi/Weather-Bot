from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('input slack app token', 
	'input slack bot token'
	'slack verification token'
	debug_mode = True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))


