def bfs(entity, grid):
    if entity.position == entity.target.position:
        return (0, 0)
    queue = []
    visited = {tuple(entity.position)}
    cardinal_directions = [
        (0, -1), 
        (0, 1),   
        (-1, 0),  
        (1, 0)   
    ]
    for move in cardinal_directions:
        validity, newpos = grid.checkifvalidmove(entity.position, move)
        if validity:
            tuple_pos = tuple(newpos)
            if tuple_pos not in visited:
                visited.add(tuple_pos)
                queue.append((newpos, move))
    while queue:
        current_pos, first_step = queue.pop(0)
        if current_pos == entity.target.position:
            return first_step
            
        for move in cardinal_directions:
            validity, next_pos = grid.checkifvalidmove(current_pos, move)
            if validity:
                tuple_next = tuple(next_pos)
                if tuple_next not in visited:
                    visited.add(tuple_next)
                    queue.append((next_pos, first_step))
    return (0,0)