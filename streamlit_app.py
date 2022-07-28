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

  st.info('Useful Webpage Links')

  icon_size = 20
  
  st_button('clipboard', 'https://asm3.nmci.navy.mil/ASM3/cac?utm_source=mnp%20public', 'ASM', icon_size)

  st_button('cup', 'https://www.buymeacoffee.com/hegerjl', 'Buy me a Coffee', icon_size)
  

if __name__ == "__main__":
  main()
