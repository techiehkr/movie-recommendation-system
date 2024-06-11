import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise.accuracy import rmse
from web.models import Myrating
def Myrecommend():
    # Load data from the Django model
    df = pd.DataFrame(list(Myrating.objects.all().values()))
    
    # Prepare the data for Surprise
    reader = Reader(rating_scale=(1, 5))  # assuming ratings are between 1 and 5
    data = Dataset.load_from_df(df[['user_id', 'movie_id', 'rating']], reader)
    
    # Split the data into training and test sets
    trainset, testset = train_test_split(data, test_size=0.25)
    
    # Use the SVD algorithm
    algo = SVD()
    
    # Train the algorithm on the trainset
    algo.fit(trainset)
    
    # Test the algorithm on the testset
    predictions = algo.test(testset)
    
    # Compute and print RMSE
    rmse(predictions)
    
    # Normalize the ratings
    # Calculate mean ratings for each movie
    Ymean = df.groupby('movie_id')['rating'].mean().values
    
    # Making predictions for all users and items
    all_predictions = []
    for uid in df['user_id'].unique():
        for iid in df['movie_id'].unique():
            est = algo.predict(uid, iid).est
            all_predictions.append((uid, iid, est))
    
    # Convert predictions to a DataFrame
    pred_df = pd.DataFrame(all_predictions, columns=['user_id', 'movie_id', 'pred_rating'])
    
    # Reshape the predictions into the same format as the original Y matrix
    prediction_matrix = pred_df.pivot(index='movie_id', columns='user_id', values='pred_rating').fillna(0).values
    
    return prediction_matrix, Ymean




