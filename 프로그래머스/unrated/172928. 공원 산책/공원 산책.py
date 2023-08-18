def solution(park, routes):
    
    answer = []
           
    
    go = {
        'N':[-1,0],
        'S':[1,0],
        'E':[0,1],
        'W':[0,-1]
    }
        
    
    position = getStartPosition(park)
    for route in routes:
        direction,step_cnt = route.split(' ')
        print(f'direction,step_cnt : {direction} {step_cnt}')
        step_cnt = int(step_cnt)
        
        move_to = go.get(direction)
        position = move(park, position, move_to, step_cnt)
    
    #direct = go.get('S')
    #position = move(park, position, direct, 2)
    
    #direct = go.get('W')
    #position = move(park, position, direct, 1)
    
    
    print(position)
        
    return position

def move(park:list, location:list, direction:list, step_cnt:int):
    
    print('============ move ACTIVATED ============')
    
    print(f'GIVEN POSITION : {location}')
    
    position = [] 
    
    # if it is movable, return cordinates after move
    # or return where you are
    
    # park : n X m 2 demention
    # location : current cordinates
    # direction : N S E W
    # step_cnt : number of steps to take to the given direction
    
    x,y = location
    
    for _ in range(step_cnt):
      
        step_x,step_y = direction
        
        print(f'x + step_x = {x} + {step_x}')
        x += step_x
        print(f'y + step_y = {y} + {step_y}')
        y += step_y
        # took one step by here
        
        print(f'x,y = {x},{y}')
        
        try:
            if park[x][y] != 'X' and (0 <= x < len(park)) and (0 <= y < len(park[0])):
                # when it's movable, return updated cordinate
                position = [x,y]
                print(f'MOVE SUCCESS : {position}')
            else:
                position = location
                print(f'MOVE FAIL 01 : {position}')
                break
        except:
            position = location
            print(f'MOVE FAIL 02 : {position}')
            break
            
    print('============ move DEACTIVATED ============')
    return position
    
def getStartPosition(park):
    
    print('============ getStartPosition ACTIVATED ============')
    position = []
    
    for row_index, row in enumerate(park):
        for col_index, col in enumerate(row):
            if park[row_index][col_index] == 'S':
                position.append(row_index)
                position.append(col_index)
    print(f'CURRENT CORDINATE : {position}')
    print('============ getStartPosition DEACTIVATED ============')
        
    return position
    
        