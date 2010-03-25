#!/usr/bin/env python
from psychopy import visual, filters, event, core
import numpy as np
"""Textures (e.g. for a PatchStim) can be created from custom numpy arrays. 

For this they should be square arrays, with size in powers of two (e.g. 64,128,256,512)
A 256x256 array can then be given colour efficiently using the normal stimulus methods.
A 256x256x3 array has its colour defined by the array (obviously).

This demo creates a radial array as a patch stimulus, using helper functions from 
psychopy.filters and then creates a second sub-stimulus created from a section of
the original. Both are masked simply by circles.
"""
win = visual.Window([800,600], units='pix')

#generate the radial textures
cycles=6
res=512
radius = filters.makeRadialMatrix(res)
radialTexture = np.sin(radius*2*np.pi*cycles)
mainMask = filters.makeMask(res)*2-1

#select the upper left quadrant of our radial stimulus
radialTexture_sub = radialTexture[256:,0:256]
#and create an appropriate mask for it
subMask = filters.makeMask(res, radius=0.5, center=[-0,0])*2-1

bigStim = visual.PatchStim(win, tex=radialTexture, mask=mainMask,
   rgb=[1,1,1], size=512, sf=1.0/512, interpolate=True)
#draw the quadrant stimulus centred in the top left quadrant of the 'base' stimulus (so they're aligned)
subStim = visual.PatchStim(win, tex=radialTexture_sub, pos=(-128,128), mask=subMask,
   rgb=[1,1,1], size=256, sf=1.0/256, interpolate=True)

bigStim.draw()
subStim.draw()

while True:
    #clockwise rotation of sub-patch
    for i in range(-360,360):
        bigStim.draw()
        subStim.setOri(i/10) #control speed 
        subStim.draw()
        
        win.flip()
    
    #smooth reversal to anticlockwise    
    for i in range(-360,360):
        bigStim.draw()
        subStim.setOri(-i/10) #control speed 
        subStim.draw()
        try:
            instruction.draw()
        except:
            pass
        win.flip()

    for keys in event.getKeys():
        if keys in ['escape','q']:
            core.quit()
    event.clearEvents()