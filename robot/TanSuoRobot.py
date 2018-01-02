from engine import ImageEngine
from engine import MouseEngine
from engine import RegisterEngine
from base import Log


class TanSuoRobot:

    # master or slave or self mode
    # 1-master
    # 2-slave
    # 3-self
    masterMode = 0

    # for control battle count
    countLimit = 0

    # current battle count
    currentCount = 0


    # engine declare
    imageengine = 0
    mouseengine = 0
    registerengine = 0


    def __init__(self,mastermode,countlimit):
        self.masterMode = mastermode
        self.countLimit = countlimit

        # engine initial
        self.registerengine = RegisterEngine.RegisterEngine()
        self.imageengine = ImageEngine.ImageEngine(self.registerengine)
        self.mouseengine = MouseEngine.MouseEngine(self.registerengine)

        return

    def start(self):
        Log.log("start")
        if self.masterMode == 1:
            self.masterstart()
        elif self.masterMode == 2:
            self.salvestart()
        elif self.masterMode == 3:
            self.selfstart()
        else:
            self.stop()
        return

    def salvestart(self):
        Log.log("slave start")
        while(self.currentCount < self.countLimit):
            if self.isatendbattlewindow():
                self.clickendbattle()
            elif self.isatshowspoilswindow():
                self.clicklowerright()
            elif self.isatteaminvitewindow():
                self.clickyes()
            elif self.isatbaoxiangwindow():
                self.clickbaoxiang()
            # elif self.isatlosewindow():
            #     self.clicklose()
            # elif self.isatnoenergywindow():
            #     self.stop()
            # elif self.isatendbattlewindow():
            #     self.clickendbattle()
            # elif self.isatwinwindow():
            #     self.clickwin()
            # elif self.isatxuanshanginvitewindow():
            #     self.clickno()
            else:
                self.cannotrecognisesolog()
        return

    def masterstart(self):
        return

    def selfstart(self):
        return



# image recognition

    def isatwinwindow(self):
       return self.imageengine.find_picture("win")

    def isatlosewindow(self):
        return self.imageengine.find_picture("lose")

    def isatendbattlewindow(self):
        return self.imageengine.find_picture("endbattle")

    def isatbaoxiangwindow(self):
        return self.imageengine.find_picture("baoxiang")

    def isatshowspoilswindow(self):
        return self.imageengine.find_picture("showspoils")

    def isatteaminvitewindow(self):
        return self.imageengine.find_picture("yes")

    def isatnoenergywindow(self):
        return self.imageengine.find_picture("noenergy")

    def isatxuanshanginvitewindow(self):
        return self.imageengine.find_picture("xuanshanginvite")


# action

# click action

    def clickwin(self):
        return self.mouseengine.clickdefault()

    def clicklose(self):
        return self.mouseengine.clickdefault()

    def clickendbattle(self):
        return self.mouseengine.clickdefault()

    def clickbaoxiang(self):
        return self.mouseengine.clickdefault()

    def clicklowerright(self):
        return self.mouseengine.clickadddefault(0,-100)

    def clickyes(self):
        # self.imageengine.find_picture("yes")
        return self.mouseengine.clickdefault()

    def clickno(self):
        return self.mouseengine.clickdefault()

    def cannotrecognisesolog(self):
        Log.log("cannot recognise")
        return

# other action

    def stop(self):
        self.currentCount = self.countLimit
        Log.log("stop")
        return
