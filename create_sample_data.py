import pandas as pd
import numpy as np
import os

# Create sample flight data with realistic price correlations
np.random.seed(42)

n_samples = 2000

# Define categories
airlines = ['SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India']
cities = ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai']
times = ['Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night']
stops_list = ['zero', 'one', 'two_or_more']
classes = ['Economy', 'Business']

# Create random selections
airline = np.random.choice(airlines, n_samples)
source_city = np.random.choice(cities, n_samples)
departure_time = np.random.choice(times, n_samples)
stops = np.random.choice(stops_list, n_samples)
arrival_time = np.random.choice(times, n_samples)
destination_city = np.random.choice(cities, n_samples)
classs = np.random.choice(classes, n_samples)

# Generate duration and days_left with realistic ranges
duration = np.random.uniform(1, 12, n_samples)
days_left = np.random.randint(1, 60, n_samples)

# Generate price based on features (realistic correlations)
base_price = 10000.0  # Use float

# Add price based on class (Business class = higher price)
price = np.where(classs == 'Business', base_price + 15000, base_price).astype(float)

# Add price based on number of stops (more stops = cheaper)
price = price + np.where(stops == 'zero', 5000, 
                  np.where(stops == 'one', 2000, 0)).astype(float)

# Add price based on duration (longer flights = higher price)
price = price + duration * 1000

# Add price based on days left (less days = more expensive)
price = price + (60 - days_left) * 150

# Add price based on airline (some airlines more expensive)
airline_price = {
    'Air_India': 2000,
    'Vistara': 1500,
    'Indigo': 500,
    'SpiceJet': 200,
    'AirAsia': 100,
    'GO_FIRST': 0
}
price = price + np.array([airline_price.get(a, 0) for a in airline], dtype=float)

# Add some random noise
price += np.random.normal(0, 1500, n_samples)

# Ensure price is positive
price = np.maximum(price, 3000)

# Create DataFrame
data = {
    'Unnamed: 0': range(n_samples),
    'airline': airline,
    'source_city': source_city,
    'departure_time': departure_time,
    'stops': stops,
    'arrival_time': arrival_time,
    'destination_city': destination_city,
    'classs': classs,
    'duration': duration,
    'days_left': days_left,
    'price': price,
}

df = pd.DataFrame(data)

# Create the directory if it doesn't exist
os.makedirs('Notebook_Experiments/Data', exist_ok=True)

# Save the data
df.to_csv('Notebook_Experiments/Data/data.csv', index=False)
print(f"Sample data created successfully with {n_samples} records")
print("\nData Statistics:")
print(f"Price range: ${df['price'].min():.2f} to ${df['price'].max():.2f}")
print(f"Price mean: ${df['price'].mean():.2f}")
print(f"Price std: ${df['price'].std():.2f}")
print("\nFirst few rows:")
print(df.head(10))
