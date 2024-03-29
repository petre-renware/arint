![arint_logo](../pictures/arint_logo.png){ width="55" align=left }
<small markdown>**ALPHAREN CORE-Integrator (ARINT) System**<br>
*(c) 2021 RENware Software Systems. RESTRICTED only for project internal use*
</small><br><br><br>


# Outgoing (channels) 
<small>

Product 0000-0156 0.0 to current version 

* 210731 me new doc 
* 210801 me last update 
</small> 

***Table of contents:***

[TOC]

***



## Outgoing channels overview 

An outgoing channel is a **output endpoint** from a service. It will act as an endpoint usable by a service to access an external system. They will be named as short *OUTGOING* or *OUTCONNS*. 

Outgoings can use multiple standard destinations, SAP  queues (ex AMQPz IBM), databases, mail and so on. 

Outconns are typically invoked (by a service) using attributes from self.out, e.g. self.out.rest, self.out.amqp, self.out.sap and so on, maintaining a connection pool internally when needed so that services can just focus on the invocation part. 

## REST outgoing definition 

For an **outgoing**, the following parameters must be provided: 

* Name 
* Host 
* URL path
* Data format
* Service
* Security definition

<small>

(*NOTE:* it is important to retain the default HEAD ping method, because it will be used to check the endpoint availability) 
</small>

**Name** is the ARCLST name of the channel.

**URL path** is the address of channel endpoint. This is part of ARCLST route, ie `ARCLST_path.../URL_path`.

**Data format** is the format of data that will be exchanged through this channel. Usual (for REST channels at least) is to specify here *JSON*. 

**Service** is the name of the service that will be called when channel is invoked.

**Security** represents the security domain that will be applied to this channel.

Other parameters could also be specified here, for example if there are supplementary parameters (like those with ? after the route), header info (for out channels) and so on.