from data.additional_services_data import AdditionalServicesData
from data.on_how_many_data import OnHowManyData
from data.on_which_sum_data import OnWhichSumData
from data.station_number_data import StationNumberData
from orders.fuel_types.diesel_order import DieselOrder
from orders.fuel_types.gas_order import GasOrder
from orders.fuel_types.petrol_order import PetrolOrder
from states_machine.state_context import State


class CleanService(State):
    def __init__(self):
        pass

    def income_handle(self) -> None:
        # TODO:
        #
        print(f"income_handle: CleanService")

    def outcome_handle(self) -> None:
        # TODO:
        #
        print(f"outcome_handle: CleanService")

        status = False
        try:
            self.text_machine.start_transaction()
            # if no one contains this word - SKIP
            if self.text_machine.get_next() in (StationNumberData.main_words + StationNumberData.number_nums
                                                + StationNumberData.number_words):
                status = True
            elif self.text_machine.get_next() in (OnWhichSumData.main_words + OnWhichSumData.additional_words):
                status = True
            elif self.text_machine.get_next() in (OnHowManyData.main_words + OnHowManyData.additional_words):
                status = True
            elif self.text_machine.get_next() in AdditionalServicesData.main_words:
                status = True
            elif self.text_machine.get_next() in (DieselOrder.main_words + DieselOrder.additional_words):
                status = True
            elif self.text_machine.get_next() in (PetrolOrder.main_words + PetrolOrder.additional_words):
                status = True
            elif self.text_machine.get_next() in GasOrder.main_words:
                status = True
            else:
                # SKIP
                self.text_machine.move()
                self.text_machine.commit()

                self.log_warning_word()
            # notify logger with this word

            if not status:
                self.text_machine.rollback()
        except:
            print(f" {type(CleanService)}: exception ")
            self.text_machine.rollback()
        else:
            pass
        finally:
            if not self.text_machine.has_finished():
                self.text_machine.rollback()

        print(f" CleanService wants to change the state of the context StationNumber.")
        from states_machine.states.station_number import StationNumber
        self.context.transition_to(StationNumber())

    def log_warning_word(self):
        print("#" * 25 + " WARNING BEGIN " + "#" * 25)
        print(self.text_machine.get_current())
        with open("problem_words.txt", "a") as file:
            file.write(self.text_machine.get_current() + "\n")
        print("#" * 25 + " WARNING END " + "#" * 25)

