> [![Awesome list badge](https://awesome.re/badge.svg)](https://awesome.re) A curated list of awesome open source technology for agriculture, farming and gardening. [Pull requests welcome!](https://github.com/open-ag/open-ag.github.io)

[Agriculture](https://en.wikipedia.org/wiki/Agriculture) is the science and art of cultivating plants and livestock for food and materials. This list covers open source robotics, hardware, data, modelling and software for farms and growers.

Contributions welcome! Please follow the [contributing guidelines](https://github.com/open-ag/awesome-agriculture/blob/master/contributing.md). Repos updated over a year ago can be found in [Legacy](https://github.com/open-ag/open-ag.github.io/blob/master/LEGACY.md) this is a fork of [Bryce Johnson list](https://github.com/brycejohnston/awesome-agriculture)

## Contents

| Section | Subsections |
| :--- | :--- |
| [Automation and Robotics](#automation-and-robotics) |  |
| [Climate, Environment and Weather](#climate-environment-and-weather) |  |
| [Crop Modelling, Phenotyping and Pathology](#crop-modelling-phenotyping-and-pathology) |  |
| [Datasets](#datasets) |  |
| [Data Standardisation, Interoperability and APIs](#data-standardisation-interoperability-and-apis) |  |
| [Farm Management Systems and Record Keeping](#farm-management-systems-and-record-keeping) |  |
| [Geospatial and GIS](#geospatial-and-gis) | [GIS Resources](#gis-resources) · [GIS Platforms](#gis-platforms) · [Shapefiles](#shapefiles) |
| [IoT, Hardware](#iot-hardware) |  |
| [Knowledgebases and Learning Resources](#knowledgebases-and-learning-resources) |  |
| [Machine Learning and AI](#machine-learning-and-ai) |  |
| [Remote Sensing and Imagery](#remote-sensing-and-imagery) |  |

## Automation and Robotics

> Star and commit badges are only shown for single repositories. Organisation links and non-GitHub projects have none.

| Project Name | Description |
| :--- | :--- |
| [amiga-dev-kit](https://github.com/farm-ng/amiga-dev-kit) ![GitHub Repo stars](https://img.shields.io/github/stars/farm-ng/amiga-dev-kit?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/farm-ng/amiga-dev-kit) | Development kit for third-party hardware and software extensions to the farm-ng Amiga rover. |
| [bonsai-sdk](https://github.com/BonsaiRobotics/bonsai-sdk) ![GitHub Repo stars](https://img.shields.io/github/stars/BonsaiRobotics/bonsai-sdk?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/BonsaiRobotics/bonsai-sdk) | SDK for interacting with the Bonsai Robotics Amiga through ROS 2. |
| [farmbot-arduino-firmware](https://github.com/FarmBot/farmbot-arduino-firmware) ![GitHub Repo stars](https://img.shields.io/github/stars/FarmBot/farmbot-arduino-firmware?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/FarmBot/farmbot-arduino-firmware) | Arduino firmware executing g-code like commands over serial to move the FarmBot and operate the tool mount. |
| [farmbot-js](https://github.com/FarmBot/farmbot-js) ![GitHub Repo stars](https://img.shields.io/github/stars/FarmBot/farmbot-js?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/FarmBot/farmbot-js) | JavaScript wrapper for FarmBot's authentication and RPC instructions. |
| [farmbot-py](https://github.com/FarmBot/farmbot-py) ![GitHub Repo stars](https://img.shields.io/github/stars/FarmBot/farmbot-py?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/FarmBot/farmbot-py) | Authentication and communication utilities for FarmBot, Python. |
| [FarmBot-ROS](https://github.com/farmbot-ros/) | Open source farming robot. |
| [Farmbot-Web-App](https://github.com/FarmBot/Farmbot-Web-App) ![GitHub Repo stars](https://img.shields.io/github/stars/FarmBot/Farmbot-Web-App?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/FarmBot/Farmbot-Web-App) | Setup, customize and control FarmBot from any device, TypeScript. |
| [farmbot_os](https://github.com/FarmBot/farmbot_os) ![GitHub Repo stars](https://img.shields.io/github/stars/FarmBot/farmbot_os?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/FarmBot/farmbot_os) | Embedded OS handling motor axes, watering tools and sensors on FarmBot hardware. |
| [feldfreund_devkit](https://github.com/zauberzeug/feldfreund_devkit) ![GitHub Repo stars](https://img.shields.io/github/stars/zauberzeug/feldfreund_devkit?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/zauberzeug/feldfreund_devkit) | Development platform for autonomous weeding. |
| [Fields2Cover](https://github.com/Fields2Cover/Fields2Cover) ![GitHub Repo stars](https://img.shields.io/github/stars/Fields2Cover/Fields2Cover?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Fields2Cover/Fields2Cover) | Robust and efficient coverage paths for autonomous agricultural vehicles. |
| [JABAS.AI](https://github.com/jabasai) | ROS 2 repositories including graph-based topological navigation for crop-row layouts. |
| [librcom](https://github.com/romi/librcom) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/librcom?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/librcom) | ROMI rcom library, C++. |
| [lizard](https://github.com/zauberzeug/lizard) ![GitHub Repo stars](https://img.shields.io/github/stars/zauberzeug/lizard?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/zauberzeug/lizard) | Domain-specific language for real-time motor control and E-stop logic on microcontrollers. |
| [romi-apps](https://github.com/romi/romi-apps) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/romi-apps?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/romi-apps) | Applications for the ROMI system: CNC, camera, gimbal, cablebot, rover. |
| [romitask](https://github.com/romi/romitask) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/romitask?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/romitask) | ROMI task runner, a Luigi based task pipeline. |
| [rosys](https://github.com/zauberzeug/rosys) ![GitHub Repo stars](https://img.shields.io/github/stars/zauberzeug/rosys?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/zauberzeug/rosys) | Asynchronous Python framework for web GUI and state handling on mobile robots, used for field rovers. |
| [Sowbot](https://github.com/Agroecology-Lab/feldfreund_devkit_ros) ![GitHub Repo stars](https://img.shields.io/github/stars/Agroecology-Lab/feldfreund_devkit_ros?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Agroecology-Lab/feldfreund_devkit_ros) | Line-following sowing and weeding robot with some web UI tools. |
| [trellis](https://github.com/agtonomy/trellis) ![GitHub Repo stars](https://img.shields.io/github/stars/agtonomy/trellis?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agtonomy/trellis) | General-purpose middleware framework for distributed applications, by Agtonomy. Not ROS-based. |

## Climate, Environment and Weather

| Project Name | Description |
| :--- | :--- |
| [frostline](https://github.com/waldoj/frostline) ![GitHub Repo stars](https://img.shields.io/github/stars/waldoj/frostline?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/waldoj/frostline) | Dataset, API and Python parser for USDA plant hardiness zones. |
| [GSODR](https://github.com/ropensci/GSODR) ![GitHub Repo stars](https://img.shields.io/github/stars/ropensci/GSODR?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/ropensci/GSODR) | Global summary daily weather data in R. |
| [iem](https://github.com/akrherz/iem) ![GitHub Repo stars](https://img.shields.io/github/stars/akrherz/iem?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/akrherz/iem) | Code that makes the Iowa Environmental Mesonet run. |
| [OpenAgri-IrrigationManagement](https://github.com/agstack/OpenAgri-IrrigationManagement) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-IrrigationManagement?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-IrrigationManagement) | Evapotranspiration calculations and soil moisture analysis. |
| [OpenAgri-WeatherService](https://github.com/agstack/OpenAgri-WeatherService) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-WeatherService?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-WeatherService) | Weather forecasts and critical agricultural indicators. |
| [pyTSEB](https://github.com/hectornieto/pyTSEB) ![GitHub Repo stars](https://img.shields.io/github/stars/hectornieto/pyTSEB?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/hectornieto/pyTSEB) | Python two-source energy balance model for estimating evapotranspiration from remote sensing data. |
| [soilDB](https://github.com/ncss-tech/soilDB) ![GitHub Repo stars](https://img.shields.io/github/stars/ncss-tech/soilDB?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/ncss-tech/soilDB) | R library for simplified access to NCSS soil databases. |

## Crop Modelling, Phenotyping and Pathology

| Project Name | Description |
| :--- | :--- |
| [ApsimX](https://github.com/APSIMInitiative/ApsimX) ![GitHub Repo stars](https://img.shields.io/github/stars/APSIMInitiative/ApsimX?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/APSIMInitiative/ApsimX) | Next-generation APSIM framework for agricultural system simulations, C#. |
| [AquaCrop](https://github.com/aquacropos/aquacrop) ![GitHub Repo stars](https://img.shields.io/github/stars/aquacropos/aquacrop?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/aquacropos/aquacrop) | Python implementation of AquaCrop-OS for crop growth and water use. |
| [Awesome Crop Models](https://github.com/YuanyuanMa03/awesome-crop-models) ![GitHub Repo stars](https://img.shields.io/github/stars/YuanyuanMa03/awesome-crop-models?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/YuanyuanMa03/awesome-crop-models) | Curated list of open source crop models, process models, tools, applications and data-driven models. |
| [DSSAT](https://github.com/DSSAT/dssat-csm-os) ![GitHub Repo stars](https://img.shields.io/github/stars/DSSAT/dssat-csm-os?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/DSSAT/dssat-csm-os) | Cropping-system simulations across crops, soils, weather and management, Fortran. |
| [Open Plant Pathology](https://www.openplantpathology.org/) ([GitHub organisation](https://github.com/openplantpathology)) | Community for open data and computational tools in epidemiology and pathogen population biology and ecology. |
| [opensource-pestmodels](https://github.com/agstack/opensource-pestmodels) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/opensource-pestmodels?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/opensource-pestmodels) | Hierarchical pest and disease modelling framework (13 models, 19 crops, 54 threats) with Python wheel, FastAPI and MCP server. |
| [PCSE](https://github.com/ajwdewit/pcse) ![GitHub Repo stars](https://img.shields.io/github/stars/ajwdewit/pcse?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/ajwdewit/pcse) | Python environment for running crop growth and production models. |
| [plant-3d-explorer](https://github.com/romi/plant-3d-explorer) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/plant-3d-explorer?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/plant-3d-explorer) | Browser application to visualise 3D scanned plants. |
| [plant-3d-vision](https://github.com/romi/plant-3d-vision) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/plant-3d-vision?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/plant-3d-vision) | Digital reconstruction and phenotypic quantification of plant phyllotaxis. |
| [plant-imager](https://github.com/romi/plant-imager) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/plant-imager?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/plant-imager) | Library controlling the PlantImager (hardware) or the VirtualPlantImager (Blender) to acquire images of single potted plants. |
| [Plant-Imager3](https://github.com/romi/Plant-Imager3) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/Plant-Imager3?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/Plant-Imager3) | Plant imager software, Python. |
| [plantdb](https://github.com/romi/plantdb) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/plantdb?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/plantdb) | Database to host and serve images and processed data. |
| [romicgal](https://github.com/romi/romicgal) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/romicgal?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/romicgal) | Python CGAL bindings for skeletonisation. |
| [skeleton_refinement](https://github.com/romi/skeleton_refinement) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/skeleton_refinement?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/skeleton_refinement) | Plant skeleton optimisation using a stochastic framework on point cloud data. |

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

## Data Standardisation, Interoperability and APIs

| Project Name | Description |
| :--- | :--- |
| [ADAPT-Visualizer](https://github.com/AgGateway-ADAPT/ADAPT-Visualizer) ![GitHub Repo stars](https://img.shields.io/github/stars/AgGateway-ADAPT/ADAPT-Visualizer?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/AgGateway-ADAPT/ADAPT-Visualizer) | Windows Forms diagnostic tool for the ADAPT Framework, C#. |
| [AgIsoDDOPGenerator](https://github.com/Open-Agriculture/AgIsoDDOPGenerator) ![GitHub Repo stars](https://img.shields.io/github/stars/Open-Agriculture/AgIsoDDOPGenerator?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Open-Agriculture/AgIsoDDOPGenerator) | Free ISO11783 DDOP editor based on AgIsoStack++, C++. |
| [AgIsoDevelopmentTools](https://github.com/Open-Agriculture/AgIsoDevelopmentTools) ![GitHub Repo stars](https://img.shields.io/github/stars/Open-Agriculture/AgIsoDevelopmentTools?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Open-Agriculture/AgIsoDevelopmentTools) | AgIso development tools, C++. |
| [AgIsoStack-plus-plus](https://github.com/Open-Agriculture/AgIsoStack-plus-plus) ![GitHub Repo stars](https://img.shields.io/github/stars/Open-Agriculture/AgIsoStack-plus-plus?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Open-Agriculture/AgIsoStack-plus-plus) | Free open-source C++ ISOBUS library (ISO11783/J1939 CAN stack), MIT. |
| [AgIsoTerminalDesigner](https://github.com/Open-Agriculture/AgIsoTerminalDesigner) ![GitHub Repo stars](https://img.shields.io/github/stars/Open-Agriculture/AgIsoTerminalDesigner?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Open-Agriculture/AgIsoTerminalDesigner) | Experimental GUI for designing and modifying VT object pools, Rust. |
| [AgIsoVirtualTerminal](https://github.com/Open-Agriculture/AgIsoVirtualTerminal) ![GitHub Repo stars](https://img.shields.io/github/stars/Open-Agriculture/AgIsoVirtualTerminal?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Open-Agriculture/AgIsoVirtualTerminal) | Experimental ISO11783-6 Virtual Terminal (VT) server GUI based on AgIsoStack++, C++. |
| [ar2](https://github.com/agstack/ar2) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/ar2?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/ar2) | Asset Registry 2: hub and spoke model. |
| [ar2-hub](https://github.com/agstack/ar2-hub) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/ar2-hub?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/ar2-hub) | Hub component for Asset Registry 2. |
| [asset-registry](https://github.com/agstack/asset-registry) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/asset-registry?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/asset-registry) | Registers a geospatial asset (typically a polygon) and returns a unique GeoID; Flask, AR 1.0. |
| [Botanica](https://github.com/Michael-A-Kuykendall/botanica) ![GitHub Repo stars](https://img.shields.io/github/stars/Michael-A-Kuykendall/botanica?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/Michael-A-Kuykendall/botanica) | Rust crate for botanical data management with taxonomic hierarchy, cultivation tracking and Darwin Core compliance. |
| [cli](https://github.com/OADA/cli) ![GitHub Repo stars](https://img.shields.io/github/stars/OADA/cli?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/OADA/cli) | Pipeable OADA CLI client. |
| [cotton-gin-data-plugin](https://github.com/AgGateway-ADAPT/cotton-gin-data-plugin) ![GitHub Repo stars](https://img.shields.io/github/stars/AgGateway-ADAPT/cotton-gin-data-plugin?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/AgGateway-ADAPT/cotton-gin-data-plugin) | ADAPT Framework import-only plugin for cotton gin data, developed with Cotton Inc., C#. |
| [Data Food Consortium](https://github.com/datafoodconsortium/standard) ![GitHub Repo stars](https://img.shields.io/github/stars/datafoodconsortium/standard?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/datafoodconsortium/standard) | Open data standard (ontology, JSON-LD, LDP, OIDC) for interoperability between platforms used by producers in short food supply chains. |
| [dataModel.Agrifood](https://github.com/smart-data-models/dataModel.Agrifood) ![GitHub Repo stars](https://img.shields.io/github/stars/smart-data-models/dataModel.Agrifood?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/smart-data-models/dataModel.Agrifood) | Smart Data Models for agrifood: harmonised schemas for farms, parcels, crops, operations and greenhouse records. |
| [formats](https://github.com/OADA/formats) ![GitHub Repo stars](https://img.shields.io/github/stars/OADA/formats?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/OADA/formats) | Simplified approach to OADA formats using JSON Schema. |
| [ISOv4Plugin](https://github.com/AgGateway-ADAPT/ISOv4Plugin) ![GitHub Repo stars](https://img.shields.io/github/stars/AgGateway-ADAPT/ISOv4Plugin?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/AgGateway-ADAPT/ISOv4Plugin) | ADAPT Framework plugin for ISOXML (ISO11783-10), C#. |
| [MyJohnDeereAPI-OAuth2-Java-Example](https://github.com/JohnDeere/MyJohnDeereAPI-OAuth2-Java-Example) ![GitHub Repo stars](https://img.shields.io/github/stars/JohnDeere/MyJohnDeereAPI-OAuth2-Java-Example?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/JohnDeere/MyJohnDeereAPI-OAuth2-Java-Example) | Java MyJohnDeere API client example. |
| [MyJohnDeereAPI-OAuth2-NodeJS-Example](https://github.com/JohnDeere/MyJohnDeereAPI-OAuth2-NodeJS-Example) ![GitHub Repo stars](https://img.shields.io/github/stars/JohnDeere/MyJohnDeereAPI-OAuth2-NodeJS-Example?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/JohnDeere/MyJohnDeereAPI-OAuth2-NodeJS-Example) | Node.js MyJohnDeere API client example. |
| [oada-error-js](https://github.com/OADA/oada-error-js) ![GitHub Repo stars](https://img.shields.io/github/stars/OADA/oada-error-js?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/OADA/oada-error-js) | OADA standard error middleware. |
| [oadaify](https://github.com/OADA/oadaify) ![GitHub Repo stars](https://img.shields.io/github/stars/OADA/oadaify?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/OADA/oadaify) | Make OADA data nicer to work with in JS/TS. |
| [OpenAgri-Bootstrap-Deployment](https://github.com/agstack/OpenAgri-Bootstrap-Deployment) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-Bootstrap-Deployment?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-Bootstrap-Deployment) | Modular configuration and deployment of all OpenAgri services. |
| [OpenAgri-GateKeeper](https://github.com/agstack/OpenAgri-GateKeeper) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-GateKeeper?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-GateKeeper) | JWT-based authentication and access proxy. |
| [OpenAgri-OCSM](https://github.com/agstack/OpenAgri-OCSM) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-OCSM?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-OCSM) | OpenAgri Common Semantic Model. |
| [OpenTeam](https://openteam.community/) | Open technology ecosystem for agricultural management. |
| [pancake](https://github.com/agstack/pancake) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/pancake?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/pancake) | AI-native geospatial datastore and DPI services: field ownership grants as SD-JWT credentials, signed audit ledger, scheduled vendor data ingestion. |
| [SawitDB](https://github.com/WowoEngine/SawitDB) ![GitHub Repo stars](https://img.shields.io/github/stars/WowoEngine/SawitDB?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/WowoEngine/SawitDB) | Node.js database engine built for data sovereignty. |
| [semantic-croissant](https://github.com/agstack/semantic-croissant) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/semantic-croissant?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/semantic-croissant) | Semantic Croissant infrastructure, forked from codata/semantic-croissant. |
| [server](https://github.com/OADA/server) ![GitHub Repo stars](https://img.shields.io/github/stars/OADA/server?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/OADA/server) | Reference implementation of an OADA-conformant API server, TypeScript. |
| [Standard](https://github.com/AgGateway-ADAPT/Standard) ![GitHub Repo stars](https://img.shields.io/github/stars/AgGateway-ADAPT/Standard?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/AgGateway-ADAPT/Standard) | ADAPT Standard: data schema for farm reference data, field operations and geospatial layers, for B2B data sharing. |
| [StandardPlugin](https://github.com/AgGateway-ADAPT/StandardPlugin) ![GitHub Repo stars](https://img.shields.io/github/stars/AgGateway-ADAPT/StandardPlugin?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/AgGateway-ADAPT/StandardPlugin) | ADAPT Framework plugin to convert data to the ADAPT Standard, C#. |
| [user-registry](https://github.com/agstack/user-registry) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/user-registry?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/user-registry) | User accounts, JWT issuance and API keys for AR 1.0. |

## Farm Management Systems and Record Keeping

| Project Name | Description |
| :--- | :--- |
| [AgriOS](https://github.com/agstack/AgriOS) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/AgriOS?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/AgriOS) | Odoo 18 farm management addons: farmers, plots, trade and training (AGPL-3). |
| [Canopi](https://github.com/opencanopi/canopi) ![GitHub Repo stars](https://img.shields.io/github/stars/opencanopi/canopi?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/opencanopi/canopi) | Agroecological design for permaculture, syntropic agriculture and food forests, with a plant catalog and geolocated map canvas. Rust and TypeScript, AGPL-3.0. |
| [Ekylibre](https://github.com/ekylibre/ekylibre) ![GitHub Repo stars](https://img.shields.io/github/stars/ekylibre/ekylibre?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/ekylibre/ekylibre) | Farm management information system for farmers and small enterprises, Ruby on Rails and PostgreSQL/PostGIS. |
| [farmOS](https://github.com/farmOS/farmOS) ![GitHub Repo stars](https://img.shields.io/github/stars/farmOS/farmOS?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/farmOS/farmOS) | Web-based farm record keeping application built with Drupal and PHP. |
| [GrowerHub](https://github.com/aspinozaxxx-lab/growerhub) ![GitHub Repo stars](https://img.shields.io/github/stars/aspinozaxxx-lab/growerhub?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/aspinozaxxx-lab/growerhub) | Greenhouse and small-farm management: Zigbee2MQTT monitoring, plant and watering journals, lighting and irrigation automation. |
| [HortusFox](https://github.com/danielbrendel/hortusfox-web) ![GitHub Repo stars](https://img.shields.io/github/stars/danielbrendel/hortusfox-web?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/danielbrendel/hortusfox-web) | Self-hosted, collaborative plant management and journaling app. |
| [inatrace](https://github.com/agstack/inatrace) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/inatrace?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/inatrace) | Meta repository linking the INATrace backend, frontend, mobile and blockchain components; blockchain-based track and trace for supply chains. |
| [inatrace-backend](https://github.com/agstack/inatrace-backend) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/inatrace-backend?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/inatrace-backend) | Java/Spring backend. |
| [inatrace-coffee-network](https://github.com/agstack/inatrace-coffee-network) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/inatrace-coffee-network?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/inatrace-coffee-network) | Blockchain smart contracts for the coffee supply chain. |
| [inatrace-frontend](https://github.com/agstack/inatrace-frontend) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/inatrace-frontend?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/inatrace-frontend) | Angular frontend. |
| [inatrace-mobile](https://github.com/agstack/inatrace-mobile) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/inatrace-mobile?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/inatrace-mobile) | Mobile app for farmer data collection. |
| [LiteFarm](https://github.com/LiteFarmOrg/LiteFarm) ![GitHub Repo stars](https://img.shields.io/github/stars/LiteFarmOrg/LiteFarm?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/LiteFarmOrg/LiteFarm) | Community-led, not-for-profit farm management system. |
| [OpenAgri-FarmCalendar](https://github.com/agstack/OpenAgri-FarmCalendar) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-FarmCalendar?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-FarmCalendar) | Digital farm calendar for operations, observations, parcels and assets. |
| [OpenAgri-ReportingService](https://github.com/agstack/OpenAgri-ReportingService) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/OpenAgri-ReportingService?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/OpenAgri-ReportingService) | PDF report generation for agricultural data visualisation. |
| [Plant-it](https://github.com/MDeLuise/plant-it) ![GitHub Repo stars](https://img.shields.io/github/stars/MDeLuise/plant-it?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/MDeLuise/plant-it) | Self-hosted gardening companion app. |
| [tracefoodchain](https://github.com/agstack/tracefoodchain) ![GitHub Repo stars](https://img.shields.io/github/stars/agstack/tracefoodchain?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/agstack/tracefoodchain) | Flutter app and web app for tracing goods along food production chains. |

## Geospatial and GIS

### GIS Resources

| Project Name | Description |
| :--- | :--- |
| [Awesome GIS](https://github.com/sshuair/awesome-gis) ![GitHub Repo stars](https://img.shields.io/github/stars/sshuair/awesome-gis?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/sshuair/awesome-gis) | Curated list of GIS related sources. |

### GIS Platforms

| Project Name | Description |
| :--- | :--- |
| [QGIS](https://qgis.org) ([GitHub repository](https://github.com/qgis/QGIS)) ![GitHub Repo stars](https://img.shields.io/github/stars/qgis/QGIS?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/qgis/QGIS) | Free, open source, cross-platform (Linux, Windows, macOS) geographic information system. |

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
| [OpenWeedLocator](https://github.com/geezacoleman/OpenWeedLocator) ![GitHub Repo stars](https://img.shields.io/github/stars/geezacoleman/OpenWeedLocator?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/geezacoleman/OpenWeedLocator) | Low-cost, image-based weed detection device for in-crop and fallow scenarios. |
| [romi-bldc-controller](https://github.com/romi/romi-bldc-controller) ![GitHub Repo stars](https://img.shields.io/github/stars/romi/romi-bldc-controller?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/romi/romi-bldc-controller) | Arduino firmware to control brushless motors, based on SimpleFOC. |
| [Simplesteer](https://github.com/matmis/simplesteer) ![GitHub Repo stars](https://img.shields.io/github/stars/matmis/simplesteer?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/matmis/simplesteer) | RTK GPS tractor autosteer with a web interface controllable from a smartphone; runs on a Raspberry Pi. |

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

## Remote Sensing and Imagery

| Project Name | Description |
| :--- | :--- |
| [Raster Vision](https://github.com/azavea/raster-vision) ![GitHub Repo stars](https://img.shields.io/github/stars/azavea/raster-vision?style=social)<br>![GitHub last commit](https://img.shields.io/github/last-commit/azavea/raster-vision) | Deep learning for aerial and satellite imagery. |

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
