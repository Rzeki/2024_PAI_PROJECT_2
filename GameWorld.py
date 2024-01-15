import pygame as pg
from pygame import Vector2 as Vec2
from GameObject import *
from Graph import *
import util


class GameWorld:
    def __init__(self, window : pg.surface) -> None:
        self.window = window
        self.window_w, self.window_h = window.get_size()
        
        #container of projectiles
        self.projectiles : list = []
            
        self.g = SparceGraph()
        # self.generate_nodes(self.g)
        self.world_grid : list[list] = []
        self.init_world_grid()
        self.world_grid[1][10] = [0, None]
        self.world_grid[2][10] = [0, None]
        self.world_grid[7][2] = [0, None]
        self.world_grid[6][2] = [0, None]
        self.world_grid[6][3] = [0, None]
        self.world_grid[7][3] = [0, None]
        self.world_grid[5][8] = [0, None]
        self.world_grid[5][9] = [0, None]
        self.world_grid[6][8] = [0, None]
        self.world_grid[6][9] = [0, None]
        self.flood_fill(Vec2(5,5), self.g)
        
    def update(self, dt : float) -> None :
        pass
        
    def draw(self) -> None :
        self.window.fill(pg.Color(0,0,0)) # BACKGROUND
        self.draw_grid()
        self.draw_graph(self.g)
        
        
    def draw_graph(self, graph : SparceGraph) :
        for edges in graph.edge_list_vector:
            for edge in edges:
                node = graph.node_vector[edge.from_node].position
                node_2 = graph.node_vector[edge.to_node].position
                pg.draw.line(self.window, pg.Color(0, 50, 0), node, node_2, 2)
        for node in graph.node_vector:
            pg.draw.circle(self.window, pg.Color(0,0,100), node.position, 7.5)
    
    def draw_grid(self) :
        for w in range(0, util.screen_wdth, util.grid) :
            pg.draw.line(self.window, pg.Color(50, 0, 0), Vec2(w, 0), Vec2(w, util.screen_hgth))
        for h in range(0, util.screen_hgth, util.grid) :
            pg.draw.line(self.window, pg.Color(50, 0, 0), Vec2(0, h), Vec2(util.screen_wdth, h))
        
        i, j = 0, 0
        for line in self.world_grid:
            for cell in line:
                if cell[0]==0:
                    pg.draw.rect(self.window, pg.Color(50, 0, 0), pg.Rect(i*util.grid, j*util.grid, util.grid, util.grid))
                # if cell[0]==2:
                #     pg.draw.rect(self.window, pg.Color(0, 100, 0), pg.Rect(i*util.grid, j*util.grid, util.grid, util.grid))
                i+=1
            j+=1
            i=0
    
    def init_world_grid(self) -> None :
        wdth, hgth = int(util.screen_wdth/util.grid), int(util.screen_hgth/util.grid)
        self.world_grid.append([[0, None] for _ in range(0, wdth)])
        for _ in range(0, hgth-2):
            temp = [[0, None]]
            temp += [[1, None] for _ in range(0, wdth-2)]
            temp.append([0, None])
            self.world_grid.append(temp)
        self.world_grid.append([[0, None] for _ in range(0, wdth)])
    
    def flood_fill(self, start : Vec2, graph : SparceGraph) -> None:
        queue = []
        grid_size = Vec2(len(self.world_grid), len(self.world_grid[0]))
        
        if self.is_cell_valid(grid_size, int(start.x), int(start.y)):
            node = Node(util.grid_to_coord(int(start.x), int(start.y)))
            graph.add_node(node)
            
            #index x, index y and node id
            queue.append([int(start.x), int(start.y), node.index])
        
        while queue:
            curr_cell : Vec2 = queue.pop()
            curr_x, curr_y, curr_node_id = curr_cell[0], curr_cell[1], curr_cell[2]
            
            node = None
            
            for i in range(-1, 2):
                for j in range(-1, 2):
                    n = self.is_cell_valid(grid_size, curr_x+i, curr_y+j)
                    print(n)
                    if n[0]:
                        if n[1] != None:
                            graph.add_edge(Edge(curr_node_id, n[1]))
                        else:
                            node = Node(util.grid_to_coord(curr_x+i, curr_y+j))
                            graph.add_node(node)
                            graph.add_edge(Edge(curr_node_id, node.index))
                            self.world_grid[curr_x+i][curr_y+j] = [2, node.index]
                            queue.append([curr_x+i, curr_y+j, node.index])     
                
    def is_cell_valid(self, grid : Vec2, x : int, y : int) -> [bool, int]:
        if x < 0 or x >= grid.x or\
            y < 0 or y >= grid.y or\
            self.world_grid[x][y][0] == 0:
                return [False, None]
        elif self.world_grid[x][y][0] == 2:
            return [True, self.world_grid[x][y][1]]
        else: return [True, None]
            
        