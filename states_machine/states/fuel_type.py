from orders.fuel_types.diesel_order import DieselOrder
from orders.fuel_types.gas_order import GasOrder
from orders.fuel_types.petrol_order import PetrolOrder
from services.common import Common
from states_machine.state_context import State
from states_machine.states.additional_services import AdditionalServices


class FuelType(State):
    def __init__(self):
        pass

    def income_handle(self) -> None:
        # TODO:
        #
        print(f"income_handle: FuelType")

    def outcome_handle(self) -> None:
        print(f"outcome_handle: FuelType")

        status = False
        try:
            self.text_machine.start_transaction()
            # дизельне пальне
            # газу
            # дизель плюс
            # 95 плюс
            # 100
            word = self.text_machine.move()
            if word in DieselOrder.main_words:
                if self.text_machine.get_next() in DieselOrder.additional_words:
                    # TODO: Add to state machine info!!!

                    self.text_machine.move()
                    print("*" * 10 + " FuelType " + "*" * 10)
                    print(self.text_machine.get_current())
                    print("*" * 10 + " FuelType " + "*" * 10)
                    self.text_machine.commit()
                    status = True
                else:
                    # TODO: Add to state machine info!!!
                    print("*" * 10 + " FuelType " + "*" * 10)
                    print(self.text_machine.get_current())
                    print("*" * 10 + " FuelType " + "*" * 10)
                    self.text_machine.commit()
                    status = True
            elif word in PetrolOrder.main_words:
                if self.text_machine.get_next() in PetrolOrder.additional_words:
                    # TODO: Add to state machine info!!!
                    self.text_machine.move()
                    print("*" * 10 + " FuelType " + "*" * 10)
                    print(self.text_machine.get_current())
                    print("*" * 10 + " FuelType " + "*" * 10)
                    self.text_machine.commit()
                    status = True
                else:
                    print("*" * 10 + " FuelType " + "*" * 10)
                    print(self.text_machine.get_current())
                    print("*" * 10 + " FuelType " + "*" * 10)
                    self.text_machine.commit()
                    status = True
            elif word in GasOrder.main_words:
                # TODO: Add to state machine info!!!
                print("*" * 10 + " FuelType " + "*" * 10)
                print(self.text_machine.get_current())
                print("*" * 10 + " FuelType " + "*" * 10)
                self.text_machine.commit()
                status = True

            if not status:
                self.text_machine.rollback()

        except:
            print(f" FuelType: exception ")
            self.text_machine.rollback()
        else:
            pass
        finally:
            if not self.text_machine.has_finished():
                self.text_machine.rollback()

        print(f" FuelType wants to change the state of the context AdditionalServices.")
        self.context.transition_to(AdditionalServices())

