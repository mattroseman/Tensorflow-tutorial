import input_data

#  this data is split into 3 groups
#  55,000 data points - training data
#  10,000 data points - test data
#  5,000 data points - validation data
#  every data point also has two different parts
#   the image of handwritten data
#   and the corresponding label
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
