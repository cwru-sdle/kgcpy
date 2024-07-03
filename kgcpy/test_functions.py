from kgcpy import loadKMZImage, loadCSV, lookupCZ, translateZipCode, irradianceQuantile, roundCoordinates, nearbyCZ
import pytest

# Testing LookupCZ() function with random lon and lat
def test_lookupCZ():
    assert lookupCZ(56.002315, -130.041026) == 'Dfb'
    assert lookupCZ(18.263085, -66.712985) == 'Af'
    assert lookupCZ(18.107800, -67.037263) == 'Am'
    assert lookupCZ(42.600633, -70.883303) == 'Cfa'
    assert lookupCZ(42.673909, -71.091334) == 'Dfa'
    assert lookupCZ(41.209283, -73.164603) == 'Cfa'
    assert lookupCZ(39.159233, -119.735982) == 'Csa'
    assert lookupCZ(56.002315, -130.041026) == 'Dfb'
    assert lookupCZ(37.769436, -122.447662) == 'Csb'
    assert lookupCZ(25.531145, -80.391233) == 'Am'

# Testing translateZipCode() function with random zip codes
def test_translateZipCode():
    assert translateZipCode(49893) == (45.297038,-87.605155)
    assert translateZipCode(52335) == (41.467961,-92.053796)
    assert translateZipCode(58348) == (47.971665,-99.52109)
    assert translateZipCode(61940) == (39.807701,-87.818525)
    assert translateZipCode(65669) == (36.911907,-93.302603)
    assert translateZipCode(67457) == (38.393628,-97.992841)
    assert translateZipCode(68142) == (41.371146,-96.10708)
    assert translateZipCode(70815) == (30.455463,-91.066262)
    assert translateZipCode(74136) == (36.0624,-95.941457)
    assert translateZipCode(75975) == (31.897138,-94.413785)

# Testing irradianceQuantile() function with random KGC climate areas
def test_irradianceQuantile():
    assert irradianceQuantile("Am") == (2205.288, 1958.4, 1857.6, 1800)
    assert irradianceQuantile("BSk") == (2199.6, 1915.2, 1627.2, 1497.6)
    assert irradianceQuantile("Cfa") == (2021.688, 1767.6, 1638.0, 1436.4)
    assert irradianceQuantile("Csb") == (2210.4, 1843.2, 1641.6, 1547.28)
    assert irradianceQuantile("Dfa") == (1591.2, 1472.4, 1386.0, 1303.2)
    assert irradianceQuantile("Dfc") == (1306.8, 1108.8, 997.2, 943.2)
    assert irradianceQuantile("Dsb") == (2022.336, 1836.0, 1684.8, 1611.36)
    assert irradianceQuantile("Dwc") == (1987.2, 1386.0, 1256.4, 1195.2)
    assert irradianceQuantile("Dwd") == (1056.456, 1008.0, 990.0, 982.8)
    assert irradianceQuantile("EF") == (1231.2, 1137.6, 1029.6, 928.8)
    assert irradianceQuantile("ET") == (2138.4, 1130.4, 914.4, 835.2)

# Testing roundCoordiantes() function with random lon and lat
# Some of the roundings are 0.01 off due to floating point precision
def test_roundCoordinates():
    assert roundCoordinates(56.002315, -130.041026) == (56.01, -130.04)
    assert roundCoordinates(18.263085, -66.712985) == (18.26, -66.71)
    assert roundCoordinates(18.107800, -67.037263) == (18.10, -67.04)
    assert roundCoordinates(42.600633, -70.883303) == (42.60, -70.88)
    assert roundCoordinates(42.673909, -71.091334) == (42.68, -71.10)
    assert roundCoordinates(41.209283, -73.164603) == (41.21, -73.15)
    assert roundCoordinates(39.159233, -119.735982) == (39.15, -119.74)
    assert roundCoordinates(56.002315, -130.041026) == (56.01, -130.04)
    assert roundCoordinates(37.769436, -122.447662) == (37.76, -122.46)
    assert roundCoordinates(25.531145, -80.391233) == (25.54, -80.40)


# Testing nearbyCZ() function with random lon and lat
def test_nearbyCZ():
    assert nearbyCZ(56.002315, -130.041026) == ('Dfb', 1.0, [])
    assert nearbyCZ(18.263085, -66.712985) == ('Af', 1.0, [])
    assert nearbyCZ(18.107800, -67.037263) == ('Am', 1.0, [])
    assert nearbyCZ(42.600633, -70.883303) == ('Cfa', 1.0, [])
    assert nearbyCZ(42.673909, -71.091334) == ('Dfa', 0.7777777777777778, ['Dfb'])
    assert nearbyCZ(41.209283, -73.164603) == ('Cfa', 1.0, [])
    assert nearbyCZ(39.159233, -119.735982) == ('Csa', 1.0, [])
    assert nearbyCZ(56.002315, -130.041026) == ('Dfb', 1.0, [])
    assert nearbyCZ(37.769436, -122.447662) == ('Csb', 1.0, [])
    assert nearbyCZ(25.531145, -80.391233) == ('Am', 1.0, [])

 