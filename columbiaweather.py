from urllib import urlencode, urlopen
from datetime import datetime


def forecast(lat,lon):
    day_of_year = datetime.now().timetuple().tm_yday
    done = False
    forecastURL = "http://iridl.ldeo.columbia.edu/expert/home/.benno/.IMD/.three-hourly/.INDIA/.APCP/L/0.0625/0.9375/RANGE/S/"+day_of_year+"/VALUE/lat/"+lat+"/VALUE/lon/"+lon+"/VALUE/L/SUM/data.tsv"
    while(not done):
        try:
            result = urlopen(forecastURL)
            done = True
        except:
            done = False
    
    return result
