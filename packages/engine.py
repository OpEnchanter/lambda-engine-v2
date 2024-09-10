import pygame

"""Engine Classes and Functions"""

class gameObjectDefaults():
    class camera():
        def init(obj):
            pass
        def runtime(obj):
            pass

class gameObject(object):
    def __init__(self, initScript, frameScript, sprite, position):
        self.initScript = initScript
        self.frameScript = frameScript
        self.sprite = sprite
        self.position = position

        self.initScript(self)
    def executeFrame(self):
        self.frameScript(self)

class scene(object):
    def __init__(self):
        self.objects = []
    def createObject(self, initScript, frameScript, sprite, position):
        self.objects.append(gameObject(initScript, frameScript, sprite, position))
    def executeSceneFrame(self):
        for obj in self.objects:
            obj.executeFrame()

class sceneManager(object):
    def __init__(self):
        self.scenes = []
        self.scnIdx = 0
    def addScene(self, scn):
        self.scenes.append(scn)
        self.scnIdx = len(self.scenes)-1
    def setScene(self, index):
        self.scnIdx = index
    def executeFrame(self):
        self.scenes[self.scnIdx].executeSceneFrame()