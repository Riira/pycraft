from mcpi_e.minecraft import*
from mcpi_e.block import*
import collections
collections.Iterable=collections.abc.Iterable
import collections.abc
from _collections_abc import Iterable

serverAddress= "Pycraft.yasan.ac"
pythonPort= 29035
playerName= "r_samadi"

mc=Minecraft.create(serverAddress,pythonPort,playerName)

open("maze_map.txt")