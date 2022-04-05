#!/usr/bin/env python
# coding: utf-8

# In[25]:


import math
from geopy.geocoders import Nominatim
import time
# from astropy.coordinates import SkyCoord

async def model(city,obj):
    app= Nominatim(user_agent='user')
    async def locations(str) :
        # time.sleep(1)
        # try:
            a=await app.geocode(str).raw
            print(a)
            return a
        # except:
            print('Check whether what you have typed is correct')

    locat= city
    location = await locations(locat)
    print(location)
    print('========================================')
    lat = location['lat']
    lon=location['lon']

    a=time.gmtime()

    yy=float(a.tm_year%100)
    MM=float(a.tm_mon)
    dd=float(a.tm_mday)

    hh=float(a.tm_hour)
    mm=float(a.tm_min)
    ss=float(a.tm_sec)


    UT= hh +mm/60

    JD = (367*yy) - int((7*(yy+int((MM+9)/12)))/4) + int((275*MM)/9) + dd + 1721013.5 + (UT/24)
    GMST = 18.697374558 + 24.06570982441908*(JD - 2451545)
    GMST=GMST%24
    long_h=float(lon)/15
    LST=GMST+float(long_h)+1.5
    print(LST)
    
    if LST < 0:
        LST = LST +24
    
    lst=LST*15

    # J2000 = JD - 2451545.0
    # LST = 100.46 + 0.985647 * J2000 + lon + 15*UT+15
    
    # while(LST<0 or LST>360):
    #     if LST<0:
    #         LST=LST+360
    #     else:
    #         LST=LST-360
    # lst=LST

    print(lst)
    
    obj_dict={
        "venus":[331.39999,-11.14361],
        "mars":[329.904166,-15.33027],
        "jupiter":[353.07499,-4.096944],
        "saturn":[324.36666,-15.165277],
        "uranus":[40.741666,15.41555],
        "neptune":[23.626388,-3.64916]
    }
    #for ra and dec of jupiter
    ra=obj_dict[obj][0]
    dec=obj_dict[obj][1]
    
    #######
    ha = lst -ra
    #converting dec,ra,ha and lat from degrees to radians
    ra= ra*math.pi/180
    dec= dec*math.pi/180
    ha= ha*math.pi/180
    lat= float(lat)*math.pi/180

    alt= math.sin(dec)*math.sin(lat) + math.cos(dec)*math.cos(ha)
    print(alt)
    alt= math.asin(alt)

    a= (math.sin(dec) - math.sin(alt)*math.sin(lat))/(math.cos(alt)*math.cos(lat))
    if(a<-1):
        a=a+2
    print(a)
    a=math.acos(a)
    #converting alt and a from radians to degree
    alt=alt*180/math.pi
    a=a*180/math.pi

    if(math.sin(ha)<0):
        az=a
    else:
        az=360-a
    print('For JUPITER-')
    res=[alt,az]
    return res

