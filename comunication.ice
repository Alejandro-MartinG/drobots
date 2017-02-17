// -*- mode:c++ -*-
#include "drobots.ice"

module comunication {

  interface Status {
    drobots::Point getPosition();
    int getID();
    void setScanReport(drobots::Point position, int enemies, int angle, int wide);
    void setEnemyPosition(drobots::Point position, int enemies);
  };

  interface RobotControllerDefend extends drobots::RobotController, Status {};

  interface RobotControllerAttack extends drobots::RobotController, Status {};

};
