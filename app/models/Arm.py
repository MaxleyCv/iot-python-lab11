class Arm:

    def __repr__(self):
        return self.serial_number

    def __init__(self, serial_number="AA11", country_of_origin="Ukraine", count_in_stack=1, operation_crew_count=1):
        self._count_in_stack = count_in_stack
        self._serial_number = serial_number
        self._country_of_origin = country_of_origin
        self._operation_crew_count = operation_crew_count


class BaseInfo:
    def __repr__(self):
        return {
            "soldiers": self.soldiers,
            "trucks": self.trucks,
            "roads": self.roads,
            "rain": self.rain
        }

    def __init__(self, soldiers=0, trucks=2, roads=0, rain=0):
        self.soldiers = soldiers
        self.trucks = trucks
        self.roads = roads
        self.rain = rain