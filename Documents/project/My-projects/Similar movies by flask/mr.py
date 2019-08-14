class mr:
    def mrf(movie_name):
        import seaborn as sns
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np
        from sklearn.datasets import load_breast_cancer
        user=pd.read_csv("C:/Users/nikhi/Desktop/btch1pm/MachineLearning/knn/ml-100k/u.data",sep='\t',names=['user id','movie id','rating','timestamp'])
        user['timestamp']=user['timestamp'].apply(lambda x: pd.Timestamp(x).date())
        movie=pd.read_csv("C:/Users/nikhi/Desktop/btch1pm/MachineLearning/knn/ml-100k/u.item",sep='|',encoding='latin')
        geners = [ "movie id","movie title","Action", "Adventure","Animation","Children's","Comedy","Crime","Documentary","Drama","Fantasy","Film-Noir","Horror","Musical", "Mystery","Romance","Sci-Fi","Thriller", "War","Western" ]
        index=[i for i in range(24)]
        index.remove(2),index.remove(3),index.remove(4),index.remove(5)
        movie = pd.read_csv("C:/Users/nikhi/Desktop/btch1pm/MachineLearning/knn/ml-100k/u.item",names=geners,encoding='latin',sep='|',usecols=index)
        new_df=user.join(movie[['movie id','movie title']],on="movie id",how='inner',lsuffix="1" )

        new_df.drop('timestamp',axis=1,inplace=True)
        new_df.drop(["movie id1","movie id"],axis=1,inplace=True)
        data = new_df.reindex(index=range(len(new_df)))
        #data.groupby('movie title')['rating'].count().sort_values(ascending=False)[:20].plot(kind='bar')
        data.groupby("movie title").agg({"rating": np.mean})
        

        "C:/Users/nikhi/Desktop/btch1pm/MachineLearning/knn/ml-100k/u.data"
        import pandas as pd
        import os
        r_cols = ['user_id', 'movie_id', 'rating']
        ratings = pd.read_csv(os.path.join("C:/Users/nikhi/Desktop/btch1pm/MachineLearning/knn/ml-100k/u.data"), sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")
        
        m_cols = ['movie_id', 'title']
        movies = pd.read_csv(os.path.join("C:/Users/nikhi/Desktop/btch1pm/MachineLearning/knn/ml-100k/u.item"), sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")
        
        ratings = pd.merge(movies, ratings)
        movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
        starwars=movieRatings[movie_name]
        similarstarwar=movieRatings.corrwith(starwars)
        #similarstarwar.head()
        similarstarwar=similarstarwar.dropna()
        df=pd.DataFrame(similarstarwar)
        print("DF is\n")
        #df.sort_values(by='similarity',ascending=False).head()
        df.sort_values(by=0,ascending=False)
        movieStats=ratings.groupby(by='title').agg({'rating' :[np.size,np.mean]})
        popularMovies = movieStats['rating']['size'] >= 100
        #movieStats.sort_values([('rating', 'size')],ascending=False)
        df = movieStats[popularMovies].join(pd.DataFrame(similarstarwar, columns=['similarity']))
        print("\n\n\n\n")
        simtemp=df.sort_values(by='similarity',ascending=False).head()
        simtemp=np.array(simtemp.index)
        print(simtemp)
        import os
        import matplotlib.pyplot as plt
        try:
              os.remove("C:\\Users\\nikhi\\Desktop\\myflask\\static\\img.png")
        except:
                pass
        dfnew1=df.sort_values(by='similarity',ascending=False).head()
        dfnew1=df.sort_values(by='similarity',ascending=False).head()
        dfnew1.plot(y=('rating', 'mean'),kind='bar',color='green',title="Rating Plot")
        #plt.show()
        movie_name=movie_name.replace(" ","")
        plt.savefig(f'C:\\Users\\nikhi\\Documents\\Python Scripts\\myflask\\static\\{movie_name}.png')
        return simtemp




                
