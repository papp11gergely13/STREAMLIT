import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder

AgGrid(
    df.head(50),
    gridOptions=GridOptionsBuilder.from_dataframe(df).build(),
)
