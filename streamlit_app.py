import streamlit as st
from sherpa_streamlit import visualize

default_text = """This is a sample text.
With two lines.
"""
visualize(default_text,
          sidebar_title="KAIRNTECH Sherpa",
          sidebar_description="Demonstation page")
