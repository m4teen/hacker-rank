def countingValleys(steps, path):
    heights = [0]
    path = list(path)
    height = 0
    for i in range(len(path)):
        if path[i] == 'D':
            height -= 1
        elif path[i] == 'U':
            height += 1
        heights.append(height)
    valleys = 0
    for j in range(len(heights)-1):
        if heights[j] == 0 and heights[j+1] == -1:
            valleys += 1
    return valleys
    
        