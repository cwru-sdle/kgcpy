.. kgcPy: Koeppen-Geiger Climatic Zones documentation master file, created by
   sphinx-quickstart on Fri Jul 28 15:55:24 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to kgcpy: Koeppen-Geiger Climatic Zones's documentation!
================================================================

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   kgcpy

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Description
==================

The kgcpy package is a python version of "kgc: Koeppen-Geiger Climatic Zones" R package on CRAN https://cran.r-project.org/web/packages/kgc/index.html, with addiontal functions.

Aids in identifying the Koeppen-Geiger (KG) climatic zone for a given location. The Koeppen-Geiger climate zones were first published in 1884, as a system to classify regions of the earth by their relative heat and humidity through the year, for the benefit of human health, plant and agriculture and other human activity [1]. This climate zone classification system, applicable to all of the earths surface, has continued to be developed by scientists up to the present day. 

One of authors (FZ) has published updated, higher accuracy KG climate zone definitions [2]. In this package we use these updated high-resolution maps as the data source [3]. We provide functions that return the KG climate zone for a given longitude and lattitude, or for a given United States zip code. In addition the nearbyCZ() function will check climate zones nearby to check if the given location is near a climate zone boundary. 
Digital data, as well as animated maps, showing the shift of the climate zones are provided on the following website <http://koeppen-geiger.vu-wien.ac.at>. 


| [1] W. Koeppen, (2011) <doi:10.1127/0941-2948/2011/105>. 
| [2] F. Rubel and M. Kottek, (2010) <doi:10.1127/0941-2948/2010/0430>. 
| [3] F. Rubel, K. Brugger, K. Haslinger, and I. Auer, (2016) <doi:10.1127/metz/2016/0816>.
