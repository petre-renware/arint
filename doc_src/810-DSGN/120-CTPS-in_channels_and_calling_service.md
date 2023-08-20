![arint_logo](../pictures/arint_logo.png){ width="55" align=left }
<small markdown>**ALPHAREN CORE-Integrator (ARINT) System**<br>
*(c) 2021 RENware Software Systems. RESTRICTED only for project internal use*
</small><br><br><br>



# Basic concepts - in channels and calling a service



***Table of contents:***

[TOC]

***



## In Channels overview

An **IN channel** is a communication channel defined for *calling (invoking) a service* and act as *request endpoint* seen from outside world.

!!! tip "Channel term"
    The *IN channel* is also named simple *Channel* meaning that if no other details / hints are given, a "channel" shuld be understood as "IN channel".

Channels can use multiple standard protocols, such as: REST, AMQP, HL7, IBM MQ, JSON RPC, SOAP, Web Sockets, File Transfer protocols, and others. 

A channel at request will invoke an existing service.




## REST channel definition

For a *REST* channel, the following parameters must be provided:

* Name
* URL path
* Data format
* Service
* Security definition

**Name** is the ARCLST name of the channel.

**URL path** is the address of channel endpoint. This is part of ARCLST route, ie `ARCLST_path.../URL_path`.

**Data format** is the format of data that will be exchanged through this channel. Usual (for REST channels at least) is to specify here *JSON*. 

**Service** is the name of the service that will be called when channel is invoked.

**Security** represents the security domain that will be applied to this channel.

Other parameters could also be specified here, for example if there are supplementary parameters (like those with ? after the route), header info (for out channels) and so on.


### Invoking the channel

General form of invoking path will be:    `http://<user>:<password>@ARCLST_path:11223/URL_path`. 

The request is normally made thru load balancer (port 11223). The password is those defined at security domain definition. 

***NOTE:*** *The first slash (/) from URL path is part of was entered in definition and not is automatically appended. This will allow for combining channels*.
