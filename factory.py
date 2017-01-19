#!/usr/bin/python
# -*- coding:utf-8; mode:python -*-

import sys
import Ice
Ice.loadSlice('--all drobots.ice')
Ice.loadSlice('--all services.ice')
import drobots
import services
from robot_controller import RobotControllerAttack
from robot_controller import RobotControllerDefend

class FactoryI(services.Factory):
    def make(self, robot, attackers, defenders, current=None):
        servant_ctrl = self.create_servant(robot, attackers, defenders)
        controller_prx = current.adapter.addWithUUID(servant_ctrl)
        prx_id = controller_prx.ice_getIdentity()
        direct_prx = current.adapter.createDirectProxy(prx_id)

        robotCtrl_prx = drobots.RobotControllerPrx.checkedCast(direct_prx)

        return robotCtrl_prx

    def create_servant(self, robot, attackers, defenders):
        if (robot.ice_isA("::drobots::Attacker")):
            return RobotControllerAttack(robot, attackers)
        elif (robot.ice_isA("::drobots::Defender")):
            return RobotControllerDefend(robot, defenders)

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
