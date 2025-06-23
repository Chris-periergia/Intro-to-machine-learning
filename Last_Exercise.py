
# Train a model for the competition
# The code cell above trains a Random Forest model on train_X and train_y.

# Use the code cell below to build a Random Forest model and train it on all of X and y.



# To improve accuracy, create a new Random Forest model which you will train on all training data
rf_model_on_full_data = RandomForestRegressor(random_state=1)


# fit rf_model_on_full_data on all data from the training data
rf_model_on_full_data.fit(X,y)


# Now, read the file of "test" data, and apply your model to make predictions.

import pandas as pd
# path to file you will use for predictions
test_data_path = '../input/test.csv'

# read test data file using pandas
test_data = pd.read_csv(test_data_path)

# create test_X which comes from test_data but includes only the columns you used for prediction.
# The list of columns is stored in a variable called features
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

test_X = test_data[features]

# make predictions which we will submit. 
test_preds = rf_model_on_full_data.predict(test_X)