class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        points.sort(key=lambda interval: interval[1])

        arrows = 1
        current_end = points[0][1]

        for xstart, xend in points[1:]:
            if xstart > current_end:
                arrows += 1
                current_end = xend

        return arrows
