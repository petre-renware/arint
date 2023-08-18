<small markdown>**ALPHAREN Integrator (ARINT) System**<br>
*(c) 2021 RENware Software Systems. RESTRICTED only for project internal use*
</small>


# Development Overview 
<small>

Product 0000-0156 0.0 to current version 

* 210728 me new doc 
</small> 

***Table of contents:***

[TOC]





------
## Preliminaries 

Development process over ARSRV implies basically the following components: 

* **SRV** - service
* **CHN** - channel

Fundamentally and very high level, a service (SRV) use a channel (CHN) to communicate with external environment.

------
## CHN - channel 

A channel must be defined in **ARSRV** management interface before use.

The CHN establish: 

* an own name which uniquely identifies it 
* the endpoint address 
* the protocol used 
* data formats in messages exchanged thru the channel 
* auth and other security parameters 

------
## SRV - service

A service must be written in Python then deployed to **ARSRV** in order to be used.

A service has the following high level flow: 

* defines a handler in order to be accessed by ARSRV 
* obtain any required parameters in order to properly do its job 
* connects to a channel to read required input
* make the necessary transformation over obtained data
* connects to a channel to write computed output
* log any process details for future references and errors debugging

------
## File names 

Development documents (except the current one) will be named as follows:

* **`06.DEV`** as prefix 
* *optional* a code which specify (only if is case) at which subcomponent or pritocol, and so on 
* name of the document

------
## Services names

The producer reserve a name space for its services (as built in AR Integrator or as future updates) starting with characters **AR**.

The users are free to name how they wants their own developed services, but not start with AR characters. Respecting this rule will allow producer future updates to overwrite *client own developed services*.

This rule should apply as general validity for any components names, for example channel names. 

*Anyway the customer must be aware that names starting with `AR` characters are reserved and are subject of future changes without any notice or change log.*