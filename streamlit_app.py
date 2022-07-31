import pandas as pd
import streamlit as st
import numpy as np
from st_functions import st_button, load_css
from PIL import Image

def main():
  
  st.set_page_config(
     page_title="Navy Links",
     page_icon="🔗",
)
  
  load_css()

  col1, col2, col3 = st.columns(3)
  #col2.image(Image.open('dp.png'))

  st.header('Navy Links')

  #st.info('Useful Webpage Links')

  icon_size = 20
  
  st_button('clipboard', 'https://asm3.nmci.navy.mil/ASM3/cac?utm_source=mnp%20public', 'ASM', icon_size)
  st_button('person', 'https://www.bol.navy.mil/bam/?utm_source=mnp%20public', 'BOL', icon_size)
  st_button('airplane', 'https://dtsproweb.defensetravel.osd.mil/dts-app/pubsite/all/view/?utm_source=mnp%20public', 'DTS', icon_size)
  st_button('safe', 'https://safe.apps.mil/', 'DoD Safe', icon_size)
  st_button('book', 'https://jkodirect.jten.mil/Atlas2/page/login/Login.jsf', 'JKO', icon_size)
  st_button('health', 'https://www.health.mil/Military-Health-Topics/MHS-Transformation/MHS-GENESIS', 'MHS GENESIS Patient Portal', icon_size)
  st_button('connect', 'https://milconnect.dmdc.osd.mil/milconnect/', 'milConnect', icon_size)
  st_button('money', 'https://mypay.dfas.mil/#/', 'myPay', icon_size)
  st_button('info', 'https://navyfamily.navy.mil/cas/login?service?utm_source=mnp%20public', 'NFAAS', icon_size)
  st_button('person', 'https://www.nsips.navy.mil/?utm_source=mnp%20public', 'NSIPS', icon_size)
  st_button('fitness', 'https://www.mnp.navy.mil/group/performance/parfq?utm_source=mnp%20public', 'PARFQ', icon_size)
  st_button('stats', 'https://www.mnp.navy.mil/group/performance/prims?utm_source=mnp%20public', 'PRIMS', icon_size)
  st_button('appointment', 'https://idco.dmdc.osd.mil/idco/?utm_source=mnp%20public', 'RAPIDS ID', icon_size)
  st_button('sharp', 'https://sharp.dc3n.navy.mil/?utm_source=mnp%20public', 'SHARP', icon_size)
  st_button('invest', 'https://www.tsp.gov/?utm_source=mnp%20public', 'TSP', icon_size)
  
  st_button('cup', 'https://www.buymeacoffee.com/hegerjl', 'Buy me a Coffee', icon_size)
  

if __name__ == "__main__":
  main()
