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
        self.world_grid : list[int] = []
        self.init_world_grid()
        self.flood_fill(Vec2(1,1), self.g)
        
    def update(self, dt : float) -> None :
        pass
        # test_pos = Vec2(100, 500)
        # pg.draw.circle(self.window, pg.Color(255, 0, 0), test_pos, 10)
        # node = self.get_closest_node( test_pos, self.g)
        # pg.draw.circle(self.window, pg.Color(0,255,0), node.position, 7.5)
        
    def draw(self) -> None :
        self.window.fill(pg.Color(0,0,0)) # BACKGROUND
        self.draw_graph(self.g)
        self.draw_grid()
        
        
    def draw_graph(self, graph : SparceGraph) :
        for edges in graph.edge_list_vector:
            for edge in edges:
                node_1 = graph.node_vector[edge.from_node].position
                node_2 = graph.node_vector[edge.to_node].position
                pg.draw.line(self.window, pg.Color(0, 50, 0), node_1, node_2, 5)
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
                if cell==0:
                    pg.draw.rect(self.window, pg.Color(50, 0, 0), pg.Rect(i*util.grid, j*util.grid, util.grid, util.grid))
                if cell==2:
                    pg.draw.rect(self.window, pg.Color(0, 100, 0), pg.Rect(i*util.grid, j*util.grid, util.grid, util.grid))
                i+=1
            j+=1
            i=0
    
    def generate_nodes(self, graph : SparceGraph):
        for w in range(int(util.grid/2), int(util.screen_wdth), util.grid):
            for h in range(int(util.grid/2), int(util.screen_hgth), util.grid):
                graph.add_node(Node(Vec2(w, h)))
   
#deosnt work for some reason 
    # def get_closest_node(self, pos : Vec2, graph : SparceGraph) -> Node :
    #     curr_closest : Node = None
    #     curr_dist : float = 9999999999
    #     for node in graph.node_vector:
    #         temp = node.position.distance_to(pos)
    #         if temp <= curr_dist:
    #             curr_dist = temp
    #             curr_closest = node
    #     return node
    
    def init_world_grid(self) -> None :
        wdth, hgth = int(util.screen_wdth/util.grid), int(util.screen_hgth/util.grid)
        self.world_grid.append([0 for _ in range(0, wdth)])
        for _ in range(0, hgth-2):
            temp = [0]
            temp += [1 for _ in range(0, wdth-2)]
            temp.append(0)
            self.world_grid.append(temp)
        self.world_grid.append([0 for _ in range(0, wdth)])
    
    def flood_fill(self, start : Vec2, graph : SparceGraph) -> None:
        queue = []
        queue.append(start)
        
        grid_size = Vec2(len(self.world_grid), len(self.world_grid[0]))
        
        
        while queue:
            curr_cell : Vec2 = queue.pop()
            curr_x, curr_y = int(curr_cell.x), int(curr_cell.y)
            
            if self.is_cell_valid(grid_size, curr_x+1, curr_y):
                self.world_grid[curr_x+1][curr_y] = 2
                queue.append(Vec2(curr_x+1, curr_y))
            if self.is_cell_valid(grid_size, curr_x-1, curr_y):
                self.world_grid[curr_x-1][curr_y] = 2
                queue.append(Vec2(curr_x-1, curr_y))
                
            if self.is_cell_valid(grid_size, curr_x, curr_y+1):
                self.world_grid[curr_x][curr_y+1] = 2
                queue.append(Vec2(curr_x, curr_y+1))
            if self.is_cell_valid(grid_size, curr_x, curr_y-1):
                self.world_grid[curr_x][curr_y-1] = 2
                queue.append(Vec2(curr_x, curr_y-1))
                
            
            
    
    def is_cell_valid(self, grid : Vec2, x : int, y : int) -> bool :
        if x < 0 or x >= grid.x or\
            y < 0 or y >= grid.y or\
            self.world_grid[x][y] != 1 or\
            self.world_grid[x][y] == 2:
                return False
        else: return True
            
        