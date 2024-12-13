import pandas as pd
from src.data_loading import load_historical_datasets, load_raw_analyst_ratings
from src.data_cleaning import standardize_columns, handle_missing_values, convert_dates
from src.data_analysis import analyze_text_lengths, count_articles_by_publisher, extract_top_keywords
from src.sentiment_analysis import calculate_sentiment
from src.visualization import plot_publication_trends, plot_sentiment_distribution

# File paths
file_paths = [
    'Data/yfinance_data/AAPL_historical_data.csv',
    'Data/yfinance_data/AMZN_historical_data.csv',
    'Data/yfinance_data/GOOG_historical_data.csv',
    'Data/yfinance_data/META_historical_data.csv',
    'Data/yfinance_data/MSFT_historical_data.csv',
    'Data/yfinance_data/NVDA_historical_data.csv',
    'Data/yfinance_data/TSLA_historical_data.csv',
]
raw_ratings_path = 'Data/raw_analyst_ratings.csv'

# Load data
datasets = load_historical_datasets(file_paths)
raw_ratings = load_raw_analyst_ratings(raw_ratings_path)

# Clean data
datasets = standardize_columns(datasets)
datasets = handle_missing_values(datasets)
datasets = convert_dates(datasets)

# Combine datasets
historical_data = pd.concat(datasets.values(), ignore_index=True)

# Descriptive Statistics
headline_stats = analyze_text_lengths(raw_ratings, 'headline')
print("Headline Length Statistics:", headline_stats)

publisher_counts = count_articles_by_publisher(raw_ratings, 'publisher')
print("Top Publishers:\n", publisher_counts)

# Text Analysis
raw_ratings = calculate_sentiment(raw_ratings, 'headline')
top_keywords = extract_top_keywords(raw_ratings, 'headline', top_n=10)
print("Top Keywords:\n", top_keywords)

# Visualizations
plot_publication_trends(raw_ratings, 'date')
plot_sentiment_distribution(raw_ratings, 'sentiment')
