#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

net = Mininet( topo=None,
                   build=False,
                   ipBase='117.8.4.0/8',
                   link=TCLink)

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s4 = net.addSwitch('s4')
    s2 = net.addSwitch('s2')
    s8 = net.addSwitch('s8')
    s1 = net.addSwitch('s1')
    s3 = net.addSwitch('s3')
    s7 = net.addSwitch('s7')
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')

    info( '*** Add hosts\n')
    h6 = net.addHost('h6',  ip='117.8.4.6')
    h3 = net.addHost('h3',  ip='117.8.4.3')
    h8 = net.addHost('h8',  ip='117.8.4.8')
    h1 = net.addHost('h1',  ip='117.8.4.1')
    h5 = net.addHost('h5',  ip='117.8.4.5')
    h4 = net.addHost('h4',  ip='117.8.4.4')
    h7 = net.addHost('h7',  ip='117.8.4.7')
    h2 = net.addHost('h2',  ip='117.8.4.2')


    info( '*** Add links\n')
    net.addLink(s2, h1, bw=100, delay='10ms')
    net.addLink(s2, h2, bw=100, delay='10ms')
    net.addLink(s1, s2, bw=100, delay='100ms')
    net.addLink(s2, s3, bw=100, delay='100ms')
    net.addLink(s3, s4, bw=100, delay='100ms')
    net.addLink(s4, s5, bw=100, delay='100ms')
    net.addLink(s1, s6, bw=100, delay='100ms')
    net.addLink(s6, s7, bw=100, delay='100ms')
    net.addLink(s7, s8, bw=100, delay='100ms')
    net.addLink(s4, h3, bw=100, delay='10ms')
    net.addLink(s5, h4, bw=100, delay='10ms')
    net.addLink(s5, h5, bw=100, delay='10ms')
    net.addLink(s6, h7, bw=100, delay='10ms')
    net.addLink(s6, h8, bw=100, delay='10ms')
    net.addLink(s8, h6, bw=100, delay='10ms')

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s4').start([c0])
    net.get('s2').start([c0])
    net.get('s8').start([c0])
    net.get('s1').start([c0])
    net.get('s3').start([c0])
    net.get('s7').start([c0])
    net.get('s5').start([c0])
    net.get('s6').start([c0])

    info( '*** Post configure switches and hosts\n')
    net.pingAll()
    net.stop()







if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
