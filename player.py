import sys
import Ice
Ice.loadSlice('drobots.ice')
import drobots


class PlayerI(drobots.Player):
    def __init__(self, current=None):
        self.factories = 1
        self.defenders = 1
        self.attackers = 1

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

    def makeController(self, bot, current=None):
        print("Make controller starting!!!!")

        container_prx = services.ContainerPrx.checkedCast(get_proxy("Container"))
        factory_prx = drobots.FactoryPrx.checkedCast(get("Factory"+str(self.contFac)))

        robot_prx = factory_prx.make(bot, self.attackers, self.defenders)

        if (bot.ice_isA("::drobots::Attacker")):
            container_prx.link("RobotAttacker"+str(self.attackers), robot_prx)
            self.attackers += 1

        elif (bot.ice_isA("::drobots::Defender")):
            container_prx.link("RobotDefender"+str(self.defenders), robot_prx)
            self.defenders += 1

        if (self.factories == 3):
            self.factories = 1
        else:
            self.factories += 1

        return robot_prx

    def get_proxy(str_id)
        return current.adapter.getCommunicator().stringToProxy(str_id)
