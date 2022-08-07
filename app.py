import pandas as pd
import streamlit as st
import numpy as np
from st_functions import st_button, load_css
from PIL import Image
import streamlit.components.v1 as components

def inject_ga():
    """Add this in your streamlit app.py
    see https://github.com/streamlit/streamlit/issues/969
    """
    # new tag method
    GA_ID = "google_analytics"
    # NOTE: you should add id="google_analytics" value in the GA script
    # https://developers.google.com/analytics/devguides/collection/analyticsjs
    GA_JS = """
<!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ECZ57RBDL6"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-ECZ57RBDL6');
  </script>
"""
    # Insert the script in the head tag of the static template inside your virtual
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    logging.info(f'editing {index_path}')
    soup = BeautifulSoup(index_path.read_text(), features="lxml")
    if not soup.find(id=GA_ID):  # if cannot find tag
        bck_index = index_path.with_suffix('.bck')
        if bck_index.exists():
            shutil.copy(bck_index, index_path)  # recover from backup
        else:
            shutil.copy(index_path, bck_index)  # keep a backup
        html = str(soup)
        new_html = html.replace('<head>', '<head>\n' + GA_JS)
        index_path.write_text(new_html)

def main():
  
  inject_ga()
  
  st.set_page_config(
     page_title="Navy Links",
     page_icon="🔗",  
  )
  
  components.html('''
    <head>
    <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ECZ57RBDL6"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-ECZ57RBDL6');
  </script>
  </head>
  ''')

  load_css()

  st.header('Navy Links')

  col1, col2 = st.columns(2)

  icon_size = 20

  with col1:

    st.header('Flight Ops')
  
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

  st.write('')
  st.write('')
  st.write('')
  st.write('')
  st.write('')
  st.write('')
  st.write('')
  st.write('')

  col3, col4, col5 = st.columns(3)

  with col4:
    st_button('cup', 'https://www.buymeacoffee.com/hegerjl', 'Buy me a Coffee', icon_size)
    
if __name__ == "__main__":
  main()
