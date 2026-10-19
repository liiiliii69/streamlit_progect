import requests

def get_MovieInfo_ByID(movie_id):
    url = f'https://moviesapi.ir/api/v1/movies/{movie_id}'
    response = requests.get(url)
    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()
        title = response['title']
        year = response['year']
        director = response['director']
        imdb_rate = response['imdb_rating']
        genres = response['genres']
        return title, year, director, imdb_rate, genres
#------------------------------------------------------




#############################################
def get_MovieInfo_ByName(movie_name):
    url = 'https://moviesapi.ir/api/v1/movies'

    params = {'q':movie_name}

    response = requests.get(url , params=params)
    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()
        response = response['data'][0]
        title = response['title']
        year = response['year']
        country = response['country']
        imdb_rate = response['imdb_rating']
        genres = response['genres']
        return title, year, country, imdb_rate, genres
##############################################################
def get_Movie_list(movie_page=2):
    url =f'https://moviesapi.ir/api/v1/movies'
    api_parameters={'page':movie_page}
    response = requests.get(url,params=api_parameters)

    if response.status_code != 200:
        return "Error"
    else: 
        output=[]   
        response = response.json()
        response=response["data"]
        for item in response:
            title =item ['title']
            year =item  ['year']
            poster =item  ['poster']
            imdb_rate = item ['imdb_rating']
            output.append([title, year, poster, imdb_rate])    
        return output
########################################

'''def get_MovieInfo_ByGenreID(genre_id):
    url = f'https://moviesapi.ir/api/v1/genres/{genre_id}'
    response = requests.get(url)

    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()

        title = response['title']
        poster = response['poster']
        genres = response['genres']
        return title, poster,genres'''
        

#######################################################
if __name__ == '__main__':
    #movie_id = input('enter movei id: ')
    #result = get_MovieInfo_ByID(movie_id)
    movie_name=input('enter movei name: ')
    result = get_MovieInfo_ByName(movie_name)
    #result =get_Movie_list(movie_page=2) 
    #genre_id=input("enter genre_id ")
    #result = get_MovieInfo_ByGenreID(genre_id)
    print('result: ', result)