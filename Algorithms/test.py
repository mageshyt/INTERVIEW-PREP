def solution(image, radius):
    rows = len(image)
    cols = len(image[0])
    
    def get_neighbors(i, j, radius):
        neighbors = []
        for k in range(max(0, i - radius), min(rows, i + radius + 1)):
            for l in range(max(0, j - radius), min(cols, j + radius + 1)):
                if (k, l) != (i, j):  # exclude the pixel itself
                    neighbors.append(image[k][l])
        return neighbors

    def calculate_new_intensity(i, j):
        neighbors = get_neighbors(i, j, radius)
        if neighbors:
            mean_neighbors = sum(neighbors) // len(neighbors)
            return (image[i][j] + mean_neighbors) // 2
        else:
            return image[i][j]

    # Create a new image with updated intensities
    new_image = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            new_image[i][j] = calculate_new_intensity(i, j)
    
    return new_image
# Example usage
image = [[9, 6], [3, 0]]
radius = 1
blurred_image = solution(image, radius)
print(blurred_image)
