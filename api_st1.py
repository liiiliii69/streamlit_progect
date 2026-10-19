import streamlit as st
import app_api1

st.title("API STREAMLIT")
option = st.sidebar.selectbox("Select Your Option",
       ("GENRES","MOVIE LIST BY GENRE"))
       
if option == "GENRES":
    if st.button('Display Info'):
        result = app_api1.get_Genres()
        if result != "Error":
            st.write(result)
        else:
            st.error("Info Not Found")       

elif option ==  "MOVIE LIST BY GENRE":
    genre_id = st.number_input("enter genre id",min_value=1) 
    movie_page = st.number_input("enter movie list page",min_value=1)
    if st.button('Display Info'):
        result = app_api1.get_Movie_list_byGenre(genre_id,movie_page)
        if result != "Error":
            st.write(result)
        else:
            st.error("Info Not Found")


 
