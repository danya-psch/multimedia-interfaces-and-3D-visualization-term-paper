from services.common import Common
from states_machine.state_context import State
from states_machine.states.clean_service import CleanService


class AdditionalServices(State):

    def __init__(self):
        pass

    def income_handle(self) -> None:
        # TODO:
        #
        print(f"income_handle: AdditionalServices")

    def outcome_handle(self) -> None:
        # TODO:
        #
        print(f"outcome_handle: AdditionalServices")


        status = False
        try:
            self.text_machine.start_transaction()

            if not status:
                self.text_machine.rollback()
        except:
            print(f" AdditionalServices: exception ")
            self.text_machine.rollback()
        else:
            pass
        finally:
            if not self.text_machine.has_finished():
                self.text_machine.rollback()

        print(f" AdditionalServices wants to change the state of the context CleanService.")
        self.context.transition_to(CleanService())

