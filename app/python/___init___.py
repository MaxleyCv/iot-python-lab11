from app.python.managers.MilitaryBaseManager import MilitaryBaseManager
from app.python.managers.MilitaryBaseManagerUtils import MilitaryBaseManagerUtils
from app.python.managers.SortingType import SortingType
from app.python.models.Arm import Arm
from app.python.models.SpyEquipment import SpyEquipment

spy_arm1 = SpyEquipment(serial_number="AA", max_detection_distance_in_meters=2)
spy_arm2 = SpyEquipment(serial_number="BB", max_detection_distance_in_meters=4)
spy_arm3 = SpyEquipment(serial_number="CC", max_detection_distance_in_meters=6)
arm1 = Arm(serial_number="DD")
manager = MilitaryBaseManager([spy_arm1, spy_arm2, spy_arm3, arm1])
print(isinstance(spy_arm1, SpyEquipment))
print(manager.find_spy_equipment_by_min_detection_range(3))