#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import Ice
Ice.loadSlice('--all drobots.ice')
Ice.loadSlice('--all services.ice')
Ice.loadSlice('--all comunication.ice')
import comunication
import drobots
import services
from robot_controller import RobotControllerAttack
from robot_controller import RobotControllerDefend


class DetectorControllerI(drobots.DetectorController):
    def __init__(self):
        self.i = 0

    def alert(self, enemy_position, enemies, current = None):
        print("Alert! Detected %d enemies. Position: (%d, %d)" % (enemies, enemy_position.x, enemy_position.y))
        container_prx = current.adapter.getCommunicator().stringToProxy("Container")
        container = services.ContainerPrx.checkedCast(container_prx)
        robot_list = container.list().values()
        self.send_attack(robot_list, enemy_position, enemies)

    def send_attack(self, robot_list, enemy_position, enemies, current = None):
        for i in range(len(robot_list)):
            if(robot_list[i].ice_isA("::comunication::RobotControllerAttacker")):
                robot = comunication.RobotControllerAttackerPrx.uncheckedCast(robot_list[i])
                robot.setEnemyPosition(enemy_position, enemies)
