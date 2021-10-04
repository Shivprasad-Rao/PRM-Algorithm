#!/usr/bin/env python
# coding: utf-8
import pygame
import random
import math
import sys

from pygame.constants import SCALED
pygame.init()

length = 800#1024
width = 600#800
surface = pygame.display.set_mode((length,width))
color = (255,0,0) 
obstacle_list = []
vertex_list = []
edge_list = {}
neighbours = {}
nodes = []
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
blue = (0,0,128)
ORANGE = (252,127,3)
SCREENSIZE = [length,width]
SCREEN = pygame.display.set_mode(SCREENSIZE)

def set_tri(x,y,l):
    x0 = x
    y0 = y
    x1 = x - l/2
    y1 = y + 0.5*1.732*l
    x2 = x + l/2
    y2 = y + 0.5*1.732*l
    return ((x0,y0),(x1,y1),(x2,y2))

def draw_point(screen, x, y):
    pygame.draw.circle(screen, (0,255,0), (x,y), 5, 0) 

pygame.display.flip() 

def gen_sq(x,y,big_l):
    square = pygame.draw.rect(surface, color, pygame.Rect(x, y, big_l, big_l))
    obstacle_list.append(square)

def gen_circle(x,y,l):
    circle = pygame.draw.circle(surface, color, (x,y), l, 0)
    obstacle_list.append(circle)

def gen_tri(x,y,big_l):
    tri_points = set_tri(x,y,big_l)
    triangle = pygame.draw.polygon(surface, color, tri_points, 0)
    obstacle_list.append(triangle)


def displayText(txt,x,y):
    font = pygame.font.Font('freesansbold.ttf',24)
    text = font.render(txt,True,GREEN,blue)
    textRect = text.get_rect()
    textRect.center = (x,y)
    surface.blit(text,textRect)
    pygame.display.update()
    return

def shortestpath(graph,start,end,visited=[],distances={},predecessors={}):
    """Find the shortest path btw start & end nodes in a graph"""
    # detect if first time through, set current distance to zero
    try:
        if not visited: 
            distances[start]=0
        # if we've found our end node, find the path to it, and return
        if start==end:
            path=[]
            while end != None:
                path.append(end)
                end=predecessors.get(end,None)
            return distances[start], path[::-1]
        # process neighbors as per algorithm, keep track of predecessors
        for neighbor in graph[start]:
            if neighbor not in visited:
                neighbordist = distances.get(neighbor,float(math.inf))
                tentativedist = distances[start] + graph[start][neighbor]
                if tentativedist < neighbordist:
                    distances[neighbor] = tentativedist
                    predecessors[neighbor]=start
        # neighbors processed, now mark the current node as visited 
        visited.append(start)
        # finds the closest unvisited node to the start 
        unvisiteds = dict((k, distances.get(k,float(math.inf))) for k in graph if k not in visited)
        closestnode = min(unvisiteds, key=unvisiteds.get)
        # now take the closest node and recurse, making it current
    except:
        pygame.time.delay(700)
        SCREEN.fill((0,0,0))
        displayText("Path Not Found",400,200)
        displayText("Try Again....!!",400,240)
        pygame.display.update()
        pygame.time.delay(1500)
        pygame.quit()
        sys.exit()     
    return shortestpath(graph,closestnode,end,visited,distances,predecessors)

def dispInstructions():
    displayText("Instructions :  ",400,160)
    displayText("Click Left Mouse Button to Create Rectangle Obstacle",400,240)
    displayText("Click Right Mouse Button to Create Circle Obstacle",400,280)
    displayText("Click Middle Mouse Button to Create Triangle Obstacle",400,320)
    displayText("Then Press Space to Continue",400,360)
    displayText("Press LMB to select First and Second Point",400,400)
    displayText("Press ESCAPE to Exit",400,500)
    displayText("Press Enter to Continue.....",400,540)
    exitLoop = False
    while not exitLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                surface.fill((0,0,0))
                pygame.display.update()  
                exitLoop = True
                break
    return 

def Loop1():
    exitLoop = False
    l = 50
    big_l = 100
    while not exitLoop:
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                mouse_button = pygame.mouse.get_pressed()
                if mouse_button[0]:
                    gen_sq(mx,my,big_l)
                if mouse_button[2]:
                    gen_circle(mx,my,l)                        
                if mouse_button[1]:
                    gen_tri(mx,my,big_l)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                exitLoop = True
                break
            pygame.display.update()
    return


def Loop2():
    node1 = None
    node2 = None
    exitLoop = False
    while not exitLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                mouse_button = pygame.mouse.get_pressed()
                if (mouse_button[0] and node1 == None):
                    mx,my = pygame.mouse.get_pos()
                    node1 = (mx,my)
                    nodes.append(node1)
                    vertex_list.append(node1)
                    pygame.draw.circle(surface,(0,255,255),node1,7,0)
                    pygame.display.update()
                if(node1 != None):
                    exitLoop = True

    exitLoop = False
    while not exitLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                mouse_button = pygame.mouse.get_pressed()
                if (mouse_button[0] and node2 == None and node1 != None):
                    mx,my = pygame.mouse.get_pos()
                    node2 = (mx,my)
                    nodes.append(node2)
                    vertex_list.append(node2)
                    pygame.draw.circle(surface,(0,255,255),node2,7,0)
                    pygame.display.update()
                if(node1 != None and node2 != None):
                    exitLoop = True
    return node1, node2
    

def Loop3():
    iterations = 50
    i = 0
    rad = 75
    while i < iterations:
        x = random.randint(0,length)
        y = random.randint(0,width)
        flag = 0
        for j in obstacle_list:
            if j.collidepoint(x,y):
                flag = flag + 1
        if flag == 0:
            vertex_list.append((x,y))
            nodes.append((x,y))
            draw_point(surface, x , y)
            pygame.display.update()
            i=i+1
    i = 0

    for node in nodes:
        neighbours = {}
        for i in range(len(nodes)):
            distance = math.dist((node[0],node[1]),(nodes[i][0],nodes[i][1]))
            if distance <= rad*rad:
                for obstacle in obstacle_list:
                    flag = 0
                    collision = obstacle.clipline((node[0],node[1]),(nodes[i][0],nodes[i][1]))
                    distance = math.dist((node[0],node[1]),(nodes[i][0],nodes[i][1]))
                    if collision:
                        flag+=1
                        break    
                if flag!=0:
                    continue
                else:    
                    pygame.draw.lines(SCREEN, BLUE, False, [(node[0],node[1]),(nodes[i][0],nodes[i][1])], 1)
                    pygame.display.update()
                    neighbours[nodes[i]] = distance
        edge_list[node] = neighbours
        pygame.display.update()

def Loop4(nodes, EdgeList):
    result = shortestpath(EdgeList, start, end)
    pygame.time.delay(500)
    for i in range(len(result[1])-1):
        pygame.draw.lines(SCREEN, ORANGE, False, [result[1][i],result[1][i+1]], 2)
        pygame.display.update()    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()  
      

dispInstructions()
Loop1()
start, end = Loop2()
Loop3()
Loop4(nodes,edge_list)