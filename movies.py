import pandas as pd 
df = pd.read_csv("imdb_top_1000.csv")

df.drop_duplicates(subset=['Series_Title', 'Director'], keep='first', inplace=True) #you can remove any duplicates you have in the file for title and director name 

# define directors for your directors table and get the unique directors and give them ids
directors = df[['Director']].drop_duplicates().reset_index(drop=True) 
directors['director_id'] = range(1, len(directors) + 1) 
directors.to_csv("directors.csv", index=False)  #save it into a csv file

# you can do a similar thing like above for movies
movies =df[['Series_Title']].drop_duplicates().reset_index(drop=True) 
movies['movie_id'] = range(1, len(movies) + 1) 
movies.to_csv("movies.csv", index=False) 

# define genres for genres table and get the unique genres and give them ids
genres =df[['Genre']].drop_duplicates().reset_index(drop=True) 
genres['genre_id'] = range(1, len(genres) + 1) 
genres.to_csv("genres.csv", index=False) 

# define actors for actors table and get the unque actors and give them ids
# Combine the columns and drop duplicates
actors = pd.concat([df['Star1'], df['Star2'], df['Star3'], df['Star4']]).drop_duplicates().reset_index(drop=True)
actors_df = pd.DataFrame(actors, columns=['Actor'])
actors_df['actor_id'] = range(1, len(actors_df) + 1)
actors_df.to_csv("actors.csv", index=False)

# movie-director relationship table by merging df with director id
df = df.merge(directors, on='Director', how='left')

# Merge with movie_id
df = df.merge(movies, on='Series_Title', how='left')

# Select only necessary columns for the relationship table
movie_director = df[['movie_id', 'director_id']].drop_duplicates()
movie_director.to_csv("movie_director.csv", index=False)

#you can then easily use the director_id column and movie_id column to create that relationship table you were trying to create
movie_director = df[['movie_id', 'director_id']].drop_duplicates()

# Creating movie_genre table
df = df.merge(genres, on='Genre', how='left')
movie_genre = df[['movie_id', 'genre_id']].drop_duplicates()
movie_genre.to_csv("movie_genre.csv", index=False)
movie_genre = df[['movie_id', 'genre_id']].drop_duplicates()

# # Creating movie_actor table
# movies = pd.read_csv("movies.csv")
# actors_df = pd.read_csv("actors.csv")

# df = df.merge(movies, left_on='Series_Title', right_on='Series_Title', how='left')
# melted_df = df.melt(id_vars=['movie_id'], value_vars=['Star1', 'Star2', 'Star3', 'Star4'], var_name='Star Position', value_name='Actor')
# movie_actor_df = melted_df.merge(actors_df, on='Actor', how='left')[['movie_id', 'actor_id']]
# movie_actor_df.to_csv("movie_actor.csv", index=False)