from data.station_number_data import StationNumberData
from states_machine.state_context import State
from states_machine.states.on_which_sum import OnWhichSum


class StationNumber(State):

    def __init__(self):
        pass

    def income_handle(self) -> None:
        # TODO:
        #
        print(f"income_handle: StationNumber")

    def outcome_handle(self) -> None:
        result = None
        print(f"outcome_handle: StationNumber")
        try:
            self.text_machine.start_transaction()
            word = self.text_machine.move()
            if word in (StationNumberData.number_words + StationNumberData.number_nums):
                if self.text_machine.move() in StationNumberData.main_words:
                    # TODO: Add to state machine info!!!

                    print("*"*10 + " StationNumber " + "*"*10)
                    print(self.text_machine.get_current())
                    if word.isnumeric():
                        result = word
                    else:
                        for i in range(0, len(StationNumberData.number_words)):
                            if word == StationNumberData.number_words[i]:
                                result = i + 1
                                break
                    print("*" * 10 + " StationNumber " + "*" * 10)
                    self.text_machine.commit()
                else:
                    self.text_machine.rollback()
            else:
                self.text_machine.rollback()
        except:
            print(f" StationNumber: exception ")
            self.text_machine.rollback()
        else:
            pass
        finally:
            if not self.text_machine.has_finished():
                self.text_machine.rollback()

        print(f" StationNumber wants to change the state of the context OnWhichSum.")
        if result is not None:
            self.context.add_result(result, 0)
        self.context.transition_to(OnWhichSum())