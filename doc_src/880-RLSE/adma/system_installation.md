<<<<<<<< HEAD:doc_source/880-RLSE/adma/system_installation.md
<small>**ALPHAREN ARINT System**<br>
*(c) 2021 RENware Software Systems. RESTRICTED only for project internal use*
</small>


<h1>Installation</h1>


<small>***Document control:***<br>
* last update date: 230605<br>
* last updated by: petre iordanescu
</small>


[TOC]


# Install helpers
========
![arint_logo](../../pictures/arint_logo.png){ width="55" align=left }
<small markdown>**ALPHAREN Integrator (ARINT) System**<br>
*(c) 2021 RENware Software Systems. RESTRICTED only for project internal use*
</small><br><br><br>


# System Installation


<small>***Document control:***<br>
* last update date: 230605<br>
* last updated by: petre iordanescu
</small>



***Table of contents:***

[TOC]

***





## Install helpers
>>>>>>>> petre-dev:doc_src/880-RLSE/adma/system_installation.md

```
sudo apt-get install apt-transport-https curl
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo apt-get install tzdata


```
<<<<<<<< HEAD:doc_source/880-RLSE/adma/system_installation.md
## Package key
========
### Package key
>>>>>>>> petre-dev:doc_src/880-RLSE/adma/system_installation.md

```
curl -s https://zato.io/repo/zato-3.2-48849AAD40BCBB0E.pgp.txt | sudo apt-key add -
```

<<<<<<<< HEAD:doc_source/880-RLSE/adma/system_installation.md
## Add apt repository
========
### Add apt repository
>>>>>>>> petre-dev:doc_src/880-RLSE/adma/system_installation.md

```
sudo add-apt-repository \
   "deb [arch=amd64] https://zato.io/repo/stable/3.2/ubuntu $(lsb_release -cs) main"
```

<<<<<<<< HEAD:doc_source/880-RLSE/adma/system_installation.md
## Install zato
========
### Install zato
>>>>>>>> petre-dev:doc_src/880-RLSE/adma/system_installation.md

```
sudo apt-get install zato
```


<<<<<<<< HEAD:doc_source/880-RLSE/adma/system_installation.md
## Apply latest updates
========
### Apply latest updates
>>>>>>>> petre-dev:doc_src/880-RLSE/adma/system_installation.md

```
sudo su - zato
cd /opt/zato/current && ./update.sh
```

<<<<<<<< HEAD:doc_source/880-RLSE/adma/system_installation.md
## Check & confirm
========
### Check & confirm
>>>>>>>> petre-dev:doc_src/880-RLSE/adma/system_installation.md

```
zato --version
```



<<<<<<<< HEAD:doc_source/880-RLSE/adma/system_installation.md
# Create a quick cluster environment

## Create the cluster
========
## Create a quick cluster environment

### Create the cluster
>>>>>>>> petre-dev:doc_src/880-RLSE/adma/system_installation.md

This will create a new cluster ARCLST named **`arclst`** in directory `/opt/zato/env/arclst`.

```
sudo su - zato
mkdir -p ~/env/arclst
cd ~/env/arclst
zato quickstart create . sqlite localhost 6379
```

Response should looks like that:

```
[1/8] Certificate authority created
[2/8] ODB schema created
[3/8] ODB initial data created
[4/8] server1 created
[5/8] Load-balancer created
Superuser created successfully.
[6/8] Dashboard created
[7/8] Scheduler created
[8/8] Management scripts created
Quickstart cluster quickstart-904765 created
Dashboard user:[admin], password:[F7qCOiabas5ToQ7EWupLrHOn9iVHzyBv]
Visit https://zato.io/support for more information and support options
```

<<<<<<<< HEAD:doc_source/880-RLSE/adma/system_installation.md
## Change web console password
========
### Change web console password
>>>>>>>> petre-dev:doc_src/880-RLSE/adma/system_installation.md

The username web administraton console is **admin**. To change the password in **admin**, do:

```
cd ~/env/arclst/web-admin/
zato update password . admin
```



<<<<<<<< HEAD:doc_source/880-RLSE/adma/system_installation.md
# Configuration & access


## Machine general configuration
========
## Configuration & access


### Machine general configuration
>>>>>>>> petre-dev:doc_src/880-RLSE/adma/system_installation.md

* Test machine ren-cluster, 192.168.1.190
* Admin console port 8183
* Credentials admin / admin
* public access http://90.84.237.32:8183 user admin pswd admin 



<<<<<<<< HEAD:doc_source/880-RLSE/adma/system_installation.md
## Machine environment configuration
========
### Machine environment configuration
>>>>>>>> petre-dev:doc_src/880-RLSE/adma/system_installation.md

* User `sudo su - zato`
* Path `/opt/env/arclst`
* web admin console path `/opt/env/arclst/web-admin`
* ZATO Server `arclst`


<<<<<<<< HEAD:doc_source/880-RLSE/adma/system_installation.md
## System launch scripts
========
### System launch scripts
>>>>>>>> petre-dev:doc_src/880-RLSE/adma/system_installation.md

* `zato-qs-start.sh`
* `zato-qs-restart.sh`
* `zato-qs-stop.sh`


Server start in background mode, NOT as daemon.




<<<<<<<< HEAD:doc_source/880-RLSE/adma/system_installation.md
# Installation notes
========
## Installation notes
>>>>>>>> petre-dev:doc_src/880-RLSE/adma/system_installation.md

None. Everything works as documented. ATTN open 8183 port

