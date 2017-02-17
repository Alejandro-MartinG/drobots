#!/usr/bin/python
# -*- coding:utf-8; mode:python -*-

import sys
import Ice
Ice.loadSlice('drobots.ice --all')
import drobots
Ice.loadSlice('services.ice --all')
import services
Ice.loadSlice('comunication.ice --all')
import comunication
import math
import random

class RobotControllerDefend(comunication.RobotControllerDefend):
    def __init__(self, bot, id, current=None):
        self.bot = bot
        self.is_moving = False
        self.robot_id = id
        print("¡Robot DEFENDER ready!")

    def turn(self, current=None):
        if not self.robotDestroyed():
            position = self.bot.location()

            if(self.is_moving == False):
                if(position.x <= 199 and position.y <= 199):
                    angle = random.randint(0, 90)
                    self.bot.drive(angle, 100)
                elif(position.x <= 199 and position.y >= 199):
                    angle = random.randint(270,359)
                    self.bot.drive(angle, 100)
                elif(position.x > 199 and position.y < 199):
                    angle = random.randint(90, 180)
                    self.bot.drive(angle, 100)
                elif(position.x > 199 and position.y > 199):
                    angle = random.randint(180, 270)
                    self.bot.drive(angle, 100)

                self.is_moving = True

            else:
                if(position.x <= 40 or position.y <= 40 or position.x >= 339 or position.y >= 339):
                    self.bot.drive(0,0)
                    self.is_moving = False

            scan_angle = random.randint(1,359)
            scan_wide = random.randint(1, 20)

            try:
                n_robots = self.bot.scan(scan_angle, scan_wide)

                if(n_robots > 1):
                    print('%d Robots find near (%d,%d) in angle %d with wide %d' % (n_robots, position.x, position.y, scan_angle, scan_wide))
                    # self.send_scan(position, n_robots, scan_angle, scan_wide)
                    print("Enviando escaneo")
                    container_prx = current.adapter.getCommunicator().stringToProxy("Container")
                    container = services.ContainerPrx.checkedCast(container_prx)
                    proxy_list = container.list().values()

                    for i in range(len(proxy_list)):
                        if(proxy_list[i].ice_isA("::comunication::RobotControllerAttacker")):
                            print("RobotDefender report a SCANED ENEMY", position)
                            robot = comunication.RobotControllerAttackerPrx.uncheckedCast(proxy_list[i])
                            robot.setScanReport(position, n, angel, wide)



            except drobots.NoEnoughEnergy:
                print('Deffender without energy to scan, changing turn')

    def robotDestroyed(self, current=None):
        if(self.bot.damage == 100):
            container_prx = current.adapter.getCommunicator().stringToProxy("Container")
            container = services.ContainerPrx.uncheckedCast(container_prx)
            container.unlink("RobotDefender" + str(self.robot_id))
            print("RobotDefender" + str(self.robot_id) + "destroyed.")
            return True
        else:
            return False

    def send_scan(self, position, n, angle, wide, current=None):
        print("Enviando escaneo")
        container_prx = current.adapter.getCommunicator().stringToProxy("Container")
        container = services.ContainerPrx.checkedCast(container_prx)
        proxy_list = container.list().values()

        for i in range(len(proxy_list)):
            if(proxy_list[i].ice_isA("::comunication::RobotControllerAttacker")):
                print("RobotDefender report a SCANED ENEMY", position)
                robot = comunication.RobotControllerAttackerPrx.uncheckedCast(proxy_list[i])
                robot.setScanReport(position, n, angel, wide)



class RobotControllerAttack(comunication.RobotControllerAttack):
    def __init__(self, bot, id, current=None):
        self.bot = bot
        self.is_moving = False
        self.robot_id = id
        print("¡Robot ATACKER ready!")

    def turn (self, current=None):
        if not self.robotDestroyed():
            position = self.bot.location()

            if(self.is_moving == False):
                if(position.x <= 199 and position.y <= 199):
                    angle = random.randint(0, 90)
                    self.bot.drive(angle, 100)
                elif(position.x <= 199 and position.y >= 199):
                    angle = random.randint(270,359)
                    self.bot.drive(angle, 100)
                elif(position.x > 199 and position.y < 199):
                    angle = random.randint(90, 180)
                    self.bot.drive(angle, 100)
                elif(position.x > 199 and position.y > 199):
                    angle = random.randint(180, 270)
                    self.bot.drive(angle, 100)

                self.is_moving = True
            else:
                if(position.x <= 40 or position.y <= 40 or position.x >= 339 or position.y >= 339):
                    self.bot.drive(0,0)
                    self.is_moving = False

            cannon_angle = random.randint(1,359)
            cannon_distance = random.randint(80,199)

            try:
                self.bot.cannon(cannon_angle, cannon_distance)
            except drobots.NoEnoughEnergy:
                print('Attacker without energy to shoot, changing turn', self.bot.energy())

    def detectorInfo(self, position, enemies, current=None):
        pass

    def setScanReport(self, position, enemies, angle, wide, current = None):
        my_position = self.bot.position()
        distance = int(math.hypot(math.fabs(position.x - my_position.x), math.fabs(position.y - my_position.y)))
        if (distance > 200):
            angle = random.randint(1,359)
            distance = random.randint(80,199)

        try:
            self.bot.cannon(angle, distance)
        except drobots.NoEnoughEnergy:
            print('Attacker without energy to shoot, changing turn')

    def robotDestroyed(self, current=None):
        if(self.bot.damage == 100):
            container_prx = current.adapter.getCommunicator().stringToProxy("Container")
            container = services.ContainerPrx.uncheckedCast(container_prx)
            container.unlink("RobotAttacker" + str(self.robot_id))
            print("RobotAttacker" + str(self.robot_id) + "destroyed.")
            return True
        else:
            return False

