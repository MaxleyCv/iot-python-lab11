from application.models.Arm import Arm
from application.models.Engine import Engine


class Vehicle(Arm):
    def __init__(self, engine=Engine(), model="Honda", max_velocity_in_kmh=10, serial_number="AA11", country_of_origin="Ukraine", count_in_stack=1, operation_crew_count=1):
        super().__init__(serial_number, country_of_origin, count_in_stack, operation_crew_count)
        self.max_velocity_in_kmh = max_velocity_in_kmh
        self.model = model
        self.engine = engine
