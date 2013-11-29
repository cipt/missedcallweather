from urllib import urlencode, urlopen
from datetime import datetime


def forecast(lat,lon):
    day_of_year = str(datetime.now().timetuple().tm_yday)
    done = False
    errors = 0
    forecastURL = "http://iridl.ldeo.columbia.edu/expert/home/.benno/.IMD/.three-hourly/.INDIA/.APCP/L/0.0625/0.9375/RANGE/S/"+day_of_year+"/VALUE/lat/"+str(lat)+"/VALUE/lon/"+str(lon)+"/VALUE/L/SUM/data.tsv"
    while((not done) and (errors<5)):
        try:
            result = urlopen(forecastURL)
            data = result.read()
            done = True
        except:
            done = False
            errors+=1
    return data
