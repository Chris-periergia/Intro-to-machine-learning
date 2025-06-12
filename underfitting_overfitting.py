
# Step 1: Compare Different Tree Sizes¶
# Write a loop that tries the following values for max_leaf_nodes from a set of possible values.

# Call the get_mae function on each value of max_leaf_nodes. Store the output in some way that allows you to select the value of max_leaf_nodes that gives the most accurate model on your data.

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
# Write loop to find the ideal tree size from candidate_max_leaf_nodes
mae_values={}
for size in candidate_max_leaf_nodes:
# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
    best_tree_size = get_mae(size,train_X, val_X, train_y, val_y)
    mae_values[size]=best_tree_size
    
best_tree_size=min(mae_values,key=mae_values.get)    
   
# Step 2: Fit Model Using All Data
# You know the best tree size. If you were going to deploy this model in practice, you would make it even more accurate by using all of the data and keeping that tree size. That is, you don't need to hold out the validation data now that you've made all your modeling decisions.

# Fill in argument to make optimal size and uncomment
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size,random_state=0)

# fit the final model and uncomment the next two lines
final_model.fit(X, y)

