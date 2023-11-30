import streamlit as st
import st_aggrid as sta

AgGrid(
    df.head(50),
    gridOptions=GridOptionsBuilder.from_dataframe(df).build(),
)
