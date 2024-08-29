from typing import List


class MergeTripletsToFormTargetTriplet:
    @staticmethod
    def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:
        valid_indices = []
        for i in range(len(triplets)):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                valid_indices.append(i)

        is_x_present, is_y_present, is_z_present = False, False, False
        for index in valid_indices:
            if not is_x_present and triplets[index][0] == target[0]:
                is_x_present = True
            if not is_y_present and triplets[index][1] == target[1]:
                is_y_present = True
            if not is_z_present and triplets[index][2] == target[2]:
                is_z_present = True

        return is_x_present and is_y_present and is_z_present
