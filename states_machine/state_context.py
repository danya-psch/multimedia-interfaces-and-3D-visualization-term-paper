from __future__ import annotations
from abc import ABC, abstractmethod

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
        self._text_machine = text_machine
        self.transition_to(state)

    def transition_to(self, state: State):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.text_machine = self._text_machine
        self._state.context = self

    def income_request(self):
        self._state.income_handle()

    def outcome_request(self):
        self._state.outcome_handle()