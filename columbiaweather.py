from urllib import urlencode, urlopen
from datetime import datetime


def forecast(lat,lon):
    day_of_year = str(datetime.now().timetuple().tm_yday)
    done = False
    forecastURL = "http://iridl.ldeo.columbia.edu/expert/home/.benno/.IMD/.three-hourly/.INDIA/.APCP/L/0.0625/0.9375/RANGE/S/"+day_of_year+"/VALUE/lat/"+str(lat)+"/VALUE/lon/"+str(lon)+"/VALUE/L/SUM/data.tsv"
    while(not done):
        try:
            ##print forecastURL
            result = urlopen(forecastURL)
            data = result.read()
            done = True
        except:
            done = False
    
    return data
