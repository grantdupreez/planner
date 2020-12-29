#Prices of housing in the UK

import pydeck as pdk
import pandas as pd

CPU_GRID_LAYER_DATA = (
    "https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK_House_price_index.xlsx"
)
df = pd.read_excel(CPU_GRID_LAYER_DATA)

# Define a layer to display on a map

layer = pdk.Layer(
    "GridLayer", df, pickable=True, extruded=True, cell_size=200, elevation_scale=4, get_position="COORDINATES",
)

view_state = pdk.ViewState(latitude=52.2323, longitude=-1.415, zoom=6, bearing=0, pitch=45)

# Render
r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{position}\nCount: {count}"},)
r.to_html("grid_layer.html")
