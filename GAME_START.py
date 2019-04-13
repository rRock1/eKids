import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.minecraft import Vec3
from minecraftstuff import MinecraftDrawing
from minecraftstuff import MinecraftShape, ShapeBlock
from random import randint
from time import sleep

mc = minecraft. Minecraft.create()
mcDrawing = MinecraftDrawing(mc)
   

def prepare():
    mcDrawing.drawSphere(0, 0, 0, 10,block.SAND)
    mc.setBlock (4, 3, 1, block.BEDROCK)
    mc.setBlock (9, 8, 9, block.GLASS)
    
def game():
    while True:
        pass
    

mcDrawing.drawSphere(10, 10, 10, 5,block.DIAMOND_BLOCK)

mcDrawing.drawSphere(10, 10, 10, 3,block.AIR)            


def main():
    prepare()
    #game()
    
main()