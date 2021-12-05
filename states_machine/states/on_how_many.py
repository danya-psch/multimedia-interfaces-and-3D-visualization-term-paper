from data.on_how_many_data import OnHowManyData
from services.common import Common
from states_machine.state_context import State
from states_machine.states.fuel_type import FuelType


class OnHowMany(State):

    def __init__(self):
        pass

    def income_handle(self) -> None:
        # TODO:
        #
        print(f"income_handle: OnHowMany")

    def outcome_handle(self) -> None:
        print(f"outcome_handle: OnHowMany")

        result = None
        status = False
        try:
            self.text_machine.start_transaction()
            # на 20 л(ітрів)
            # на 20
            if self.text_machine.get_next() in OnHowManyData.additional_words:
                self.text_machine.move()
                if self.text_machine.get_next().isnumeric():
                    word = self.text_machine.move()
                    if self.text_machine.get_next() in OnHowManyData.main_words:
                        # TODO: Add to state machine info!!!
                        result = word
                        self.text_machine.move()
                        print("*" * 10 + " OnHowMany " + "*" * 10)
                        print(self.text_machine.get_current())
                        print("*" * 10 + " OnHowMany " + "*" * 10)
                        self.text_machine.commit()
                        status = True
                        # на 20
                    elif float(self.text_machine.get_current()) < 100:
                        result = self.text_machine.get_current()
                        print("*" * 10 + " OnHowMany " + "*" * 10)
                        print(self.text_machine.get_current())
                        print("*" * 10 + " OnHowMany " + "*" * 10)
                        self.text_machine.commit()
                        status = True
            # 20л(ітрів)
            elif len([currentWord
                      for
                      currentWord
                      in
                      OnHowManyData.main_words
                      if currentWord in self.text_machine.get_next() and
                         Common.has_numbers(self.text_machine.get_next())]) > 0:

                result = int(''.join(s for s in self.text_machine.get_next() if s.isdigit()))

                print("*" * 10 + " OnHowMany " + "*" * 10)
                print(self.text_machine.get_current())
                print("*" * 10 + " OnHowMany " + "*" * 10)
                self.text_machine.commit()
                status = True

            if not status:
                self.text_machine.rollback()

        except:
            print(f" OnHowMany: exception ")
            self.text_machine.rollback()
        else:
            pass
        finally:
            if not self.text_machine.has_finished():
                self.text_machine.rollback()

        print(f" OnHowMany wants to change the state of the context FuelType.")
        if result is not None:
            self.context.add_result(0, 2)
            self.context.add_result(result, 3)
        self.context.transition_to(FuelType())
