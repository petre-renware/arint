![arint_logo](../pictures/arint_logo.png){ width="55" align=left }
<small markdown>**ALPHAREN CORE-Integrator (ARINT) System**<br>
*(c) 2021 RENware Software Systems. RESTRICTED only for project internal use*
</small><br><br><br>


# Channel security


***Table of contents:***

[TOC]

***





## Security overview 

Mainly security is used to secure channels. As long as a service can interact with external world thru channels, this is clearly enough for all normal operations. 

System allow for multiple security models, types and protocols. There ca be active more security rules, each one applicable as needed in various circumstances. 


## Define basic security rules

By **basic security** is understood a rule based on requesting explicitly an user and a password. 

Basic security allowed **types** are:

* HTTP Basic auth
* JWT
* NTLM
* RBAC
* SSL / TLS
* API keys
* AWS
* Vaul
* WS-Security
* X-Path

<!-- #NOTE- see more details at `https://zato.io/en/docs/3.2/admin/security/channel.html` -->


-#TODO this section START HERE should be reviewed and updated / dropped -----------------------------
Basic security rules can be defined from administration console, *Security* menu, *Basic auth* entry. A security rule means:

* a name for the rule
* an username 
* a domain in which rule is applicable (think domain as a kind of grouping more rules in a set usable for a purpose, for example channels); thid approach allows for many to many relationships between security rules and channels or other objects 

Password will be generated automatically as uuid4 (guid) and This can be modified latter.
-#TODO to review section END HERE ---------------------------------------------------------------------


