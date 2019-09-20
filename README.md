# Redes SDN usando mininet 

_En este repositorio podremos ver el desarrollo de una pequeña red usando mininet y python._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


###<span style="color:green">Pre-requisitos 📋</span> 
*Mininet
*Ubuntu
*editor de texto o blog de notas


### Instalación 🔧

_Pasos de instalacion en la pag oficial de mininet [aqui](http://mininet.org/download/)_


## Ejecutando las pruebas ⚙️

_Escriviendo esto en un script de python puede ejecutarlo._


### Y las pruebas de estilo de codificación ⌨️

<p align="center"> 
<img src="https://i.pinimg.com/236x/17/0d/a0/170da077057300c4ab336d030926017c.jpg" width="350"/> 
</p>


_Librerias_
```py
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
```


_definicion de la funcion que carga los valores de la red y el controlador (incluyendo los enlaces)._

```py
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
```


_Manera de agregar un swicht a la red y darle un nombre._

```py
 info( '***Add switches\n')
   s2 = net.addSwitch('s2')

```


 _Agregar un host a la red ,darle un nombre y asignarle una ip._

```py
 info( '*** Add hosts\n')
      h2 = net.addHost('h2',  ip='117.8.4.2')
```


_Asignar las conecciones entre los dispositivos._

```py
 info( '*** Add links\n')
 net.addLink(s2, h2, bw=100, delay='10ms')
```


_Construye la red con los especificado   y inicia el controlador._


```py
info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

```


_Iniciar el funcionamineto de un sw._

```py
info( '*** Starting switches\n')
    net.get('s4').start([c0])
```

```py
info( '*** Post configure switches and hosts\n')
    net.pingAll()  #ping entre todos los host#
    net.stop()    #termina la ejecucion#
```



_Inicializador del Script._


```py
if __name__ == '__main__':  #si encuentra el main carga y ejecuta el script de la clase#
    setLogLevel( 'info' )
    myNetwork()
```

## Deployment 📦

Clonar el proyecto.
```
git clone https://github.com/kenny2312/Proyecto_Integrador_Redes_SL.git
```

Ver todos los commits a traves del tiempo.
```
git log 
```

Para ejecutar el script hay que dale permisos en Ubuntu.
```
chmod network.py 750
```

Ejecutar el script.
```
sudo python network.py
```


*Podras modificar a tu gusto respetando al autor original 🤓 🤓 🤓.*



## Construido con 🛠️

_Las herramientas que utilizamos para crear el proyecto:_

* [Mininet](http://mininet.org/download/) -Simulador de redes de hosts, switches controladores y links virtuales.
* [Ubuntu 14.04](http://releases.ubuntu.com/14.04/) - El sistema operativo usado
* [MarkdownPad 2](http://markdownpad.com/) - Usado generar este readme


## Wiki 📖

Puedes encontrar mucho más acerca de SDN en la [Wiki](https://es.wikipedia.org/wiki/Redes_definidas_por_software)

## Versionado 📌

Usamos [git](https://git-scm.com/downloads) para el versionamiento del codigo.

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **kenny vera** - *Documentación* - [kenny](https://github.com/kenny2312)
* **Angel Ceballos** - *apoyo moral* - [Angel](https://github.com/AngelC01)
* **Mario Orrala** - *Trabajo Inicia* - [Mario](https://github.com/marioorrala)
 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Invita una cerveza 🍺 a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.



---

