from typing import List


class DailyTemperatures:
    @staticmethod
    def dailyTemperatures(temperatures: List[int]) -> list[int] | None:
        # Special case
        if temperatures is None or len(temperatures) == 0:
            return temperatures
        # Length of the list
        n = len(temperatures)
        # List to store the output
        answer = [0] * n
        # Stack to store the indices of elements
        stack = [-1] * n
        # Top of the stack
        top = -1
        # Process the array
        for i in range(n - 1, -1, -1):
            # Since we are moving from right to left, the next
            # greater element will be at the top of the stack
            # and we can consider it
            while top > -1 and temperatures[i] >= temperatures[stack[top]]:
                top -= 1
            # If the stack is not empty at this time, it means we have next greater
            # element represented by the top, and we can find the distance between
            # current index and top
            if top > -1:
                answer[i] = stack[top] - i
            # Insert current index
            top += 1
            stack[top] = i
        return answer
