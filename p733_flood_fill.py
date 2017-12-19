class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        old_color = image[sr][sc]
        frontier = [(sr, sc)]
        while frontier:
            r, c = frontier.pop()
            image[r][c] = newColor
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < len(image) and 0 <= nc < len(image[0])
                        and image[nr][nc] == old_color
                        and image[nr][nc] != newColor):
                    frontier.append((nr, nc))
        return image


def main():
    sol = Solution().floodFill
    print(sol([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
    print(sol([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 1))


if __name__ == '__main__':
    main()
