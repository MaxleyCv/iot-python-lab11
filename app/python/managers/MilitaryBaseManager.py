from app.python.models.Arm import Arm
from app.python.models.SpyEquipment import SpyEquipment


class MilitaryBaseManager:
    def __init__(self, list_of_arms):
        self.list_of_arms = list_of_arms

    def find_spy_equipment_by_min_detection_range(self, detect_range):
        """
        >>> spy_arm1 = SpyEquipment(serial_number="AA", max_detection_distance_in_meters=2)
        >>> spy_arm2 = SpyEquipment(serial_number="BB", max_detection_distance_in_meters=4)
        >>> spy_arm3 = SpyEquipment(serial_number="CC", max_detection_distance_in_meters=6)
        >>> arm1 = Arm(serial_number="DD")
        >>> manager = MilitaryBaseManager([spy_arm1, spy_arm2, spy_arm3, arm1])
        >>> manager.find_spy_equipment_by_min_detection_range(3)
        [BB, CC]
        """
        result = []
        for arm in self.list_of_arms:
            if isinstance(arm, SpyEquipment):
                if arm.max_detection_distance_in_meters > detect_range:
                    result.append(arm)
        return result
