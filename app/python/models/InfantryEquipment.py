from app.python.models.Arm import Arm


class InfantryEquipment(Arm):

    def __init__(self, calibre, cartridge_capacity, mass_in_kg, serial_number="AA11", country_of_origin="Ukraine", count_in_stack=1, operation_crew_count=1):
        super().__init__(serial_number, country_of_origin, count_in_stack, operation_crew_count)
