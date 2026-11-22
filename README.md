> [![Awesome list badge](https://awesome.re/badge.svg)](https://awesome.re) A curated list of awesome open source technology for agriculture, farming and gardening. [Pull requests welcome!](https://github.com/open-ag/open-ag.github.io)

[Agriculture](https://en.wikipedia.org/wiki/Agriculture) is the science and art of cultivating plants and livestock for food and materials. This list covers open source robotics, hardware, data, modelling and software for farms and growers.

Contributions welcome! Please follow the [contributing guidelines](https://github.com/open-ag/awesome-agriculture/blob/master/contributing.md). Repos updated over a year ago can be found in [Legacy](https://github.com/open-ag/open-ag.github.io/blob/master/LEGACY.md) this is a fork of [Bryce Johnson list](https://github.com/brycejohnston/awesome-agriculture)

This list was improved using data from [this ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S277237552600969X).

## Contents

| Section | Subsections |
| :--- | :--- |
| [Data Standardisation, Interoperability and APIs](#data-standardisation-interoperability-and-apis) | [Data standards compared](#data-standards-compared) · [OADA](#oada-formats-and-api-tooling) · [OpenAgri services](#openagri-services) · [AgStack registries](#agstack-registries-and-infrastructure) · [ADAPT plugins](#adapt-framework-plugins-and-tools) · [ISOBUS](#isobus-iso-11783) · [Vendor API examples](#vendor-api-examples) · [Other tools](#other-tools-and-communities) |
| [Farm Management Systems and Record Keeping](#farm-management-systems-and-record-keeping) |  |
| [Automation and Robotics](#automation-and-robotics) |  |
| [Climate, Environment and Weather](#climate-environment-and-weather) |  |
| [Crop Modelling, Phenotyping and Pathology](#crop-modelling-phenotyping-and-pathology) |  |
| [Datasets](#datasets) |  |
| [Geospatial and GIS](#geospatial-and-gis) | [GIS Resources](#gis-resources) · [GIS Platforms](#gis-platforms) · [Shapefiles](#shapefiles) |
| [IoT, Hardware](#iot-hardware) | [General-purpose IoT platforms and components](#general-purpose-iot-platforms-and-components) |
| [Knowledgebases and Learning Resources](#knowledgebases-and-learning-resources) |  |
| [Machine Learning and AI](#machine-learning-and-ai) |  |
| [Remote Sensing and Imagery](#remote-sensing-and-imagery) |  |

## Data Standardisation, Interoperability and APIs

### Data standards compared

Three standards cover the farm side and one covers trade. SDM is generic IoT-style entities, ADAPT is machinery and field operations, OCSM is a semantic ontology, and DFC is supply-chain concepts. Overlap between them is small, so this is a choice of fit, not a ranking.

| Project | Scope | Format | Users |
| :--- | :--- | :--- | :--- |
| [dataModel.Agrifood](https://github.com/smart-data-models/dataModel.Agrifood)<br>![GitHub Repo stars](https://img.shields.io/github/stars/smart-data-models/dataModel.Agrifood?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/smart-data-models/dataModel.Agrifood)<br>Licence: none shown on repo page | Harmonised schemas for farms, parcels, crops, operations and greenhouse records | JSON Schema, JSON-LD context, NGSI-LD oriented | Run by the [Smart Data Models](https://github.com/smart-data-models) programme, led by [FIWARE Foundation](https://www.fiware.org), [TM Forum](https://www.tmforum.org), [IUDX](https://iudx.org.in) and [OASC](https://oascities.org). More than 80 organisations collaborate across all domains. The Agrifood README names UCO and SensoWave (Animal model, IoF2020 ShareBeef use case) |
| [Adapt Standard](https://github.com/AgGateway-ADAPT/Standard)<br>![GitHub Repo stars](https://img.shields.io/github/stars/AgGateway-ADAPT/Standard?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/AgGateway-ADAPT/Standard)<br>Licence: MIT | Farm reference data, field operations and geospatial layers, for B2B data sharing | JSON Schema | Backed by [AgGateway](https://www.aggateway.org) (ADAPT Oversight Committee). [AEF](https://www.aef-online.org) (the ISOBUS body) cooperates with AgGateway, with AEM, VDMA, AGCO, CLAAS, CNH and John Deere behind AEF. Cotton Inc. co-developed the cotton gin plugin |
| [OpenAgri-OCSM](https://github.com/agstack/OpenAgri-OCSM)<br>![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-OCSM?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-OCSM)<br>Licence: EUPL-1.2 (repo), CC BY 4.0 (model, per README) | OpenAgri Common Semantic Model, an ontology built on AIM and Ploutos CSM | RDF/OWL, JSON-LD, JSON Schema | Hosted by the [AgStack Foundation](https://www.linuxfoundation.org/press/agstack-becomes-key-player-in-openagri) (Linux Foundation). Developed in the [OpenAgri project](https://cordis.europa.eu/project/id/101134083) (Horizon Europe): [Maastricht University](https://www.maastrichtuniversity.nl) coordinates a consortium of 18 partners, including SCiO and Łukasiewicz-PIT. Built on DEMETER AIM and the Ploutos model |
| [Data Food Consortium](https://github.com/datafoodconsortium/standard)<br>![GitHub Repo stars](https://img.shields.io/github/stars/datafoodconsortium/standard?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/datafoodconsortium/standard)<br>Licence: AGPL-3 (ontology and UML repos; standard repo not checked) | Product, order and agent concepts for short food supply chains (trade, not production) | OWL/RDF ontology, JSON-LD, LDP endpoints | French multi-stakeholder initiative, started in 2017 by local food platforms: Open Food France, Cagette.net, Panier Local, La Ruche Qui Dit Oui, Ekylibre and Sony CSL. Later participants listed include Socleo, Elzeard, Mycelium, INRAE and Open Food Facts |

### OADA: formats and API tooling

The Open Ag Data Alliance, led by the Purdue Open Ag Technology Group, defines an API for sharing farm data plus JSON Schema formats for what travels over it. It is transport-oriented, not a domain model, and its backing is mostly legacy. The repos below are the formats, a reference server and client tools.

| Project | Description | Stars | Last commit |
| :--- | :--- | :--- | :--- |
| [formats](https://github.com/OADA/formats) | Simplified approach to OADA formats using JSON Schema | ![GitHub Repo stars](https://img.shields.io/github/stars/OADA/formats?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/OADA/formats) |
| [server](https://github.com/OADA/server) | Reference implementation of an OADA-conformant API server, TypeScript | ![GitHub Repo stars](https://img.shields.io/github/stars/OADA/server?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/OADA/server) |
| [cli](https://github.com/OADA/cli) | Pipeable OADA CLI client | ![GitHub Repo stars](https://img.shields.io/github/stars/OADA/cli?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/OADA/cli) |
| [oada-error-js](https://github.com/OADA/oada-error-js) | OADA standard error middleware | ![GitHub Repo stars](https://img.shields.io/github/stars/OADA/oada-error-js?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/OADA/oada-error-js) |
| [oadaify](https://github.com/OADA/oadaify) | Make OADA data nicer to work with in JS/TS | ![GitHub Repo stars](https://img.shields.io/github/stars/OADA/oadaify?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/OADA/oadaify) |

### OpenAgri services

OpenAgri is a Horizon Europe project (18 partners, coordinated by Maastricht University) building open-source farm management tools. OCSM is its data model. These repos are the services around it, so they only matter if you adopt the OpenAgri stack.

| Project | Description | Stars | Last commit |
| :--- | :--- | :--- | :--- |
| [OpenAgri-GateKeeper](https://github.com/agstack/OpenAgri-GateKeeper) | JWT-based authentication and access proxy | ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-GateKeeper?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-GateKeeper) |
| [OpenAgri-Bootstrap-Deployment](https://github.com/agstack/OpenAgri-Bootstrap-Deployment) | Modular configuration and deployment of all OpenAgri services | ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-Bootstrap-Deployment?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-Bootstrap-Deployment) |

### AgStack registries and infrastructure

AgStack is a Linux Foundation project that hosts shared agricultural infrastructure. The core piece is a registry that gives each field polygon a unique GeoID. The rest is identity, datastore and semantic tooling around it.

| Project | Description | Stars | Last commit |
| :--- | :--- | :--- | :--- |
| [asset-registry](https://github.com/agstack/asset-registry) | Registers a geospatial asset (typically a polygon) and returns a unique GeoID; Flask, AR 1.0 | ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/asset-registry?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/agstack/asset-registry) |
| [user-registry](https://github.com/agstack/user-registry) | User accounts, JWT issuance and API keys for AR 1.0 | ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/user-registry?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/agstack/user-registry) |
| [ar2](https://github.com/agstack/ar2) | Asset Registry 2: hub and spoke model | ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/ar2?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/agstack/ar2) |
| [ar2-hub](https://github.com/agstack/ar2-hub) | Hub component for Asset Registry 2 | ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/ar2-hub?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/agstack/ar2-hub) |
| [pancake](https://github.com/agstack/pancake) | AI-native geospatial datastore and DPI services: field ownership grants as SD-JWT credentials, signed audit ledger, scheduled vendor data ingestion | ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/pancake?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/agstack/pancake) |
| [semantic-croissant](https://github.com/agstack/semantic-croissant) | Semantic Croissant infrastructure, forked from codata/semantic-croissant | ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/semantic-croissant?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/agstack/semantic-croissant) |

### ADAPT Framework plugins and tools

ADAPT is AgGateway's open-source project: a standard data model plus a plugin framework that converts vendor formats to and from it. These are the plugins and a diagnostic tool, all C#.

| Project | Description | Stars | Last commit |
| :--- | :--- | :--- | :--- |
| [ISOv4Plugin](https://github.com/AgGateway-ADAPT/ISOv4Plugin) | ADAPT Framework plugin for ISOXML (ISO11783-10), C# | ![GitHub Repo stars](https://img.shields.io/github/stars/AgGateway-ADAPT/ISOv4Plugin?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/AgGateway-ADAPT/ISOv4Plugin) |
| [StandardPlugin](https://github.com/AgGateway-ADAPT/StandardPlugin) | ADAPT Framework plugin to convert data to the ADAPT Standard, C# | ![GitHub Repo stars](https://img.shields.io/github/stars/AgGateway-ADAPT/StandardPlugin?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/AgGateway-ADAPT/StandardPlugin) |
| [cotton-gin-data-plugin](https://github.com/AgGateway-ADAPT/cotton-gin-data-plugin) | ADAPT Framework import-only plugin for cotton gin data, developed with Cotton Inc., C# | ![GitHub Repo stars](https://img.shields.io/github/stars/AgGateway-ADAPT/cotton-gin-data-plugin?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/AgGateway-ADAPT/cotton-gin-data-plugin) |
| [ADAPT-Visualizer](https://github.com/AgGateway-ADAPT/ADAPT-Visualizer) | Windows Forms diagnostic tool for the ADAPT Framework, C# | ![GitHub Repo stars](https://img.shields.io/github/stars/AgGateway-ADAPT/ADAPT-Visualizer?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/AgGateway-ADAPT/ADAPT-Visualizer) |

### ISOBUS (ISO 11783)

ISO 11783 is the tractor-implement CAN bus standard. Open-Agriculture's AgIso projects are an open-source C++ stack and tooling for it. This is machine connectivity, not a data model, so it only matters if the robot must talk to implements.

| Project | Description | Stars | Last commit |
| :--- | :--- | :--- | :--- |
| [AgIsoStack-plus-plus](https://github.com/Open-Agriculture/AgIsoStack-plus-plus) | Free open-source C++ ISOBUS library (ISO11783/J1939 CAN stack), MIT | ![GitHub Repo stars](https://img.shields.io/github/stars/Open-Agriculture/AgIsoStack-plus-plus?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/Open-Agriculture/AgIsoStack-plus-plus) |
| [AgIsoVirtualTerminal](https://github.com/Open-Agriculture/AgIsoVirtualTerminal) | Experimental ISO11783-6 Virtual Terminal (VT) server GUI based on AgIsoStack++, C++ | ![GitHub Repo stars](https://img.shields.io/github/stars/Open-Agriculture/AgIsoVirtualTerminal?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/Open-Agriculture/AgIsoVirtualTerminal) |
| [AgIsoTerminalDesigner](https://github.com/Open-Agriculture/AgIsoTerminalDesigner) | Experimental GUI for designing and modifying VT object pools, Rust | ![GitHub Repo stars](https://img.shields.io/github/stars/Open-Agriculture/AgIsoTerminalDesigner?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/Open-Agriculture/AgIsoTerminalDesigner) |
| [AgIsoDDOPGenerator](https://github.com/Open-Agriculture/AgIsoDDOPGenerator) | Free ISO11783 DDOP editor based on AgIsoStack++, C++ | ![GitHub Repo stars](https://img.shields.io/github/stars/Open-Agriculture/AgIsoDDOPGenerator?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/Open-Agriculture/AgIsoDDOPGenerator) |
| [AgIsoDevelopmentTools](https://github.com/Open-Agriculture/AgIsoDevelopmentTools) | AgIso development tools, C++ | ![GitHub Repo stars](https://img.shields.io/github/stars/Open-Agriculture/AgIsoDevelopmentTools?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/Open-Agriculture/AgIsoDevelopmentTools) |

### Vendor API examples

Single-vendor sample code: OAuth2 clients for John Deere's API. Useful only if you integrate with Deere's platform.

| Project | Description | Stars | Last commit |
| :--- | :--- | :--- | :--- |
| [MyJohnDeereAPI-OAuth2-Java-Example](https://github.com/JohnDeere/MyJohnDeereAPI-OAuth2-Java-Example) | Java MyJohnDeere API client example | ![GitHub Repo stars](https://img.shields.io/github/stars/JohnDeere/MyJohnDeereAPI-OAuth2-Java-Example?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/JohnDeere/MyJohnDeereAPI-OAuth2-Java-Example) |
| [MyJohnDeereAPI-OAuth2-NodeJS-Example](https://github.com/JohnDeere/MyJohnDeereAPI-OAuth2-NodeJS-Example) | Node.js MyJohnDeere API client example | ![GitHub Repo stars](https://img.shields.io/github/stars/JohnDeere/MyJohnDeereAPI-OAuth2-NodeJS-Example?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/JohnDeere/MyJohnDeereAPI-OAuth2-NodeJS-Example) |

### Other tools and communities

Unrelated one-offs that fit nowhere else: a database engine, a botanical data crate, a Dutch government API connector and a community ecosystem.

| Project | Description | Stars | Last commit |
| :--- | :--- | :--- | :--- |
| [SawitDB](https://github.com/WowoEngine/SawitDB) | Node.js database engine built for data sovereignty | ![GitHub Repo stars](https://img.shields.io/github/stars/WowoEngine/SawitDB?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/WowoEngine/SawitDB) |
| [Botanica](https://github.com/Michael-A-Kuykendall/botanica) | Rust crate for botanical data management with taxonomic hierarchy, cultivation tracking and Darwin Core compliance | ![GitHub Repo stars](https://img.shields.io/github/stars/Michael-A-Kuykendall/botanica?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/Michael-A-Kuykendall/botanica) |
| [OpenTeam](https://openteam.community/) | Open technology ecosystem for agricultural management | n/a | n/a |
| [rvo-connector](https://github.com/SvenVw/rvo-connector) | npm package connecting to Dutch RVO government webservices. Needs a whitelisted IP and PKIoverheid or eHerkenning authentication. MIT. | ![GitHub Repo stars](https://img.shields.io/github/stars/SvenVw/rvo-connector?style=social) | ![GitHub last commit](https://img.shields.io/github/last-commit/SvenVw/rvo-connector) |


## Farm Management Systems and Record Keeping

| Project Name | Description |
| :--- | :--- |
| [HortusFox](https://github.com/danielbrendel/hortusfox-web) ![GitHub Repo stars](https://img.shields.io/github/stars/danielbrendel/hortusfox-web?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/danielbrendel/hortusfox-web) | Self-hosted, collaborative plant management and journaling app. |
| [farmOS](https://github.com/farmOS/farmOS) ![GitHub Repo stars](https://img.shields.io/github/stars/farmOS/farmOS?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/farmOS/farmOS) | Web-based farm record keeping application built with Drupal and PHP. |
| [Plant-it](https://github.com/MDeLuise/plant-it) ![GitHub Repo stars](https://img.shields.io/github/stars/MDeLuise/plant-it?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/MDeLuise/plant-it) | Self-hosted gardening companion app. |
| [Ekylibre](https://github.com/ekylibre/ekylibre) ![GitHub Repo stars](https://img.shields.io/github/stars/ekylibre/ekylibre?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/ekylibre/ekylibre) | Farm management information system for farmers and small enterprises, Ruby on Rails and PostgreSQL/PostGIS. |
| [LiteFarm](https://github.com/LiteFarmOrg/LiteFarm) ![GitHub Repo stars](https://img.shields.io/github/stars/LiteFarmOrg/LiteFarm?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/LiteFarmOrg/LiteFarm) | Community-led, not-for-profit farm management system. |
| [OpenAgri-FarmCalendar](https://github.com/agstack/OpenAgri-FarmCalendar) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-FarmCalendar?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-FarmCalendar) | Digital farm calendar for operations, observations, parcels and assets. |
| [inatrace-backend](https://github.com/agstack/inatrace-backend) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/inatrace-backend?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/inatrace-backend) | Java/Spring backend. |
| [OpenAgri-ReportingService](https://github.com/agstack/OpenAgri-ReportingService) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-ReportingService?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-ReportingService) | PDF report generation for agricultural data visualisation. |
| [GrowerHub](https://github.com/aspinozaxxx-lab/growerhub) ![GitHub Repo stars](https://img.shields.io/github/stars/aspinozaxxx-lab/growerhub?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/aspinozaxxx-lab/growerhub) | Greenhouse and small-farm management: Zigbee2MQTT monitoring, plant and watering journals, lighting and irrigation automation. |
| [tracefoodchain](https://github.com/agstack/tracefoodchain) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/tracefoodchain?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/tracefoodchain) | Flutter app and web app for tracing goods along food production chains. |
| [inatrace](https://github.com/agstack/inatrace) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/inatrace?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/inatrace) | Meta repository linking the INATrace backend, frontend, mobile and blockchain components; blockchain-based track and trace for supply chains. |
| [AgriOS](https://github.com/agstack/AgriOS) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/AgriOS?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/AgriOS) | Odoo 18 farm management addons: farmers, plots, trade and training (AGPL-3). |
| [Canopi](https://github.com/opencanopi/canopi) ![GitHub Repo stars](https://img.shields.io/github/stars/opencanopi/canopi?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/opencanopi/canopi) | Agroecological design for permaculture, syntropic agriculture and food forests, with a plant catalog and geolocated map canvas. Rust and TypeScript, AGPL-3.0. |
| [inatrace-coffee-network](https://github.com/agstack/inatrace-coffee-network) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/inatrace-coffee-network?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/inatrace-coffee-network) | Blockchain smart contracts for the coffee supply chain. |
| [inatrace-frontend](https://github.com/agstack/inatrace-frontend) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/inatrace-frontend?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/inatrace-frontend) | Angular frontend. |
| [inatrace-mobile](https://github.com/agstack/inatrace-mobile) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/inatrace-mobile?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/inatrace-mobile) | Mobile app for farmer data collection. |
| [Open Food Network](https://github.com/openfoodfoundation/openfoodnetwork) ![GitHub Repo stars](https://img.shields.io/github/stars/openfoodfoundation/openfoodnetwork?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/openfoodfoundation/openfoodnetwork) | Marketplace platform for local food enterprises, in production since 2012 with regional affiliates. Ruby on Rails and PostgreSQL, AGPL-3.0. |
| [FarmMaps (Akkerweb)](https://git.akkerweb.nl/explore/repos) | Web-based farm management platform with open code repositories under various licences. Relies on cloud storage and processing. |
| [Prescription Map Editor](https://github.com/Eden-Library-AI/openagri_prescription_map_editor) ![GitHub Repo stars](https://img.shields.io/github/stars/Eden-Library-AI/openagri_prescription_map_editor?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Eden-Library-AI/openagri_prescription_map_editor) | Offline desktop tool for editing variable-rate prescription maps, from the OpenAgri project. MIT. |
| [SFS SmartFeed Backend](https://github.com/inokron-doo/OA-Cloud-Backend) ![GitHub Repo stars](https://img.shields.io/github/stars/inokron-doo/OA-Cloud-Backend?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/inokron-doo/OA-Cloud-Backend) | Backend for SmartFeed livestock feed monitoring: IoT telemetry, predictive analytics and alerts. AGPL-3.0. |
| [SFS SmartFeed Web App](https://github.com/inokron-doo/OA-Cloud-Frontend) ![GitHub Repo stars](https://img.shields.io/github/stars/inokron-doo/OA-Cloud-Frontend?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/inokron-doo/OA-Cloud-Frontend) | React, TypeScript and Vite dashboard for SmartFeed monitoring and analytics. GPL-3.0. |
| [OpenAgri reporting templates](https://github.com/Agrobitsrl/reporting-templates) ![GitHub Repo stars](https://img.shields.io/github/stars/Agrobitsrl/reporting-templates?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Agrobitsrl/reporting-templates) | Converts JSON inputs into formatted compliance, sustainability and operational reports for PGI and DPO products. Apache-2.0. |



## Automation and Robotics

| Project Name | Description |
| :--- | :--- |
| [farmbot_os](https://github.com/FarmBot/farmbot_os) ![GitHub Repo stars](https://img.shields.io/github/stars/FarmBot/farmbot_os?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/FarmBot/farmbot_os) | Embedded OS handling motor axes, watering tools and sensors on FarmBot hardware. |
| [Farmbot-Web-App](https://github.com/FarmBot/Farmbot-Web-App) ![GitHub Repo stars](https://img.shields.io/github/stars/FarmBot/Farmbot-Web-App?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/FarmBot/Farmbot-Web-App) | Setup, customize and control FarmBot from any device, TypeScript. |
| [Fields2Cover](https://github.com/Fields2Cover/Fields2Cover) ![GitHub Repo stars](https://img.shields.io/github/stars/Fields2Cover/Fields2Cover?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Fields2Cover/Fields2Cover) | Robust and efficient coverage paths for autonomous agricultural vehicles. |
| [OpenWeedLocator](https://github.com/geezacoleman/OpenWeedLocator) ![GitHub Repo stars](https://img.shields.io/github/stars/geezacoleman/OpenWeedLocator?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/geezacoleman/OpenWeedLocator) | Low-cost, image-based weed detection device for in-crop and fallow scenarios. |
| [farmbot-arduino-firmware](https://github.com/FarmBot/farmbot-arduino-firmware) ![GitHub Repo stars](https://img.shields.io/github/stars/FarmBot/farmbot-arduino-firmware?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/FarmBot/farmbot-arduino-firmware) | Arduino firmware executing g-code like commands over serial to move the FarmBot and operate the tool mount. |
| [rosys](https://github.com/zauberzeug/rosys) ![GitHub Repo stars](https://img.shields.io/github/stars/zauberzeug/rosys?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/zauberzeug/rosys) | Asynchronous Python framework for web GUI and state handling on mobile robots, used for field rovers. |
| [farmbot-js](https://github.com/FarmBot/farmbot-js) ![GitHub Repo stars](https://img.shields.io/github/stars/FarmBot/farmbot-js?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/FarmBot/farmbot-js) | JavaScript wrapper for FarmBot's authentication and RPC instructions. |
| [Sowbot](https://github.com/Agroecology-Lab/feldfreund_devkit_ros) ![GitHub Repo stars](https://img.shields.io/github/stars/Agroecology-Lab/feldfreund_devkit_ros?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Agroecology-Lab/feldfreund_devkit_ros) | Line-following sowing and weeding robot with some web UI tools. |
| [lizard](https://github.com/zauberzeug/lizard) ![GitHub Repo stars](https://img.shields.io/github/stars/zauberzeug/lizard?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/zauberzeug/lizard) | Domain-specific language for real-time motor control and E-stop logic on microcontrollers. |
| [trellis](https://github.com/agtonomy/trellis) ![GitHub Repo stars](https://img.shields.io/github/stars/agtonomy/trellis?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agtonomy/trellis) | General-purpose middleware framework for distributed applications, by Agtonomy. Not ROS-based. |
| [amiga-dev-kit](https://github.com/farm-ng/amiga-dev-kit) ![GitHub Repo stars](https://img.shields.io/github/stars/farm-ng/amiga-dev-kit?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/farm-ng/amiga-dev-kit) | Development kit for third-party hardware and software extensions to the farm-ng Amiga rover. |
| [farmbot-py](https://github.com/FarmBot/farmbot-py) ![GitHub Repo stars](https://img.shields.io/github/stars/FarmBot/farmbot-py?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/FarmBot/farmbot-py) | Authentication and communication utilities for FarmBot, Python. |
| [feldfreund_devkit](https://github.com/zauberzeug/feldfreund_devkit) ![GitHub Repo stars](https://img.shields.io/github/stars/zauberzeug/feldfreund_devkit?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/zauberzeug/feldfreund_devkit) | Development platform for autonomous weeding. |
| [librcom](https://github.com/romi/librcom) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/librcom?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/librcom) | ROMI rcom library, C++. |
| [romitask](https://github.com/romi/romitask) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/romitask?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/romitask) | ROMI task runner, a Luigi based task pipeline. |
| [bonsai-sdk](https://github.com/BonsaiRobotics/bonsai-sdk) ![GitHub Repo stars](https://img.shields.io/github/stars/BonsaiRobotics/bonsai-sdk?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/BonsaiRobotics/bonsai-sdk) | SDK for interacting with the Bonsai Robotics Amiga through ROS 2. |
| [romi-apps](https://github.com/romi/romi-apps) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/romi-apps?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/romi-apps) | Applications for the ROMI system: CNC, camera, gimbal, cablebot, rover. |
| [FarmBot-ROS](https://github.com/farmbot-ros/) | Open source farming robot. |
| [JABAS.AI](https://github.com/jabasai) | ROS 2 repositories including graph-based topological navigation for crop-row layouts. |
| [FarmBot Genesis docs](https://github.com/FarmBot-Docs/farmbot-genesis) ![GitHub Repo stars](https://img.shields.io/github/stars/FarmBot-Docs/farmbot-genesis?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/FarmBot-Docs/farmbot-genesis) | Hardware documentation for the FarmBot Genesis and Genesis XL machines. |
| [DJI Payload SDK](https://github.com/dji-sdk/Payload-SDK) ![GitHub Repo stars](https://img.shields.io/github/stars/dji-sdk/Payload-SDK?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/dji-sdk/Payload-SDK) | SDK for building custom payloads for DJI drones. MIT. |

## Climate, Environment and Weather

| Project Name | Description |
| :--- | :--- |
| [iem](https://github.com/akrherz/iem) ![GitHub Repo stars](https://img.shields.io/github/stars/akrherz/iem?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/akrherz/iem) | Code that makes the Iowa Environmental Mesonet run. |
| [pyTSEB](https://github.com/hectornieto/pyTSEB) ![GitHub Repo stars](https://img.shields.io/github/stars/hectornieto/pyTSEB?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/hectornieto/pyTSEB) | Python two-source energy balance model for estimating evapotranspiration from remote sensing data. |
| [frostline](https://github.com/waldoj/frostline) ![GitHub Repo stars](https://img.shields.io/github/stars/waldoj/frostline?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/waldoj/frostline) | Dataset, API and Python parser for USDA plant hardiness zones. |
| [soilDB](https://github.com/ncss-tech/soilDB) ![GitHub Repo stars](https://img.shields.io/github/stars/ncss-tech/soilDB?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/ncss-tech/soilDB) | R library for simplified access to NCSS soil databases. |
| [GSODR](https://github.com/ropensci/GSODR) ![GitHub Repo stars](https://img.shields.io/github/stars/ropensci/GSODR?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/ropensci/GSODR) | Global summary daily weather data in R. |
| [OpenAgri-WeatherService](https://github.com/agstack/OpenAgri-WeatherService) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-WeatherService?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-WeatherService) | Weather forecasts and critical agricultural indicators. |
| [OpenAgri-IrrigationManagement](https://github.com/agstack/OpenAgri-IrrigationManagement) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-IrrigationManagement?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-IrrigationManagement) | Evapotranspiration calculations and soil moisture analysis. |
| [Open-Meteo](https://github.com/open-meteo/open-meteo) ![GitHub Repo stars](https://img.shields.io/github/stars/open-meteo/open-meteo?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/open-meteo/open-meteo) | Weather forecast API with a free public instance. AGPL-3.0. |
| [WeeWX](https://github.com/weewx/weewx) ![GitHub Repo stars](https://img.shields.io/github/stars/weewx/weewx?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/weewx/weewx) | Software for logging, archiving and publishing data from personal weather stations. GPL-3.0. |

## Crop Modelling, Phenotyping and Pathology

| Project Name | Description |
| :--- | :--- |
| [PCSE](https://github.com/ajwdewit/pcse) ![GitHub Repo stars](https://img.shields.io/github/stars/ajwdewit/pcse?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/ajwdewit/pcse) | Python environment for running crop growth and production models. |
| [DSSAT](https://github.com/DSSAT/dssat-csm-os) ![GitHub Repo stars](https://img.shields.io/github/stars/DSSAT/dssat-csm-os?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/DSSAT/dssat-csm-os) | Cropping-system simulations across crops, soils, weather and management, Fortran. |
| [ApsimX](https://github.com/APSIMInitiative/ApsimX) ![GitHub Repo stars](https://img.shields.io/github/stars/APSIMInitiative/ApsimX?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/APSIMInitiative/ApsimX) | Next-generation APSIM framework for agricultural system simulations, C#. |
| [AquaCrop](https://github.com/aquacropos/aquacrop) ![GitHub Repo stars](https://img.shields.io/github/stars/aquacropos/aquacrop?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/aquacropos/aquacrop) | Python implementation of AquaCrop-OS for crop growth and water use. |
| [plant-3d-vision](https://github.com/romi/plant-3d-vision) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/plant-3d-vision?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/plant-3d-vision) | Digital reconstruction and phenotypic quantification of plant phyllotaxis. |
| [plant-3d-explorer](https://github.com/romi/plant-3d-explorer) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/plant-3d-explorer?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/plant-3d-explorer) | Browser application to visualise 3D scanned plants. |
| [romicgal](https://github.com/romi/romicgal) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/romicgal?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/romicgal) | Python CGAL bindings for skeletonisation. |
| [skeleton_refinement](https://github.com/romi/skeleton_refinement) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/skeleton_refinement?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/skeleton_refinement) | Plant skeleton optimisation using a stochastic framework on point cloud data. |
| [plant-imager](https://github.com/romi/plant-imager) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/plant-imager?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/plant-imager) | Library controlling the PlantImager (hardware) or the VirtualPlantImager (Blender) to acquire images of single potted plants. |
| [plantdb](https://github.com/romi/plantdb) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/plantdb?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/plantdb) | Database to host and serve images and processed data. |
| [Awesome Crop Models](https://github.com/YuanyuanMa03/awesome-crop-models) ![GitHub Repo stars](https://img.shields.io/github/stars/YuanyuanMa03/awesome-crop-models?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/YuanyuanMa03/awesome-crop-models) | Curated list of open source crop models, process models, tools, applications and data-driven models. |
| [opensource-pestmodels](https://github.com/agstack/opensource-pestmodels) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/opensource-pestmodels?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/opensource-pestmodels) | Hierarchical pest and disease modelling framework (13 models, 19 crops, 54 threats) with Python wheel, FastAPI and MCP server. |
| [Plant-Imager3](https://github.com/romi/Plant-Imager3) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/Plant-Imager3?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/Plant-Imager3) | Plant imager software, Python. |
| [Open Plant Pathology](https://www.openplantpathology.org/) ([GitHub organisation](https://github.com/openplantpathology)) | Community for open data and computational tools in epidemiology and pathogen population biology and ecology. |
| [OpenAgri pest and disease management](https://github.com/openagri-eu/pest-and-disease-management) ![GitHub Repo stars](https://img.shields.io/github/stars/openagri-eu/pest-and-disease-management?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/openagri-eu/pest-and-disease-management) | Growing degree day and pest risk calculations, from the OpenAgri project. EUPL-1.2. |
| [iAgro PDM fuzzy model](https://github.com/Agrobitsrl/PDM-fuzzymodel) ![GitHub Repo stars](https://img.shields.io/github/stars/Agrobitsrl/PDM-fuzzymodel?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Agrobitsrl/PDM-fuzzymodel) | Fuzzy-logic model forecasting crop pest and disease pressure under changing environmental conditions. Apache-2.0. |
| [FD-freezinginjury](https://github.com/Agrobitsrl/FD-freezinginjury) ![GitHub Repo stars](https://img.shields.io/github/stars/Agrobitsrl/FD-freezinginjury?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Agrobitsrl/FD-freezinginjury) | Frost injury alert model that assesses crop vulnerability by growth stage and temperature. Apache-2.0. |

## Datasets

| Project Name | Description |
| :--- | :--- |
| [Agriculture Datasets Collection](https://lacunafund.org/datasets/agriculture/) | Curated machine learning datasets addressing food security in developing regions. |
| [CEAOD](https://ceaod.github.io/) ([GitHub repository](https://github.com/CEAOD/Data)) ![GitHub Repo stars](https://img.shields.io/github/stars/CEAOD/Data?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/CEAOD/Data) | Controlled Environment Agriculture Open Data: standardised greenhouse and indoor farming datasets with analysis tools. |
| **[digital-agriculture-datasets](https://github.com/Agroecology-Lab/digital-agriculture-datasets)** ![GitHub Repo stars](https://img.shields.io/github/stars/Agroecology-Lab/digital-agriculture-datasets?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Agroecology-Lab/digital-agriculture-datasets) | Open datasets for training and benchmarking AI and robotic systems in agriculture and off-road environments. |
| [FAO/NASA Harvest Crop Type Dataset](https://data.harvestportal.org/dataset/fao-bha-nasa-harvest-public-crop-type-datasets) | Ground truth crop type observations with geolocated field data for training and validating cropland classification models. |
| [Growstuff](https://www.growstuff.org/crops) ([GitHub repository](https://github.com/Growstuff/growstuff)) ![GitHub Repo stars](https://img.shields.io/github/stars/Growstuff/growstuff?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Growstuff/growstuff) | Record keeping and crop database with a good API. |
| [PlantVillage](https://www.kaggle.com/datasets/emmarex/plantdisease) | Leaf images of healthy and diseased plants, 38 disease classes across 14 crops. |
| [TERRA REF](https://terraref.org) ([GitHub organisation](https://github.com/terraref)) | 1 PB of public domain, high resolution sensor data from sorghum breeding trials. [Data publication](https://doi.org/10.5061/dryad.4b8gtht99), with large files on [Globus](https://app.globus.org/file-manager?origin_id=e8feaff4-96cd-11ea-bf90-0e6cccbb0103&origin_path=%2F) (ncsa#terra-public). |
| [US Farmers Market Statistics 2026](https://datahub.io/harvestlymarkets/us-farmers-markets-dataset) | USDA-derived farmers market statistics, CC BY 4.0. |
| [USDA Market Prices](https://github.com/JuanTorresMI/JuanTorresMI.github.io) ![GitHub Repo stars](https://img.shields.io/github/stars/JuanTorresMI/JuanTorresMI.github.io?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/JuanTorresMI/JuanTorresMI.github.io) | Daily boxed beef, pork and fed cattle prices from USDA AMS price reports since 2020, downloadable as CSV. |
| [VarshaKrishi Field NDVI](https://github.com/tanmaysahare/sentinel2-field-ndvi) ![GitHub Repo stars](https://img.shields.io/github/stars/tanmaysahare/sentinel2-field-ndvi?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/tanmaysahare/sentinel2-field-ndvi) | One year of Sentinel-2 L2A field-mean NDVI for a field near Katol, Nagpur, India, with cloud verdict and haze flag per pass. CSV and JSON, CC BY 4.0. |
| [OpenAgri Vineyard Image Dataset](https://zenodo.org/records/19698544) | Annotated vineyard imagery for yield estimation, disease detection and canopy analysis. The same record holds YOLO-based models for grape-cluster, disease and vigour detection. |
| [Annual Composting Cycle](https://zenodo.org/records/18984012) | Time-series sensor measurements from two compost piles during fermentation. |
| [Somatic Cell Count](https://doi.org/10.5281/zenodo.22748856) | Somatic cell count records and metadata for dairy health and mastitis monitoring. |
| [Estrus detection](https://doi.org/10.5281/zenodo.22748342) | Estrus observations and metadata for reproductive-status classification. |
| [SCIBee Honeybee Entrance Corridor Image Dataset](https://ieee-dataport.org/documents/scibee-honeybee-entrance-corridor-image-dataset-object-detection-precision-beekeeping) | 1,879 field images of honeybees in a hive entrance corridor, annotated with COCO-format bounding boxes. |



## Geospatial and GIS

### GIS Resources

| Project Name | Description |
| :--- | :--- |
| [Awesome GIS](https://github.com/sshuair/awesome-gis) ![GitHub Repo stars](https://img.shields.io/github/stars/sshuair/awesome-gis?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/sshuair/awesome-gis) | Curated list of GIS related sources. |

### GIS Platforms

| Project Name | Description |
| :--- | :--- |
| [QGIS](https://qgis.org) ([GitHub repository](https://github.com/qgis/QGIS)) ![GitHub Repo stars](https://img.shields.io/github/stars/qgis/QGIS?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/qgis/QGIS) | Free, open source, cross-platform (Linux, Windows, macOS) geographic information system. |
| [GeoServer](https://github.com/geoserver/geoserver) ![GitHub Repo stars](https://img.shields.io/github/stars/geoserver/geoserver?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/geoserver/geoserver) | Java server for sharing geospatial data. OGC reference implementation for WFS and WCS and a certified compliant WMS. GPL-2.0. |
| [HSLayers NG](https://github.com/hslayers/hslayers-ng) ![GitHub Repo stars](https://img.shields.io/github/stars/hslayers/hslayers-ng?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/hslayers/hslayers-ng) | Angular web mapping libraries and ready-made application bundles, with Cesium and sensor modules. MIT. |

### Shapefiles

| Project Name | Description |
| :--- | :--- |
| [pyshp](https://github.com/GeospatialPython/pyshp) ![GitHub Repo stars](https://img.shields.io/github/stars/GeospatialPython/pyshp?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/GeospatialPython/pyshp) | Reads and writes ESRI Shapefiles in pure Python. |

## IoT, Hardware

| Project Name | Description |
| :--- | :--- |
| [AgOpenGPS](https://github.com/AgOpenGPS-Official/AgOpenGPS) ![GitHub Repo stars](https://img.shields.io/github/stars/AgOpenGPS-Official/AgOpenGPS?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/AgOpenGPS-Official/AgOpenGPS) | Precision mapping and section control software. |
| [Farm Hack](https://farmhack.org/tools) | Worldwide community of farmers who build and modify their own tools. |
| [Farm-Data-Relay-System](https://github.com/timmbogner/Farm-Data-Relay-System) ![GitHub Repo stars](https://img.shields.io/github/stars/timmbogner/Farm-Data-Relay-System?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/timmbogner/Farm-Data-Relay-System) | Transports sensor data in remote areas over ESP-NOW, LoRa and other protocols, without WiFi. |
| [Open hydroponics](https://openhydroponics.com/) | Fully automated hydroponic OS. |
| [romi-bldc-controller](https://github.com/romi/romi-bldc-controller) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/romi-bldc-controller?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/romi-bldc-controller) | Arduino firmware to control brushless motors, based on SimpleFOC. |
| [Simplesteer](https://github.com/matmis/simplesteer) ![GitHub Repo stars](https://img.shields.io/github/stars/matmis/simplesteer?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/matmis/simplesteer) | RTK GPS tractor autosteer with a web interface controllable from a smartphone; runs on a Raspberry Pi. |
| [SIP (Sustainable Irrigation Platform)](https://github.com/Dan-in-CA/SIP) ![GitHub Repo stars](https://img.shields.io/github/stars/Dan-in-CA/SIP?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Dan-in-CA/SIP) | Irrigation controller with local decision-making that works fully offline. GPL. |
| [OpenSprinkler App](https://github.com/OpenSprinkler/OpenSprinkler-App) ![GitHub Repo stars](https://img.shields.io/github/stars/OpenSprinkler/OpenSprinkler-App?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/OpenSprinkler/OpenSprinkler-App) | Mobile and web app for the OpenSprinkler irrigation controller. Works locally, with optional cloud features. GPL-3.0. |
| [Pirrigo](https://github.com/vacovsky/pirrigo) ![GitHub Repo stars](https://img.shields.io/github/stars/vacovsky/pirrigo?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/vacovsky/pirrigo) | Go and Angular irrigation controller with zones, calendar, scheduler, run history and analytics. Needs no connectivity. MIT. |
| [Irrigation-Pi](https://github.com/max-pfeiffer/irrigation-pi) ![GitHub Repo stars](https://img.shields.io/github/stars/max-pfeiffer/irrigation-pi?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/max-pfeiffer/irrigation-pi) | Raspberry Pi irrigation monitoring that runs offline, with automated tests and versioned releases. MIT. |
| [OpenAgri Smart Irrigation Controller](https://gitlab.pcss.pl/openagri/openagri-smartirrigationcontroller) | Edge irrigation controller from the OpenAgri project, designed for farms with weak or no connectivity. EUPL-1.2. |
| [OpenAgri SensorNode](https://ligit.pit.lukasiewicz.gov.pl/openagri/openagri_sensornode) | Edge sensor node from the OpenAgri project, built for remote and weak-connectivity sites. EUPL-1.2. |
| [raspberrypi-m350-enclosure](https://github.com/ilvo-openagri/raspberrypi-m350-enclosure) ![GitHub Repo stars](https://img.shields.io/github/stars/ilvo-openagri/raspberrypi-m350-enclosure?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/ilvo-openagri/raspberrypi-m350-enclosure) | 3D-printed enclosure for the edge hardware on the OpenAgri UAV-based detection prototype. EUPL-1.2. |
| [Anavi Gardening uHAT](https://github.com/AnaviTechnology/anavi-docs/tree/main/anavi-gardening-uhat) ![GitHub Repo stars](https://img.shields.io/github/stars/AnaviTechnology/anavi-docs?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/AnaviTechnology/anavi-docs) | Documentation for the ANAVI Gardening uHAT, a Raspberry Pi add-on board for gardening. Badges show the wider anavi-docs repository. CC-BY-4.0. |
| [MoniCompost](https://github.com/GreenSupplyChain-DIH/monicompost) ![GitHub Repo stars](https://img.shields.io/github/stars/GreenSupplyChain-DIH/monicompost?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/GreenSupplyChain-DIH/monicompost) | Compost monitoring and reasoning from temperature, moisture and oxygen data, recommending management actions. Alerts and farm calendar integration are still roadmap items. Apache-2.0. |
| [SCIBee](https://github.com/mechatronery/scibee) ![GitHub Repo stars](https://img.shields.io/github/stars/mechatronery/scibee?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/mechatronery/scibee) | Beekeeping platform: infrared bee-traffic counting, motorised entrance control, ESP32-S3 camera capture for Varroa analysis, hive weighing and automated formic-acid treatment. Includes a locally hosted LLM evaluator and a community data hub. Apache-2.0. |
| [MOSIC](https://github.com/altsol/mosic) ![GitHub Repo stars](https://img.shields.io/github/stars/altsol/mosic?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/altsol/mosic) | Modular open-source irrigation controller for monitoring and controlling precision irrigation systems. EUPL-1.2. |
| [SFS LoRa Concentrator firmware](https://github.com/inokron-doo/OA-Concentrator) ![GitHub Repo stars](https://img.shields.io/github/stars/inokron-doo/OA-Concentrator?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/inokron-doo/OA-Concentrator) | SmartFeed gateway firmware that aggregates LoRa sensor telemetry and forwards it to SmartFeed services. GPL-3.0. |
| [SFS LoRa Sensor Node firmware](https://github.com/inokron-doo/OA-Sensor) ![GitHub Repo stars](https://img.shields.io/github/stars/inokron-doo/OA-Sensor?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/inokron-doo/OA-Sensor) | SmartFeed node firmware monitoring feed level, temperature and humidity. GPL-3.0. |
| [SFS LoRa node hardware](https://github.com/inokron-doo/OA-HWcomponents) ![GitHub Repo stars](https://img.shields.io/github/stars/inokron-doo/OA-HWcomponents?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/inokron-doo/OA-HWcomponents) | SmartFeed LoRa node design for feed-level and microclimate monitoring. CERN-OHL-S-2.0. |
| [SFS SmartFeed edge processing](https://github.com/inokron-doo/OA-LocalNodeREDsetup) ![GitHub Repo stars](https://img.shields.io/github/stars/inokron-doo/OA-LocalNodeREDsetup?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/inokron-doo/OA-LocalNodeREDsetup) | Node-RED setup that collects and processes on-farm feed and environmental data, with local storage and cloud synchronisation. GPL-3.0. |

### General-purpose IoT platforms and components

Not agriculture-specific. These are the generic middleware, databases, LoRaWAN servers and boards that other projects here are built on.

| Project Name | Description |
| :--- | :--- |
| [FIWARE catalogue](https://github.com/FIWARE/catalogue) ![GitHub Repo stars](https://img.shields.io/github/stars/FIWARE/catalogue?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/FIWARE/catalogue) | Index of FIWARE generic enablers, including the IoT Agent device management components. |
| [Orion](https://github.com/telefonicaid/fiware-orion) ![GitHub Repo stars](https://img.shields.io/github/stars/telefonicaid/fiware-orion?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/telefonicaid/fiware-orion) | FIWARE context broker for managing context information. Self-hosted, AGPL-3.0. |
| [Keyrock](https://github.com/ging/fiware-idm) ![GitHub Repo stars](https://img.shields.io/github/stars/ging/fiware-idm?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/ging/fiware-idm) | FIWARE identity management enabler, maintained by Universidad Politécnica de Madrid. MIT. |
| [EdgeX Foundry](https://github.com/edgexfoundry/) | LF Edge middleware for edge device interoperability that runs without a cloud dependency. Apache-2.0. |
| [eKuiper](https://github.com/lf-edge/ekuiper) ![GitHub Repo stars](https://img.shields.io/github/stars/lf-edge/ekuiper?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/lf-edge/ekuiper) | Lightweight stream processing and rules engine for edge devices, from LF Edge. Apache-2.0. |
| [NanoMQ](https://github.com/nanomq/nanomq) ![GitHub Repo stars](https://img.shields.io/github/stars/nanomq/nanomq?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/nanomq/nanomq) | Lightweight MQTT broker for edge deployments. MIT. |
| [Zenoh](https://github.com/eclipse-zenoh/zenoh) ![GitHub Repo stars](https://img.shields.io/github/stars/eclipse-zenoh/zenoh?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/eclipse-zenoh/zenoh) | Pub/sub and query middleware spanning edge and cloud, from the Eclipse Foundation. Apache-2.0. |
| [ChirpStack](https://github.com/chirpstack/chirpstack) ![GitHub Repo stars](https://img.shields.io/github/stars/chirpstack/chirpstack?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/chirpstack/chirpstack) | LoRaWAN network server. MIT. |
| [The Things Stack](https://github.com/TheThingsNetwork/lorawan-stack) ![GitHub Repo stars](https://img.shields.io/github/stars/TheThingsNetwork/lorawan-stack?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/TheThingsNetwork/lorawan-stack) | LoRaWAN network server from The Things Industries. Apache-2.0. |
| [ThingsBoard](https://github.com/thingsboard/thingsboard) ![GitHub Repo stars](https://img.shields.io/github/stars/thingsboard/thingsboard?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/thingsboard/thingsboard) | IoT platform with device management, dashboards and a rule engine. The Community Edition can run on a local network. Apache-2.0. |
| [Node-RED](https://github.com/node-red/node-red) ![GitHub Repo stars](https://img.shields.io/github/stars/node-red/node-red?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/node-red/node-red) | Flow-based tool for wiring together devices, APIs and services. OpenJS Foundation project. MIT. |
| [Ryax engine](https://github.com/RyaxTech/ryax-engine) ![GitHub Repo stars](https://img.shields.io/github/stars/RyaxTech/ryax-engine?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/RyaxTech/ryax-engine) | Event-driven workflow engine for Kubernetes. The GitHub repository is a read-only mirror of the main GitLab repository. MPL-2.0. |
| [InfluxDB](https://github.com/influxdata/influxdb) ![GitHub Repo stars](https://img.shields.io/github/stars/influxdata/influxdb?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/influxdata/influxdb) | Time-series database you can self-host. Not agriculture-specific. Apache-2.0 and MIT. |
| [Grafana](https://github.com/grafana/grafana) ![GitHub Repo stars](https://img.shields.io/github/stars/grafana/grafana?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/grafana/grafana) | Dashboards and monitoring for data from many sources. Not agriculture-specific. AGPL-3.0. |
| [Prometheus](https://github.com/prometheus/prometheus) ![GitHub Repo stars](https://img.shields.io/github/stars/prometheus/prometheus?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/prometheus/prometheus) | Self-hosted monitoring and alerting toolkit. Not agriculture-specific. Apache-2.0. |
| [MongoDB](https://github.com/mongodb/mongo) ![GitHub Repo stars](https://img.shields.io/github/stars/mongodb/mongo?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/mongodb/mongo) | Document database. Source-available under the SSPL, which is not an OSI-approved licence. Not agriculture-specific. |
| [DepthAI RGB camera board (BG0249)](https://github.com/luxonis/depthai-hardware/tree/master/BG0249_DepthAI_RGB_Camera) ![GitHub Repo stars](https://img.shields.io/github/stars/luxonis/depthai-hardware?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/luxonis/depthai-hardware) | Open design files for a Luxonis DepthAI RGB camera board from the OAK range. MIT. |
| [nRF Connect SDK](https://github.com/nrfconnect/sdk-nrf) ![GitHub Repo stars](https://img.shields.io/github/stars/nrfconnect/sdk-nrf?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/nrfconnect/sdk-nrf) | SDK for Nordic Semiconductor wireless chips. Uses the Nordic 5-Clause licence, not a standard open source licence. |

## Knowledgebases and Learning Resources

| Project Name | Description |
| :--- | :--- |
| [romi-robots-docs](https://github.com/romi/romi-robots-docs) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/romi-robots-docs?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/romi-robots-docs) | Source of the ROMI documentation at docs.romi-project.eu. |
| [Trefle](https://github.com/treflehq/trefle-api) ![GitHub Repo stars](https://img.shields.io/github/stars/treflehq/trefle-api?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/treflehq/trefle-api) | Plant data API. |

## Machine Learning and AI

| Project Name | Description |
| :--- | :--- |
| [AgML](https://github.com/Project-AgML/AgML) ![GitHub Repo stars](https://img.shields.io/github/stars/Project-AgML/AgML?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Project-AgML/AgML) | Centralised framework for agricultural machine learning. |
| [agridat](https://github.com/kwstat/agridat) ![GitHub Repo stars](https://img.shields.io/github/stars/kwstat/agridat?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/kwstat/agridat) | R package with an extensive collection of datasets from agricultural experiments. |
| [AgriQuant-AI](https://github.com/AgriQuantAI/AgriQuant-AI) ![GitHub Repo stars](https://img.shields.io/github/stars/AgriQuantAI/AgriQuant-AI?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/AgriQuantAI/AgriQuant-AI) | AI-powered weather intelligence for agricultural commodity futures, Python. |
| [AI Segmentation](https://plugins.qgis.org/plugins/AI_Segmentation) | QGIS plugin by TerraLab for AI-based segmentation. |
| [FarmVibes.AI](https://github.com/microsoft/farmvibes-ai) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/farmvibes-ai?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/microsoft/farmvibes-ai) | Multimodal geospatial ML models for agriculture and sustainability. |
| [palefire](https://github.com/agstack/palefire) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/palefire?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/palefire) | LLM and knowledge graph integration framework. |
| [PlantCV](https://github.com/danforthcenter/plantcv) ![GitHub Repo stars](https://img.shields.io/github/stars/danforthcenter/plantcv?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/danforthcenter/plantcv) | Plant phenotyping software using computer vision. |
| [romiseg](https://github.com/romi/romiseg) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/romiseg?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/romiseg) | Virtual plant segmentation from 2D images generated by the virtual scanner, using neural networks (PyTorch). |
| [Insect Detect](https://github.com/maxsitt/insect-detect) ![GitHub Repo stars](https://img.shields.io/github/stars/maxsitt/insect-detect?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/maxsitt/insect-detect) | Camera system for automated insect monitoring, with DIY hardware, documentation and a 2024 PLOS ONE paper. GPL-3.0. |
| [Colorado beetle detection model](https://github.com/ilvo-openagri/colorado-beetle-detection-model) ![GitHub Repo stars](https://img.shields.io/github/stars/ilvo-openagri/colorado-beetle-detection-model?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/ilvo-openagri/colorado-beetle-detection-model) | Colorado beetle detection model from the OpenAgri project. Edge inference works offline. EUPL-1.2. |
| [AgriVision](https://github.com/GEvang/agrivision-pipeline) ![GitHub Repo stars](https://img.shields.io/github/stars/GEvang/agrivision-pipeline?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/GEvang/agrivision-pipeline) | Computer-vision pipeline for agricultural imagery. EUPL-1.2. |

## Remote Sensing and Imagery

| Project Name | Description |
| :--- | :--- |
| [Raster Vision](https://github.com/azavea/raster-vision) ![GitHub Repo stars](https://img.shields.io/github/stars/azavea/raster-vision?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/azavea/raster-vision) | Deep learning for aerial and satellite imagery. |
| [Sen4CAP](https://github.com/Sen4CAP/Sen4CAP) ![GitHub Repo stars](https://img.shields.io/github/stars/Sen4CAP/Sen4CAP?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Sen4CAP/Sen4CAP) | ESA-funded Sentinel-1 and Sentinel-2 processing platform for Common Agricultural Policy monitoring. |

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Bryce Johnston](https://github.com/brycejohnston) has waived all copyright and related or neighbouring rights to this work.

<a id="home-button" href="#contents">Home</a>

<script>
document.querySelectorAll('a[href]').forEach(function (a) {
  if (a.getAttribute('href').charAt(0) === '#') return;
  a.target = '_blank';
  a.rel = 'noopener noreferrer';
});
</script>
