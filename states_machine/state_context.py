from __future__ import annotations
from abc import ABC, abstractmethod

from message_bus.request_message import RequestMessage
from text_machine.text_machine import TextMachine


class State(ABC):

    @property
    def text_machine(self) -> TextMachine:
        return self._text_machine

    @property
    def context(self) -> StateContext:
        return self._context

    @text_machine.setter
    def text_machine(self, text_machine: TextMachine) -> None:
        self._text_machine = text_machine

    @context.setter
    def context(self, context: StateContext) -> None:
        self._context = context

    @abstractmethod
    def income_handle(self) -> None:
        pass

    @abstractmethod
    def outcome_handle(self) -> None:
        pass


class StateContext:
    _state = None

    def __init__(self, state: State, text_machine: TextMachine) -> None:
        """

        :rtype: object
        """
        self.request_message = RequestMessage()
        self._text_machine = text_machine
        self.transition_to(state)

    def serialize_result(self):
        return self.request_message.serialize()

    def add_result(self, result, position):
        self.request_message.add(result, position)

    def transition_to(self, state: State):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.text_machine = self._text_machine
        self._state.context = self

    def income_request(self):
        self._state.income_handle()

    def outcome_request(self):
        self._state.outcome_handle()