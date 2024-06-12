from PIL import Image
import pandas as pd
from importlib import resources
import io
Image.MAX_IMAGE_PIXELS = None
import time

# Helper function to load png file
def loadKMZImage(file):
    # Load the image file
    with resources.files('kgcPy').joinpath(file).open('rb') as fp:
        img = fp.read()
    img = Image.open(io.BytesIO(img))
    # img_rgb = img.convert('RGB')
    return img

# Helper function to load different CSV files
def loadCSV(file):
    with resources.files('kgcPy').joinpath(file).open('rb') as fp:
        kgc_csv = fp.read()

    if file == 'kg_zoneNum.csv':
        return pd.read_csv(io.BytesIO(kgc_csv))
    elif file == 'zipcodes.csv':
        return pd.read_csv(io.BytesIO(kgc_csv), index_col=0, dtype={'zip':'string'})
    elif file == 'df_quantile.csv':
        return pd.read_csv(io.BytesIO(kgc_csv), index_col=0, dtype={'kg_zone':'string'})


# This function will return the climate zone for the co-ordinates provided.
def lookupCZ(lat,lon,img,df):
    """
    This function will return the climate zone for the co-ordinates provided.
    _summary_

    Args:
        lat (_type_): latitude
        lon (_type_): longitude

    Returns:
        _type_: _description_
    """

    # Get the KG zone values of the pixel at position (x, y)
    x = round((lon+180)*(img.size[0])/360 - 0.5)
    y = round(-(lat-90)*(img.size[1])/180 - 0.5)
    num = img.getpixel((x, y))

    # Use the loc method to find the index of the row that matches the input values
    res = df['kg_zone'].loc[df['zoneNum'] == num]

    return res.values[0]

# This function will return the data frame with the longitude and latitude of the zip codes
def translateZipCode(zipcode,df):
    """
    This function will return the data frame with the longitude and latitude of the zip codes

    _summary_

    Args:
        zipcode (_type_): zipcode

    Returns:
        _type_: _description_
    """
    zipcode = str(zipcode)
        
    try:
        rows = df.loc[df['zip'] == zipcode]
        if len(rows) == 0:
            return f"No matching rows found for zipcode {zipcode}"
        else:
            return rows['lat'].iloc[0], rows['lon'].iloc[0]
    except Exception as e:
        return f"Search failed: {e}"

# Get irradiance quantiles for each Koppen Geiger Climate Zone
def irradianceQuantile(kg_zone,df):
    """
    Get irradiance quantiles for each Koppen Geiger Climate Zone

    _summary_

    Args:
        kg_zone (_type_): Koppen Geiger zone

    Returns:
        _type_: _description_
    """
    # kg_zone = str(kg_zone)

    try:
        rows = df.loc[df['kg_zone'] == kg_zone]
        if len(rows) == 0:
            return f"Climate zone {kg_zone} doesn't exist"
        else:
            return rows['quantilep98'].iloc[0], rows['quantilep80'].iloc[0], rows['quantilep50'].iloc[0], rows['quantilep30'].iloc[0]
    except Exception as e:
        return f"Search failed: {e}"

# The inputed number to nearest ’fine’ (100s) resolution grid point.
def roundCoordinates(lat,lon,img):
    """
    The inputed number to nearest 'fine' (100s) resolution grid point.

    _summary_

    Args:
        lat (_type_): latitude
        lon (_type_): longitude

    Returns:
        _type_: _description_
    """

    # Get the RGB values of the pixel at position (x, y)
    x = round((lon+180)*(img.size[0])/360 - 0.5)
    y = round(-(lat-90)*(img.size[1])/180 - 0.5)

    lonRound = (x + 0.5) * 360 / img.size[0] - 180
    latRound = - (y + 0.5) * 180 / img.size[1] + 90

    return latRound, lonRound

