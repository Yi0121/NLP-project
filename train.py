from utils.data_loader import load_all_dataset
datasets = load_all_dataset(data_dir='data')
# print(datasets)
imdb_df = datasets['IMDB Dataset.csv']
youtube_comments_df = datasets['YoutubeCommentsDataSet.csv']

