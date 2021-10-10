import pandas as pd
import tensorflow as tf
import tensorflow.keras
#from keras.models import Sequential
#from keras.layers import *

training_data = pd.read_csv("sales_data_training_scaled.csv")

train_features = training_data.drop('total_earnings', axis=1).values
train_labels = training_data[['total_earnings']].values

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(50, input_dim=9, activation='relu'),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(1,activation='linear')
])

# Training the model
model.compile(optimizer='adam', loss = 'mean_squared_error')
model.fit(train_features, train_labels, epochs=50, shuffle=2, verbose=2)
#model.summary()

# Test the model
test_data=pd.read_csv("sales_data_test_scaled.csv")
test_features= test_data.drop('total_earnings', axis=1).values
test_labels = test_data['total_earnings'].values
test_error_rate = model.evaluate(test_features, test_labels, verbose=0)
print("The mean squared error for the test data is: {}".format(test_error_rate))