#get possible climate zones from nearby pixels, and compare to the center pixel; same as function CZUncertainty() in kgc R package 
def nearbyCZ(lat,lon,img,df,size=1):
    """
    get possible climate zones from nearby pixels, and compare to the center pixel; same as function CZUncertainty() in kgc R package 

    _summary_

    Args:
        lat (_type_): latitude
        lon (_type_): longitude
        size (int, optional): size of nearby pixel. Defaults to 1.

    Returns:
        _type_: _description_
    """
    # Load the image file
    # Test
    # img = Image.open('Beck_KG_V1_present_0p0083.tif')

    # Get the RGB values of the pixel at position (x, y)
    x = round((lon+180)*(img.size[0])/360 - 0.5)
    y = round(-(lat-90)*(img.size[1])/180 - 0.5)
 
    climateZones = []
    climateZone = ''

    for i in range(x-size, x+size+1):
        for j in range(y-size, y+size+1):
            try:
                num = img.getpixel((i, j))
                # rgb_values = {'R': r, 'G': g, 'B': b}
                # Use the loc method to find the index of the row that matches the input values
                cz = df['kg_zone'].loc[df['zoneNum'] == num]
                climateZones.append(cz.values[0])
                if i == x and j == y:
                    climateZone = cz.values[0]
            except IndexError:
                pass
    
    climateZones_series = pd.Series(climateZones)
    climateZones_counts = climateZones_series.value_counts()
    climateZones_percentage = climateZones_counts / climateZones_counts.sum()
    uncertaintyNearbyCZ = climateZones_percentage[climateZone]

    nearbyCZ = climateZones_series.unique().tolist()
    nearbyCZ.remove(climateZone)

    return climateZone, uncertaintyNearbyCZ, nearbyCZ


start_time = time.time()

'''
## Testing LookupCZ() 
zip = pd.read_csv('kgcPy/zipcodes.csv')
print(zip)

image = loadKMZImage('kmz_int_reshape.png')
kg_zonNum_df = loadCSV('kg_zoneNum.csv')
CZresults = pd.DataFrame(columns=['lat', 'lon', 'CZ'])

for i in range(len(zip)):
    lat = zip.iloc[i]['lat']
    lon = zip.iloc[i]['lon']
    cz = lookupCZ(lat, lon, img=image, df=kg_zonNum_df)
    CZresults.loc[i] = [lat, lon, cz]
print(CZresults)
'''



'''
## Testing translateZipCode()
locations = pd.DataFrame(columns=['zipcode', 'coordinates'])
zipcodes_df = loadCSV('zipcodes.csv')
for i in range(len(zipcodes_df)):
    zip = zipcodes_df.iloc[i]['zip']
    coordinate = translateZipCode(zipcode=zip,df=zipcodes_df)
    locations.loc[i] = [zip, coordinate]
print(locations)
'''



'''
## Testing irradianceQuantile()
quantiles = pd.DataFrame(columns=['kg_zone', 'quantiles'])
quantiles_df = loadCSV('df_quantile.csv')
for i in range(len(quantiles_df)):
    kg_z = quantiles_df.iloc[i]['kg_zone']
    quantile = irradianceQuantile(kg_zone=kg_z, df=quantiles_df)
    quantiles.loc[i] = [kg_z, quantile]
print(quantiles)
'''



'''
## Testing roundCoordinates()
zip = pd.read_csv('kgcPy/zipcodes.csv')

image = loadKMZImage('kmz_int_reshape.png')
rounded_coords = pd.DataFrame(columns=['original lat', 'original lon', 'rounded coordinates'])
for i in range(len(zip)):
    lat = zip.iloc[i]['lat']
    lon = zip.iloc[i]['lon']
    rounded = roundCoordinates(lat, lon, img=image)
    rounded_coords.loc[i] = [lat, lon, rounded]
print(rounded_coords)
'''



'''
## Testing nearbyCZ()
zip = pd.read_csv('kgcPy/zipcodes.csv')

image = loadKMZImage('kmz_int_reshape.png')
kg_zonNum_df = loadCSV('kg_zoneNum.csv')
nearby_CZresults = pd.DataFrame(columns=['lat', 'lon', 'Nearby CZ result'])

for i in range(len(zip)):
    lat = zip.iloc[i]['lat']
    lon = zip.iloc[i]['lon']
    nearby_result = nearbyCZ(lat, lon, img=image,df=kg_zonNum_df)    
    nearby_CZresults.loc[i] = [lat, lon, nearby_result]
print(nearby_CZresults)
'''

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.2f} seconds")