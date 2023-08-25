

[TOC]


# CHANGELOG

- For version code structure meaning see SDEVEN methodology document
- with (F) are marked those changes that are features in order to be copied in a RELNOTE file
- #NOTE sote publishing on `arint.renware.eu` from `publishing` branch
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context)



## 0.1 ALPHAREN Integrarator CORE (wip...)

* tbd... permanently follow RMAP.001 - sys 1.0 a lot of #TODO manuals
* tbd... use `SQLAlchemy` models for database ==> here: `https://zato.io/en/docs/3.2/dev/examples/sql.html`
* tbd... ref how deploy front-ends with zato `https://zato.io/docs/dev/frontend/index.html` useful to create `ARINT AdminBoatd`


### 0.1.4-release System Landscape (#TODO...)

* tbd... updated 810.02-System_Landscape.md`, ref ...


* wip...


* 220825piu_i updated `810.02-System_Landscape.md` with new pictures for ARCLST

* 230825piu_h updated Landscape picture (draw.io file)
* -#TODO---(test all up and publish)----------------
* 230825piu_g revived, tested links & updated from `230825piu_d` to `230825piu_f`. published 230825 15:45
* 230825piu_f updated and frozen `810.02-System_Landscape.md` with ARCLST structure
* 230825piu_e updated `810.02-System_Landscape.md` with ARCLST structure
* 230825piu_d updated `810.02-System_Landscape.md` with first draft list of components in new design

* 230825piu_c updated `810.02-System_Landscape.md` with a sketch and comments ref new system design
* 230825piu_b new scratch landscape diagrams: `system_landscape.fodg` (LibreOffice) & `system_landscape.drawio` (DrawIO)
* 230825piu_a set an environment on Ubuntu, with Chromium engine (selenium) & PDF generation ==> ERROR AT mkdocs run:
``` #NOTE here is the error raised:
    selenium.common.exceptions.WebDriverException: Message: Service /home/petre/.cache/selenium/chromedriver/linux64/116.0.5845.96/chromedriver unexpectedly exited. Status code was: 127
```
* 230825piu_a set version objective as "System Landscape" & updated next actions plan for version objective












### 0.1.3-release Licensing Editions and Pricing (230824 19:00)

* 230824piu_f revived, tested links & updated from `230823piu_k` to `230824piu_e`. published 230824 h14:30
* 230824piu_e finalized acceptable for a pre-release version doc `...130.04-Licensing_Editions_Pricing.md` and updated RMAP.001
* 230824piu_d updated `...130.04-Licensing_Editions_Pricing.md` introduced (as clear) component *`ARINT AdminBoard`* and *ARINT Products* as availability for an edition
* 230824piu_c updated `/810-DSGN/120-CPTS-security.md` ref security types and let a comment where find details (a link)
* 230824piu_b updated `810-DSGN/130.04-Licensing_Editions_Pricing.md` with editions options for services schema skeleton
* 230824piu_a updated `810-DSGN/130.04-Licensing_Editions_Pricing.md` with more editions and options to THINK & CREATE a coherent matrix
* 230823piu_k create first raw version of `810-DSGN/130.04-Licensing_Editions_Pricing.md` ref proposal of licensing model. Update ROADMAP ref docs status up here




### 0.1.2-release System Data and Objects (230823 18:00)

* 230823piu_j published 230823 h17:45
* 230823piu_i close at this stage  `810.03-System_Data_and_Objects.md` by letting notes for new objects creation. As an important thing in  this file, the product version is written in clear
* 230823piu_h work in progress on doc `810.03-System_Data_and_Objects.md`, section "Object categories and models"
* 230823piu_g move content of `880-RLSE/devma` to `880-RLSE/adma` and drop `devma*`. Updated `mkdocs.yml`
* 230823piu_f work in progress on doc `810.03-System_Data_and_Objects.md`
* 230823piu_e grouped all DEVELOPMENT documentation in `880-RLSE/devma/` catalog, updated `mkdocs.yml` navigation
* 230823piu_d work in progress on doc `810.03-System_Data_and_Objects.md`
* 230823piu_c first raw skeleton of doc `810.03-System_Data_and_Objects.md`
* 230823piu_b published 230823 h07:15
* 230823piu_a install `mkdocs-macros-plugin`:
    *  to be able to use external Jinja variables and macros at compiling time (see `https://mkdocs-macros-plugin.readthedocs.io/en/latest/`)
    *  updated all docs where `{}` brackets appear as doubled because of `mermaid` syntax and used another diagram symbol...
    *  included `arint_version` as extra data in `mkdocs.yml` and used it in `index.md` doc as product version info
* 230822piu_h revived, tested links & updated from `230822piu_f` to `230822piu_g`
* 230822piu_g updated<br>
    (1) `810.46-Product_Features.md` ref section _ARINT own objects and components_ &<br>
    (2) `adma_catalog.md`<br>
    with link to `810-DSGN/810.03 System Data & Objects.md`
* 230822piu_f create as new `810-DSGN/810.03-System_Data_and_Objects.md`, updated `ROADMAP` doc




### 0.1.1-release product Features (230822 14:30)

* 230822piu_e revived, tested links & updated from `230822piu_b` to `230822piu_d`. published 230822 h14:30
* 230822piu_d update `810.46-Product_Features.md` ref:
    * new section ref "ARINT objects a d components"
    * finished section "Services level features"
    * ROADMAP `RMAP.001 - sys 1.0 doc manuals`
* 230822piu_c partial update `810.46-Product_Features.md` ref section "Services level features" listed frequent issues that system address in wrting services
* 230822piu_b raw update `810.46-Product_Features.md` ref section "Services level features" - left a HTML comment with intended text
* 230822piu_a revived, tested links & updated from `230821piu_a` to `230821piu_f`. published 230822 h06:20
* 230821piu_f _finish_ update `810.46-Product_Features.md` ref standards
* 230821piu_e _first raw_ update `810.46-Product_Features.md` ref standards
* 230821piu_d created new empty file for latter write:  `810-DSGN/120-CPTS-Request_Response_objects.md` and ref it in `mkdocs.ynl`
* 230821piu_c updated `index.md` with links in "Documentation" section
* 230821piu_b updated `130.02-Overview.md`, explain how can be addressed and high level operations
* 230821piu_a updated `130.02-Overview.md` doc to reflect new ARINT CORE




### 0.1.0-release new ALPHAREN CORE-Integrator (230820 19:00)

* 230820piu_k RENAME PROD TO ALPHAREN CORE-Integrator & RELEASE becomes the core platform for RENware Software Systems products **Microservices style***
* 230820piu_j updated product logo to reflect new "CORE Integrator"
* 230820piu_i updated `130.02-Overview.md` to start to reflect the new role os **ALPHAREN CORE**
* 230820piu_h updated `index.md` (About page) to clarify what copyright has RENware and what is 3rd party (ie, product "spare parts")
* 230820piu_g fixed some text bugs in `810-DSGN/130.02-Overview.md`
* 230820piu_f tested iss `230820piu_e` & fixed all pages with titles
* 230820piu_e linked iss `230820piu_d` files in `mkdocs.yml` and put TODO iss to make them in future versions
* 230820piu_d created new empty docs for future use as:
    * `130.04-Licensing_Editions_Pricing.md`
    * `130.05-Services.md`
    * `130.05-Training_Programmes.md`










# Archived CHANGELOGs

* [0.0 release](version_history/CHANGELOG_v0.0.md)


