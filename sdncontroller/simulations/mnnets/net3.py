"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1',mac="aa:aa:aa:aa:aa:a1",ip="1.0.0.1/24")
        rightHost = self.addHost( 'h2',mac="aa:aa:aa:aa:aa:a2",ip="1.0.0.2/24")
       	switch1 = self.addSwitch( 's1')
        switch2 = self.addSwitch( 's2')

        # Add links
        self.addLink( leftHost, switch1 )
	self.addLink( switch1, switch2 )        
	self.addLink( switch2, rightHost )


topos = { 'mytopo': ( lambda: MyTopo() ) }

