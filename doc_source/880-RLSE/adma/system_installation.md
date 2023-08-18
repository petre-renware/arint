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

```
sudo apt-get install apt-transport-https curl
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo apt-get install tzdata


```
## Package key

```
curl -s https://zato.io/repo/zato-3.2-48849AAD40BCBB0E.pgp.txt | sudo apt-key add -
```

## Add apt repository

```
sudo add-apt-repository \
   "deb [arch=amd64] https://zato.io/repo/stable/3.2/ubuntu $(lsb_release -cs) main"
```

## Install zato

```
sudo apt-get install zato
```


## Apply latest updates

```
sudo su - zato
cd /opt/zato/current && ./update.sh
```

## Check & confirm

```
zato --version
```



# Create a quick cluster environment

## Create the cluster

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

## Change web console password

The username web administraton console is **admin**. To change the password in **admin**, do:

```
cd ~/env/arclst/web-admin/
zato update password . admin
```



# Configuration & access


## Machine general configuration

* Test machine ren-cluster, 192.168.1.190
* Admin console port 8183
* Credentials admin / admin
* public access http://90.84.237.32:8183 user admin pswd admin 



## Machine environment configuration

* User `sudo su - zato`
* Path `/opt/env/arclst`
* web admin console path `/opt/env/arclst/web-admin`
* ZATO Server `arclst`


## System launch scripts

* `zato-qs-start.sh`
* `zato-qs-restart.sh`
* `zato-qs-stop.sh`


Server start in background mode, NOT as daemon.




# Installation notes

None. Everything works as documented. ATTN open 8183 port

