from app.python.models.Arm import Arm


class SpyEquipment(Arm):

    def __init__(self, serial_number="AA11", country_of_origin="Ukraine", count_in_stack=1, operation_crew_count=1, max_detection_distance_in_meters=10, size_in_centimeters=None):
        super().__init__(serial_number, country_of_origin, count_in_stack, operation_crew_count)
        self.max_detection_distance_in_meters = max_detection_distance_in_meters
        self.size_in_centimeters = size_in_centimeters

    def get_surrounding_objects(self):
        print("Everything is safe")
