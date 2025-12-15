Forest Loss
========================================

.. toctree::
   :maxdepth: 1
   :caption: Navigation

   sdg_15_3_1
   land_cover
   land_cover_change
   land_productivity
   carbon_stock
   forest_loss

---

This page describes the **annual forest loss** derived from the **Hansen Global Forest Change** dataset.  
Forest loss represents the **stand-replacement disturbance** or complete removal of tree cover canopy at the pixel level for a given year.

The analysis is performed for a **specific area of interest (AOI)** and a **selected year**.

.. contents::
   :local:
   :depth: 2

---

Definition
----------------------

**Forest loss** is defined as the **complete removal of tree canopy cover** within a pixel, occurring in a specific year.  
Once a pixel is marked as forest loss, it remains classified as lost in subsequent years.

This indicator captures:
- Deforestation
- Severe logging
- Fire-induced canopy removal
- Conversion to non-forest land use

Forest loss does **not** distinguish between natural and human-induced causes.

---

Dataset
----------------------

The forest loss data is derived from:

**UMD / Hansen Global Forest Change**  
``UMD/hansen/global_forest_change_2024_v1_12``

**Key characteristics:**
- Spatial resolution: 30 m
- Temporal coverage: 2001–2023
- Global coverage
- Annual loss layer (``lossyear``)

---

Methodology
----------------------

The annual forest loss is calculated using the following steps:

1. Clip the Hansen dataset to the **Area of Interest (AOI)**
2. Select pixels where:

   - ``lossyear == target_year``

3. Mask all other pixels
4. Calculate forest loss area:

   - Pixel count × pixel area (m² → ha or km²)

This ensures that only **new forest loss for the selected year** is included.

---

Output
----------------------

.. image:: _static/images/forest_loss_year.png
   :alt: Annual forest loss map
   :width: 700px
   :align: center

**Outputs include:**
- Annual forest loss map
- Total forest loss area for the selected year
- Spatial distribution of loss within the AOI

---

Limitations
----------------------

- Forest loss represents **canopy removal**, not gradual degradation
- Temporary tree cover loss (e.g. plantations) may be included
- No attribution of loss drivers (fire, logging, agriculture)
- Forest regrowth is not considered in the loss layer

---

Reference
----------------------

- Hansen, M. C. et al. (2013). *High-Resolution Global Maps of 21st-Century Forest Cover Change*. Science.
- Dataset: ``UMD/hansen/global_forest_change_2024_v1_12``
