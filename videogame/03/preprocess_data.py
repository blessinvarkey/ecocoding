import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Training data set from CSV file
training_data = "sales_data_training.csv"

# Testing data set from CSV file
test_data ="sales_data_test.csv"

# Data needs to be scaled to a small range like 0 to 1 for the neural
# network to work well.
scaler = MinMaxScaler(feature_range=(0,1))

# Scaling both the training inputs and outputs
scaled_training = scaler.fit_transform(training_data)
scaled_testing = scaler.fit_transform(test_data)

# Print out the adjustment that the scaler applied to the total_earnings column of data
print("Note: total_earnings values were scaled by multiplying by {:.10f} and adding {:.6f}".format(scaler.scale_[8], scaler.min_[8]))

# Create new pandas DataFrame objects from the scaled data
scaled_training_df = pd.DataFrame(scaled_training, columns=training_data.columns.values)
scaled_testing_df = pd.DataFrame(scaled_testing, columns=test_data.columns.values)

# Save scaled data dataframes to new CSV files
scaled_training_df.to_csv("sales_data_training_scaled.csv", index=False)
scaled_testing_df.to_csv("sales_data_test_scaled.csv", index=False)