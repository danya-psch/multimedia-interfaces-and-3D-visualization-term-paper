import speech_recognition as sr
import os
from pydub.silence import split_on_silence
from pydub import AudioSegment
import threading
from word2number import w2n

import working_server.server
# from communication_module import com_module

# cm = com_module(f"g:\\Projects\\UnrealEngine_project\\MI_\\MI\\Config\\MyConfig.txt")

from states_machine.state_context import StateContext
from states_machine.states.station_number import StationNumber
from text_machine.text_machine import TextMachine


class state:
    AWAITING_GREETINGS = 0
    AWAITING_ORDER = 1

class word_types:
    NUMBER = 0
    AWAITING_ORDER = 1

class global_ctxt:
    curr_state = state.AWAITING_GREETINGS
    words = []
    curr_word = 0

ctxt = global_ctxt()

greetings_strings = ["вітаю", "привіт"]
def awaiting_greetings_handler(text):
    if text in greetings_strings:
        ctxt.curr_state = state.AWAITING_ORDER
        print("ctxt.curr_state = state.AWAITING_ORDER")

# static Tree *accept(Parser *parser, TokenType type) {
# 	if (eoi(parser)) return nullptr;
# 	Token lexem = parser->get_iterator_value();

# 	if (lexem.get_type() == type) {

# 		AstNodeType astType = tokenType_to_astType(type);

# 		AstNode *node = new AstNode(astType, lexem.get_buffer());
# 		Tree *tree = new Tree(node);
# 		parser->increase_iterator();
# 		return tree;
# 	}
# 	return nullptr;
# }

number_strings = ["перша", "друга", "третя", "четверта", "п'ята", "шоста", "друга", "друга", "друга", "друга", "друга"]
def number_handler(word):
    return word if word in number_strings else None

type_handlers = {
    str(word_types.NUMBER): number_handler,
    # "fuel_type": fuel_type,
    # "on_which_sum": on_which_sum,
    # "on_how_many": on_how_many,
    # "additional_services": additional_services
}

def accept(word_type):
    res = type_handlers[str(word_type)](ctxt.words[ctxt.curr_word])
    return True if res is not None else False

def station_number(text):
    pass

def fuel_type(text):
    pass

def on_which_sum(text):
    pass

def on_how_many(text):
    pass

def additional_services(text):
    pass

def awaiting_order_handler(text):

    context = StateContext(StationNumber(), TextMachine(text))

    for i in range(0, 11): # while
        context.outcome_request()

    # Data Transfer Begin
    print("awaiting_order_handler")
    working_server.server.message_bus(context.serialize_result())
     #.message_bus(context.serialize_result())
    #cm.transfer_data(context.serialize_result())
    print(f'awaiting_order_handler {len(text)}')

    # Data Transfer End
    text[2:]

state_handlers = {
    str(state.AWAITING_GREETINGS): awaiting_greetings_handler,
    str(state.AWAITING_ORDER): awaiting_order_handler,
}


def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language="uk-UA", show_all=True)
        print(text)
        print(ctxt.curr_state)
        ctxt.words = text.split()
        ctxt.curr_word = 0
        state_handlers[str(ctxt.curr_state)](text)
    except Exception as e:
        return 10*"#" + " None " + 10*"#" + " "


def main():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
    stop_listening = r.listen_in_background(mic, callback)
    while True:
        pass


if __name__ == "__main__":
    #main()
    working_server.server.message_bus("Hello WORKDasd!")
