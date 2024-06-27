# -*- coding: utf-8 -*-
"""deploy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14VMahl8AQIj92DBafk1IhgBspHvsQkyM
"""

!pip install pycocotools
from pycocotools.coco import COCO

!pip install -q streamlit

!pip install pyngrok

!ngrok authtoken 2Yi4DSioJ5bwBStYEuIppgZZ04t_VyBoGrdpspNPE7ZsDW2Q

from pyngrok import ngrok

# Open a ngrok tunnel to the HTTP server on port 8501
public_url = ngrok.connect()
print(' * ngrok tunnel "{}" -> "http://127.0.0.1:{}/"'.format(public_url, 8501))

!streamlit run UI.py & npx localtunnel --port 8501

