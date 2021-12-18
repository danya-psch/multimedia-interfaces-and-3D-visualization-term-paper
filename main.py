import time

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

import time
import socketio

sio = socketio.Client(logger=True, engineio_logger=True)
start_timer = None


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

    send_to_eu4(context.serialize_result())
     # working_server.server.message_bus(context.serialize_result())
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
        text = recognizer.recognize_google(audio, language="uk-UA")
        print("*"*10)
        print(text)
        print("*" * 10)
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


def send_to_eu4(data):
    print('send_to_eu4 = ', data)
    sio.emit('message_bus', data)

def send_ping():
    global start_timer
    start_timer = time.time()
    sio.emit('message_bus')
    #    time.sleep(2)

@sio.event
def connect():
    print('connected to server')
    #send_ping()


@sio.event
def pong_from_server():
    global start_timer
    latency = time.time() - start_timer
    print('latency is {0:.2f} ms'.format(latency * 1000))
    sio.sleep(1)
    if sio.connected:
        send_ping()


if __name__ == '__main__':
    sio.connect('http://localhost:5000')
    while True:
        sio.emit('message_bus', '5|1|1|1')
        time.sleep(2)
    #main()
    sio.wait()




