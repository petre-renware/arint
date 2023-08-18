<small markdown>**ALPHAREN Integrator (ARINT) System**<br>
*(c) 2021 RENware Software Systems. RESTRICTED only for project internal use*
</small>


<h1>Landscape</h1>


<small>***Document control:***<br>
* last update date: 230607<br>
* last updated by: petre iordanescu
</small>


[TOC]






# Basic components

Basic logical components of this system are:

* **(ARCLST)** Integrator Cluster subsystem
    * **(ARSRV)** Physical or virtual Server
    * **(ARLDB)** High Availability assurance service
    * **(ARWADM)** Web admin console interface
    * **(ARSCHED)** Scheduler
    * **(ARKVD)** Key-Value Data store
    * **(ARPuSuB)** Publisher Subscriber Queues
    * **(ARVPN)** Integrator VPN access

* **(ARDPX)** Discovery Service, Distribution proxy (dynamic DNS)
* **(ARMAIL)** Integrator mail
* **(#TODO)** Configuration portal #NOTE: not yet assigned code


# System Blueprints

## ARint blueprint

-#TODO a high level blueprint

## ARCLST blueprint

![ARCSLT blueprint](../pictures/system_landscape.svg)






-#TODO start and make new descriptions (based on existing) for each component

-#TODO - from here continue review




------
# ARCLST. Integrator Cluster

This component creates a local cluster formed by one or more **ARSRV** machines. Particularly can stand on one single machine with **ARSRV**.  

This is not recommended because **ARCSLT** is a *network-bounded* system and **ARSRV** is a *cpu-bounded* one, and a *cluster to cluster* integration will have to suffer.

This component can run **1 per LAN machine**.





# ARSRV. Integrator Server

This is the core / heart of each machine. It will assure information getting, processing and sending or streing.  

Other functionalities (in cooperation with **ARCLST**) cover scheduling, asynchronous processing and retrying in case of un-availability of an external system.

This component can run **n per cluster**.





# ARLDB. Integrator High Availability assurance subsystem

This component assure:

* load balancing,
* failure detection,
* service availability,
* RTT ordering access to in case of multiple **ARSRV** modules.

All **ARSRV** components work *ACTIVE ACTIVE* inside any **ARCLST**. Of course, clusters work independently each of the others.

Also, each **ARLDB** keeps a dynamic trace of any **ARCLST** from the system, so a new cluster can be added without the need of any downtime. 

This thing is also applicable inside a cluster where at any time, with any downtime, a new **ARSRV** can be added. If is right configured then will be automatically discovered and made part of cluster.

This component can run **1 per cluster**.




# ARWADM Web amin console

This will assure cluster administration, for all its servers and other components.

This component can run **n per cluster**. The reason for more ARWADM is to secure each of them.






# ARDPX. Access and distribution proxy

This module is useful when an **ARCLST** is buit on **ARSRV**s physically implemented as a set of small virtual
 machines on a single server, having their LAN. Sure, ALPHA-REN hardware will assure that, but if you're using other hardware it will be needed. 

Thiz module will stay in own LAN DMZ being directly exposed on **ARCLST** IP external access.

This module is responsible for:

* access
 the system outside its LAN without the need of a router with port forwarding.
* assurance of all reverse proxy operations.
* access on the **ARCLST** and **ARSRV**s outside cluster LAN.

This component can run **1 per machine**.








# ARMAIL Integrator mail

This module is responsible for sending administrative and notification mails from **ARCLST** cluster. 

This component can run **1 per machine**.





# ARVPN. Integrator VPN access

This module assure VPN access into the **ARCLST** cluster.









# Deployment over multiple LAN environments

In an environment with multiple LANs, in deployment architecture and process should consider the following aspects:

* every LAN should have at least its own **ARSRV** in order to communicate with other LANs
* an **ARCLST** can assure balancing and failure services inside LAN
* in order to assure balancing and failure services over LANs, each one must have its own **ARCLST** (wirh all other required components to assure corresponding services) which communicate with the others.
* a queue service is strictly required both to assure messages transport inside LAN, but also between LANs; for this reason cannot be used any queuing system but one with remote (over LANs) capabilities (aka named broker system)






