import tensorflow as tf

#  create a variable, that will be initialized to the scalar value 0
state = tf.Variable(0, name="counter")

#  create an operation that adds one to state
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

#  variables must be initialized by running an init Op after having launched
#  the graph.
init_op = tf.initialize_all_variables()

#  now we launch the graph and run the ops
with tf.Session() as sess:
    sess.run(init_op)
    #  print initial value of state
    print(sess.run(state))
    for x in range(3):
        sess.run(update)
        print(sess.run(state))
