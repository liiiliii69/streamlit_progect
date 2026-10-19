import streamlit as st
import app_api

st.title('API STREAMLIT')
option = st.sidebar.selectbox('Select Your Option'
    ,('MOVIE API BY ID', 'MOVIE API BY NAME','MOVIE LIST BY PAGE'))

if option == 'MOVIE API BY ID':
    movie_id = st.number_input('enter movie id', min_value=1, max_value=250)
    if st.button('Display Info'):
        result = app_api.get_MovieInfo_ByID(movie_id)
        if result != 'ERROR':
            st.write(result)
        else:
            st.error('INFO NOT FOUND')

elif option == 'MOVIE API BY NAME':
    movie_name = st.text_input('enter movie name: ')
    if st.button('Display Info'):
        result = app_api.get_MovieInfo_ByName(movie_name)
        if result != 'ERROR':
            st.write(result)
        else:
            st.error('INFO NOT FOUND')
elif option == 'MOVIE LIST BY PAGE':
    movie_page = st.number_input('enter movie list page: ',min_value=1 ,max_value=25)
    if st.button('Display Info'):
        result = app_api.get_Movie_list(movie_page)
        if result != 'ERROR':
            st.write(result)
        else:
            st.error('INFO NOT FOUND')


'''elif option == 'Movie By Genre ID ':
    genre_id = st.number_input('enter genre_id', min_value=1, max_value=250)
    if st.button('Display Info'):
        result = app_api.get_MovieInfo_ByGenreID(genre_id)

        if result != 'ERROR':
            st.write(result)
        else:
            st.error('INFO NOT FOUND') '''   
        





        

                              