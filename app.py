import pandas as pd
import streamlit as st
import numpy as np
from st_functions import st_button, load_css
from PIL import Image
import os
import avwx
import streamlit.components.v1 as components
   
def main():

  st.set_page_config(
     page_title="SDO App",
     page_icon="🖥️",  
  )

  load_css()

  st.title('SDO App')

  col1, col2 = st.tabs(["Flight OPS", "Admin"])

  icon_size = 20

  with col1:

    st.header('Flight Ops')
  
    
    components.iframe('https://embed.windy.com/embed2.html?lat=48.283&lon=-122.695&detailLat=37.751&detailLon=-97.822&width=700&height=600&zoom=6&level=surface&overlay=radar&product=radar&menu=&message=true&marker=true&calendar=now&pressure=&type=map&location=coordinates&detail=&metricWind=kt&metricTemp=%C2%B0F&radarRange=-1', width=700, height=600)
   
   
    airports = st.text_input('Enter ICAO')
    if airports:
      metar = avwx.Metar(airports)
      taf = avwx.Taf(airports)
      notam = avwx.Notams(airports)
      st.write(metar.station.name)
      st.write(metar.update())
      st.write(metar.last_updated)
      st.write(metar.raw)
      st.write(taf.station.name)
      st.write(taf.update())
      st.write(taf.last_updated)
      st.write(taf.raw)
      st.write(notam.update())
      st.write(notam.last_updated)
      for i in range(len(notam.data)):
         st.write(notam.data[i].raw)
      
      
    st_button('safety', 'https://asap.safety.af.mil/#/', 'ASAP', icon_size)
    st_button('card', 'https://aircardsys.com/cgi-bin/fbo_locate', 'Air Card FBO Locator', icon_size)
    st_button('adds', 'https://aviationweather.gov/adds/', 'ADDS Weather', icon_size)
    st_button('schedule', 'https://dcast.cds.disa.mil', 'DCAST', icon_size)
    st_button('wx', 'https://fwb.metoc.navy.mil/', 'Navy Flight Weather Briefer', icon_size)
    st_button('notams', 'https://www.notams.faa.gov/dinsQueryWeb/', 'NOTAMS', icon_size)
    st_button('sharp', 'https://sharp.dc3n.navy.mil/?utm_source=mnp%20public', 'SHARP', icon_size)
    st_button('sky', 'https://skyvector.com/', 'Skyvector', icon_size)
   
  with col2:

    st.header('Admin')

    st_button('clipboard', 'https://asm3.nmci.navy.mil/ASM3/cac?utm_source=mnp%20public', 'ASM', icon_size)
    st_button('person', 'https://www.bol.navy.mil/bam/?utm_source=mnp%20public', 'BOL', icon_size)
    st_button('airplane', 'https://dtsproweb.defensetravel.osd.mil/dts-app/pubsite/all/view/?utm_source=mnp%20public', 'DTS', icon_size)
    st_button('safe', 'https://safe.apps.mil/', 'DoD Safe', icon_size)
    st_button('navfit', 'https://nefp.bol.navy.mil/lc/ws', 'eNavFit', icon_size)
    st_button('book', 'https://jkodirect.jten.mil/Atlas2/page/login/Login.jsf', 'JKO', icon_size)
    st_button('health', 'https://www.health.mil/Military-Health-Topics/MHS-Transformation/MHS-GENESIS', 'MHS GENESIS Patient Portal', icon_size)
    st_button('connect', 'https://milconnect.dmdc.osd.mil/milconnect/', 'milConnect', icon_size)
    st_button('money', 'https://mypay.dfas.mil/#/', 'myPay', icon_size)
    st_button('ndds', 'https://ndds.navair.navy.mil/', 'NDDS', icon_size)
    st_button('info', 'https://navyfamily.navy.mil/cas/login?service?utm_source=mnp%20public', 'NFAAS', icon_size)
    st_button('person', 'https://www.nsips.navy.mil/?utm_source=mnp%20public', 'NSIPS', icon_size)
    st_button('report', 'https://ntira.nmci.navy.mil/', 'NTIRA', icon_size)
    st_button('fitness', 'https://www.mnp.navy.mil/group/performance/parfq?utm_source=mnp%20public', 'PARFQ', icon_size)
    st_button('stats', 'https://www.mnp.navy.mil/group/performance/prims?utm_source=mnp%20public', 'PRIMS', icon_size)
    st_button('appointment', 'https://idco.dmdc.osd.mil/idco/?utm_source=mnp%20public', 'RAPIDS ID', icon_size)
    st_button('invest', 'https://www.tsp.gov/?utm_source=mnp%20public', 'TSP', icon_size)
    st_button('email', 'https://webmail.east.nmci.navy.mil/exchange/', 'Webmail East', icon_size)
    st_button('email', 'https://webmail.west.nmci.navy.mil/exchange/', 'Webmail West', icon_size)
    st_button('email2', 'https://portal.apps.mil/default.aspx', 'Flankspeed Portal', icon_size)


  col3, col4, col5 = st.columns(3)

  with col4:

    st_button('cup', 'https://www.buymeacoffee.com/hegerjl', 'Buy me a Coffee', icon_size)

  components.iframe('https://open.spotify.com/embed/playlist/5AsAwYzcbeuoKZN17TecbB?utm_source=generator&theme=0', width=480, height=360)
  
if __name__ == "__main__":
   
  main()
