from abc import ABC, abstractmethod
from functools import cmp_to_key

from app.python.managers.SortingType import SortingType
from app.python.models.Arm import Arm


class MilitaryBaseManagerUtils(ABC):

    @staticmethod
    def compare_by_equipage(arm: Arm):
        return arm.operation_crew_count

    @staticmethod
    def sort_arms_by_equipage(list_of_arms, sorting_type):
        """
        >>> arm1 = Arm()
        >>> arm2 = Arm(operation_crew_count=5)
        >>> arm3 = Arm(operation_crew_count=2)
        >>> checklist = MilitaryBaseManagerUtils.sort_arms_by_equipage([arm1, arm2, arm3], SortingType.DESCEND)
        >>> check_count = []
        >>> for arm in checklist: check_count.append(arm.operation_crew_count)
        >>> check_count
        [5, 2, 1]
        """
        rev = False
        if sorting_type == SortingType.DESCEND:
            rev = True
        return sorted(list_of_arms, key=MilitaryBaseManagerUtils.compare_by_equipage, reverse=rev)

    @staticmethod
    def sort_by_stack_count(list_of_arms, sorting_type):
        """
        >>> arm1 = Arm()
        >>> arm2 = Arm(count_in_stack=5)
        >>> arm3 = Arm(count_in_stack=2)
        >>> checklist = MilitaryBaseManagerUtils.sort_by_stack_count([arm1, arm2, arm3], SortingType.DESCEND)
        >>> check_count = []
        >>> for arm in checklist: check_count.append(arm.count_in_stack)
        >>> check_count
        [5, 2, 1]
        """
        rev = False
        if sorting_type == SortingType.DESCEND:
            rev = True
        return sorted(list_of_arms, key=MilitaryBaseManagerUtils.compare_by_stack_count, reverse=rev)

    @staticmethod
    def compare_by_stack_count(arm: Arm):
        return arm.count_in_stack

