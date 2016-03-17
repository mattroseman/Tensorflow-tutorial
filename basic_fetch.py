import tensorflow as tf

input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
intermed = tf.add(input2, input3)
mul = tf.mul(input1, intermed)

with tf.Session() as sess:
    #  result is a rank 1 tensor that contains
    #  [input1 * (input2 + input3), input2 + input3]
    result = sess.run([mul, intermed])
    #  as soon as mul and intermed is run the value is set and it is not run
    #  again, so input2 + input3 is computed for mul and doesn't get computed
    #  again
    print(result)
