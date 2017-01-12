import Ice
import sys
Ice.loadSlice('drobots.ice')
import drobots
import Container
from RobotController import RobotControllerAttack
from RobotController import RobotControllerDefend

class FactoryI(drobots.Factory):
    def make(self, robot, contA, contD, current=None):
        servant_ctrl = create_servant(robot, contA, contD)
        controller_prx = current.adapter.addWithUUID(servant_ctrl)
        prx_id = controller_prx.ice_getIdentity()
        direct_prx = current.adapter.createDirectProxy(prx_id)

        robotCtrl_prx = drobots.RobotControllerPrx.checkedCast(direct_prx)

        return robotCtrl_prx

    def create_servant(robot)
        if (robot.ice_isA("::drobots::Attacker")):
            return RobotControllerAttack(robot, contA)
        elif (robot.ice_isA("::drobots::Defender")):
            return RobotControllerDefend(robot, contD)

class ServerFactory(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        adapter = broker.createObjectAdapter("Factory_Adapter")

        properties = broker.getProperties().getProperty("Identity")
        identidad = broker.stringToIdentity(properties)

        servant = FactoryI()

        proxy_server = adapter.add(servant, identidad)

        print(str(proxy_server))

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0

sys.exit(ServerFactory().main(sys.argv))
