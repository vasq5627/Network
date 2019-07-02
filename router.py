#!/usr/bin/python
# File: legacy_router.py

from mininet.net import Mininet
from mininet.node import Host,Node
from mininet.cli import CLI
from mininet.log import setLogLevel,info

def init_network():

	net = Mininet ( topo=None,
					build=False,
					ipBase='10.0.0.0/24')
	info( '*** Adding controller\n')			
	r1=net.addHost('r1',cls=Node,ip='10.0.1.1/24')
	r1.cmd('sysctl -w net.ipv4.ip_forward=1')
	
	info( '*** Add hosts\n')
	h1=net.addHost('h1',cls=Host,ip='10.0.1.10/24',defaultRoute='via 10.0.1.1')
	h2=net.addHost('h2',cls=Host,ip='10.0.2.10/24',defaultRoute='via 10.0.2.1')
	
	info( '*** Add links\n')
	net.addLink(h1,r1, intfName1='h1-eth0',intfName1='r1-eth0',params2={'ip':'10.0.1.1/24'})
	net.addLink(h2,r1, intfName2='h2-eth0', intfName2='r1-eth1',params2={'ip':'10.0.2.1/24'})

	 info( '*** Starting network\n')
	net.build()

	CLI(net)
	net.stop()
	
if __name__=='__main__' :
	setLogLevel('info')
	my_network()
