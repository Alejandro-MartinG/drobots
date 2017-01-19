// -*- mode:c++ -*-
#include "drobots.ice"

module services {

  exception AlreadyExists { string key; };
  exception NoSuchKey { string key; };

  dictionary<string, Object*> ObjectPrxDict;

  interface Container {
    void link(string key, Object* proxy) throws AlreadyExists;
    void unlink(string key) throws NoSuchKey;
    ObjectPrxDict list();
  };

  interface RobotControllerDefend extends drobots::RobotController {};

  interface RobotControllerAttack extends drobots::RobotController {};

  interface Factory {
    drobots::RobotController* make(drobots::Robot* robot, int cont1, int cont2);

  };

};

