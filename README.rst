Tacos and Transit
=================

Overview:
---------

Tacos and Transit is an idea from Open San Diego to create an interactive map of Taco Shops in San Diego, and illustrate their accessibility by public transit.

Goals:
------

1. Contrast things San Diego is often considered the best at (Tacos), and the worst at (Public Transit).
2. Highlight public transit accessibility to something very integral to San Diego culture / experience
3. Have an excuse to make a master list of taco shops, yum yum!

Status: 
-------
Prototype / Exploration

Features:
---------

1. Taco Shop Listing
2. Taco Shop Scores / Info
3. Interactive Map
4. Time-To-Taco (get directions, but with public transit to taco shop - stretch goal)

Tech Stack:
-----------

**This is under consideration**

1. Python Scripts (for data gathering / processing ) 
   - Possibly Jupyter for data calculation?
2. Javascript / HTML (for interactive web interface)
3. Webpack (for managing web interface)

NOTE: we may want to either build the web interface as part of this project repo, or have it a common tool in opensandiego.github.io that we then use to pull in geoJSON features. TBD

Tasks to Do
-----------

1. Identify source(s) for Taco Shop listing 
2. Automate pull of transit stop data, identify different values (e.g. agency) and what that means
3. Create scoring system for Taco Shop accessibility - ideally find existing literature on how to score a location by accessibility to public transit (if not - ideas might be distance from transit stop and frequency of service, or time to travel from major hubs)
4. Export GeoJSON for import into overlay JS
5. Build out Interactive Map*

* A tertiary goal of this project is to create a common interactive data map or Open San Diego, where visitors can explore Open Data in San Diego, and OSD can showcase its projects, initiatives, and research.

