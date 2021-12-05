from data.on_which_sum_data import OnWhichSumData
from services.common import Common
from states_machine.state_context import State
from states_machine.states.on_how_many import OnHowMany


class OnWhichSum(State):

    def __init__(self):
        pass

    def income_handle(self) -> None:
        # TODO:
        #
        print(f"income_handle: OnWhichSum")

    def outcome_handle(self) -> None:
        print(f"outcome_handle: OnWhichSum")

        result = None
        status = False
        try:
            self.text_machine.start_transaction()
            word = self.text_machine.move()
            # на 150 гривень
            # на 150
            if word in OnWhichSumData.additional_words:
                word = self.text_machine.move()
                if word.isnumeric():
                    if self.text_machine.get_next() in OnWhichSumData.main_words:

                        result = word
                        self.text_machine.move()
                        print("*" * 10 + " OnWhichSum " + "*" * 10)
                        print(self.text_machine.get_current())
                        print("*" * 10 + " OnWhichSum " + "*" * 10)

                        self.text_machine.commit()
                        status = True
                    # на >= 100 - будуть гривні
                    # менше 100 - будуть літри
                    elif float(word) >= 100:
                        result = word
                        print("*" * 10 + " OnWhichSum " + "*" * 10)
                        print(self.text_machine.get_current())
                        print("*" * 10 + " OnWhichSum " + "*" * 10)
                        self.text_machine.commit()
                        status = True
            # 150грн
            elif len([currentWord
                                for
                                    currentWord
                                in
                                    OnWhichSumData.main_words
                                if  currentWord in word and Common.has_numbers(word)]) > 0:

                result = int(''.join(s for s in word if s.isdigit()))
                print("*" * 10 + " OnWhichSum " + "*" * 10)
                print(word)
                print("*" * 10 + " OnWhichSum " + "*" * 10)

                self.text_machine.commit()
                status = True

            if not status:
                self.text_machine.rollback()

        except:
            print(f" OnWhichSum: exception ")
            self.text_machine.rollback()
        else:
            pass
        finally:
            if not self.text_machine.has_finished():
                self.text_machine.rollback()
        print(f" OnWhichSum wants to change the state of the context OnHowMany.")
        if result is not None:
            self.context.add_result(1, 2)
            self.context.add_result(result, 3)
        self.context.transition_to(OnHowMany())
