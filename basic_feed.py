import tensorflow as tf

#  a feed temporarily replaces the output of an operation with a tensor value
#  you supply feed data as an argument to a run call
#  the most common use is to use placeholder operations
#  placeholder operations supply an error if you do not supply a feed for them
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.mul(input1, input2)

with tf.Session() as sess:
    print(sess.run([output], feed_dict={input1:[7.], input2:[2.]}))
