import tensorflow as tf

#  this creates a 1x2 constant operation
matrix1 = tf.constant([[3., 3,]])
#  this creates a 2x1 constant operation
matrix2 = tf.constant([[2.], [2.]])

#  create a matmul op that takes matrix1 and matrix2 as input
#  the return value product represents the matrix multiplication
product = tf.matmul(matrix1, matrix2)

#  resulting graph has 3 nodes or operations
#  two constant operations which are graphs
#  one matmul operation which takes the two constant operations as input and
#  outputs the multiplication of the matrices

#  launch the default graph
sess = tf.Session()

#  we can run this computation by calling the end operation product which in
#  turns calls all the children operation
result = sess.run(product)
print(result)

#  now we close the session when we are done
sess.close()
