import sys
import Ice
Ice.loadSlice('--all drobots.ice')
Ice.loadSlice('--all services.ice')
import drobots
import services

class PlayerI(drobots.Player):
    def __init__(self, current=None):
        self.factories = 1
        self.defenders = 1
        self.attackers = 1
        self.detectors = 0

    def win(self, current=None):
        print("Win")
        current.adapter.getCommunicator().shutdown()

    def lose(self, current=None):
        print("Lose")
        current.adapter.getCommunicator().shutdown()

    def gameAbort(self, current=None):
        print("Aborting game!!!")
        current.adapter.getCommunicator().shutdown()

    def makeDetectorController(self, current=None):
        print("Make detector starting")
        print("Detector controller Factory: "+str(self.factories))
        proxy_factory = current.adapter.getCommunicator().stringToProxy("Factory2")
        factory = services.FactoryPrx.checkedCast(proxy_factory)
        self.detectors += 1
        print("done detector bro!!!")

        return factory.makeDetector()

    def makeController(self, bot, current=None):
        print("Make controller starting!!!!")

        proxy = current.adapter.getCommunicator().stringToProxy("Container")
        print("Container proxy: ", proxy)
        container_prx = services.ContainerPrx.checkedCast(proxy)

        print("Make Controller Factory: "+str(self.factories))
        fproxy = current.adapter.getCommunicator().stringToProxy("Factory"+str(self.factories))
        factory_prx = services.FactoryPrx.checkedCast(fproxy)

        robot_prx = factory_prx.make(bot, self.attackers, self.defenders)

        if (bot.ice_isA("::drobots::Attacker")):
            container_prx.link("RobotAttacker" + str(self.attackers), robot_prx)
            self.attackers += 1

        elif (bot.ice_isA("::drobots::Defender")):
            container_prx.link("RobotDefender" + str(self.defenders), robot_prx)
            self.defenders += 1

        if (self.factories == 3):
            self.factories = 0

        self.factories += 1

        return robot_prx
