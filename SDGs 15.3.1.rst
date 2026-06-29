.. _sdg-15-3-1:

SDG 15.3.1
========================================

The Sustainable Development Goal (SDG) 15.3 aims to **combat desertification** and **restore degraded land and soil**, striving to achieve a **land degradation–neutral world by 2030**.

Indicator **15.3.1** measures the **proportion of degraded land** over the total land area, using three key sub-indicators:

.. contents::
   :local:
   :depth: 2

---

.. _land-cover:

Land Cover
----------

.. figure:: _static/images/land_cover_niger.png
   :alt: Land cover map for Niger
   :width: 700px
   :align: center

   Land cover map for Niger

The land cover sub-indicator measures changes in the Earth's surface cover over time,
detecting conversions between natural and human-modified land types.

**Typical data sources:**

* ESA CCI Land Cover
* Spatial resolution: 300 m
* Temporal coverage: 1992–2022

`Back to top <#sdg-15-3-1>`_

---

.. _land-cover-change:

Land Cover Change
-----------------

.. figure:: _static/images/landcover_change_niger_baseline.png
   :alt: Land cover change map for Niger – baseline period
   :width: 700px
   :align: center

   Land cover change map for Niger – baseline period (2000–2015)

.. figure:: _static/images/landcover_chnage_niger_baseline.png
   :alt: Land cover change map for Niger – detail
   :width: 700px
   :align: center

   Land cover change map for Niger – detail view

This sub-indicator assesses **changes in land cover** between two reference periods (e.g., 2000–2015 or 2015–2022).
It helps detect transitions between land-cover classes (forest, cropland, grassland, built-up areas, etc.)
and quantify **losses or gains of natural land**.

**Reference periods:**

* Baseline: 2000–2015
* Reporting: 2015–2022

**Typical data sources:**

* ESA CCI Land Cover

`Back to top <#sdg-15-3-1>`_

---

.. _land-productivity:

Land Productivity
-----------------

.. figure:: _static/images/land_productivity_ethiopie_baseline.png
   :alt: Land productivity map for Ethiopia – baseline period
   :width: 700px
   :align: center

   Land productivity map for Ethiopia – baseline period

.. figure:: _static/images/productivity.png
   :alt: Land productivity map
   :width: 700px
   :align: center

   Land productivity map

This sub-indicator analyzes **vegetation dynamics** (e.g., NDVI or EVI) to estimate **productivity trends**.
A persistent decline in vegetation productivity can indicate **ecological degradation** or **human-induced land stress**.

**Common methods:**

* NDVI trend analysis (Mann-Kendall, Theil-Sen)
* Deviation from potential productivity
* Land productivity state classification

**Data sources:**

* MODIS NDVI/EVI
* Landsat NDVI
* Google Earth Engine analyses

`Back to top <#sdg-15-3-1>`_

---

.. _carbon-stock:

Carbon Stock
------------

.. figure:: _static/images/soil_organique_carbone_reporting.png
   :alt: Soil organic carbon map – reporting period
   :width: 700px
   :align: center

   Soil organic carbon map – reporting period

.. figure:: _static/images/soc.png
   :alt: Soil organic carbon map
   :width: 700px
   :align: center

   Soil organic carbon map

The **carbon stock** sub-indicator evaluates changes in **soil and biomass organic carbon**.
Decreases in carbon storage often indicate **loss of organic matter**, **deforestation**, or **soil degradation**.

**Components considered:**

* Soil Organic Carbon (SOC)
* Above- and below-ground biomass carbon
* Total change between two time periods

**Data sources:**

* FAO GSOCmap
* GlobBiomass
* ESA CCI Biomass

`Back to top <#sdg-15-3-1>`_

---

.. _final-sdg:

Final SDG 15.3.1 Indicator
---------------------------

.. figure:: _static/images/SDGs_15.3.1_senegal.png
   :alt: SDG 15.3.1 map for Senegal
   :width: 700px
   :align: center

   SDG 15.3.1 map for Senegal

.. figure:: _static/images/sdg.png
   :alt: SDG 15.3.1 baseline map
   :width: 700px
   :align: center

   SDG 15.3.1 baseline map – Niger (2000–2015)

The **SDG indicator 15.3.1** measures the **proportion of degraded land** over the total land area.

Land is classified as **degraded** when **at least one** of the following sub-indicators shows a negative change:

* Land cover change
* Land productivity decline
* Carbon stock loss

This follows the **"one-out, all-out"** principle recommended by the **UNCCD**.

`Back to top <#sdg-15-3-1>`_
