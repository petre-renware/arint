

[TOC]


# CHANGELOG

-#NOTE: here are the SDEVEN procedure codes:
    130.02 Product Overview (REQUIRED if not present in Datasheet)
    130.04 Licensing Editions & Pricing (OPTIONAL)
    130.05 Service & Training Programmes (OPTIONAL as RECOMMENDED)
    810.02 System Landscape (REQUIRED)
    810.46 Product Features - update of 130.01 (REQUIRED)





## 0.0.5-release (#NOTE wip...)

* tbd... update doc `system_landscape.md` to ...see TODO - from here continue review...

* wip...

* 230818piu_h update `130.00-Overview.md` for outline structure to keep only one heading 1 and small text corrections
* 230818piu_g apply ARINT logo on site and documents & updated the "facelift" on all docs; refactored `...Overview.md` to `130.02-Overview.md`
* 230818piu_f updated all doc layout ref TOC and header
* 230818piu_e created `.../euma/adma_catalog.md` doc as all *adma documentation* catalog and ref it in navigation instead of all docs
* 230818piu_d created `.../euma/euma_catalog.md` doc as all *euma documentation* catalog and ref it in navigation instead of all docs
* 230818piu_c updated `doc_src/index.md` with info from `README.md` and linked `README.md` to this `index.md` file
* 230818piu_b updated `README.md` section ref to documentation
* 230818piu_a restructured navigation, introduced a new entry for "System overview" and refined RENware entry with: contact, how to buy, support




## 0.0.4-alpha (230818 06:10)

* 230818piu_c refactored documentation header for a simpler and better visual aspect
* 230818piu_b refactored `06.DEV-service-anathomy` to `06.DEV-service-anatomy`
* 230818piu_a updated navigation to reflect documentation and future product demo system
* 230817piu_e renamed nav entry "Design documentation" to "User documentation" and "Development how..." to "Development documentation"
* 230817piu_d updated `requirements.txt` with new versions
* 230817piu_c more:
    * created file `pip_versions_chk_upgrade.md` with useful `pip` commands ref packages version
    * updated all local Python environment (`.wenv`) and that was perfect !!! (need to replicate in SDEVEN at least)
* 230817piu_b fixed `06.DEV-service-anathomy.md` diagram ref service process as a whole
* 230817piu_a clean `06.DEV-service-anathomy.md` document and make a diagram ref service process as a whole (just commented, to be finished...)
* 230815piu_a updated `requirements.txt` & `mkdocs.yml` with all things from `SDEVEN` as good documentation project




## 0.0.3-alpha standardized project structure (230814 1900)

* 230814piu_d updated project firs structure (dev portal in `doc_src/`)
* 230814piu_c updated project firs structure (dev portal in `static_portal/`)
* 230814piu_b update `mkdocs run` workflow to install al requirements and to generate in `docs/` dir
* 230814piu_a created workflow to run mkdocs on ubuntu. should test if PDFs are correctly generated and install chromium package, preferably if found one as `pip` installable by `requirements.txt`
* 230711piu_a upload REN logo and set `mkdocs.yaml` to point it - needs rebuild




## 0.0.2-beta (230706 09:00)

* 230706piu_a reorganized project directories to publish doc through GitHub (released site in `docs/` and raw source doc in `doc_source/`)
* 230608piu_a update doc `system_landscape.md` ref ARCLST components
* 230607piu_a update doc `system_landscape.md` to make a more clear distinction of what is ARCLST and its components and what is outside it
* 230606piu_a rename and first clean of doc `system_landscape.md` (old name `05-Landscape.md`)




## 0.0.2-004.alpha (230605 15:30)

* 230605piu_d refined docs, created `880-RLSE/adma` & `880-RLSE/euma` to move from existing documentation; first document `02-installation.md` to `...880-RLSE/adma/system_installation.md`




## 0.0.2-003.alpha (230605 06:35)

* 230605piu_c check and cleanup following documentation: `.../810-DSGN/02-Installation.md`, `index.md`




## 0.0.2-002.alpha (230605 05:30)

* 230605piu_b check and cleanup following documentation: `.../810-DSGN/01-Overview.md`; updated copyright information (year) in all existing docs
* 230605piu_a move all project docs AND mkdocs.yml to `docs` directory for "an uniform and more consistent" `mkdocs` documentation & site generator




## 0.0.1-001.beta (230601 06:30)

* 230601piu_b created `arint` public repo on GitHub and cloned pj here; initialized a LICENCE draft file
* 230601piu_a restarted project - create environments for building a static site with mkdocs and restructured project for 810-DSGN
* 230531piu_a unarchive 0.0.0-dev.02 and recover project from REN git "backups"




## 0.0.0-dev.02 initial project idea and design

