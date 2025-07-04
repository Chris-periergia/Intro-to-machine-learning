
# Exercises
# Step 1: Split Your Data
# Use the train_test_split function to split up your data.

# Give it the argument random_state=1 so the check functions know what to expect when verifying your code.

# Recall, your features are loaded in the DataFrame X and your target is loaded in y.

# Import the train_test_split function and uncomment
from sklearn.model_selection import train_test_split

# fill in and uncomment
train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=1)

# Check your answer
step_1.check()

# Step 2: Specify and Fit the Model
# Create a DecisionTreeRegressor model and fit it to the relevant data. Set random_state to 1 again when creating the model.

# You imported DecisionTreeRegressor in your last exercise
# and that code has been copied to the setup code above. So, no need to
# import it again

# Specify the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit iowa_model with the training data.
iowa_model.fit(train_X,train_y)

# Check your answer
step_2.check()

# Step 3: Make Predictions with Validation data

# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)

# Check your answer
step_3.check()


# Inspect your predictions and actual values from validation data.

# print the top few validation predictions
print(iowa_model.predict(X.head()))
# print the top few actual prices from validation data
print(y.head().tolist())

# Step 4: Calculate the Mean Absolute Error in Validation Data

from sklearn.metrics import mean_absolute_error
val_mae = mean_absolute_error(val_y,val_predictions)

# uncomment following line to see the validation_mae
print(val_mae)

# Check your answer
step_4.check()