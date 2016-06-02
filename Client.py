import sys
import Ice
Ice.loadSlice('drobots.ice')
import drobots
import Player


class Client(Ice.Application):
    def run(self, argv):
    broker = self.communicator()
    adapter = broker.createObjectAdapter("PlayerAdapter")

    servant = Player(adapter)
    proxyServer = adapter.add(servant, broker.stringToIdentity("Alexxx"))
    prx_id = proxyServer.ice_getIdentity()
    direct_prx = adapter.createDirectProxy(prx_id)
    player = drobots.PlayerPrx.uncheckedCast(direct_prx)

    adapter.activate()

    proxyClient=self.communicator().propertyToProxy("Game")
    game=drobots.GamePrx.checkedCast(proxyClient)
    name = "ale12344"
    game.login(player, str(name))
    print("logueado?")

    self.shutdownOnInterrupt()
    broker.waitForShutdown()

Cliente().main(sys.argv)
