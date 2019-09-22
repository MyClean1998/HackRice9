import numpy as np
import tensorflow as tf

class QScoreModel:

    def __init__(self, num_features, lr, sess):
        self.sess = sess
        self.num_features = num_features
        self.learning_rate = lr
        self.features = tf.placeholder(tf.float32, [num_features])
        self.expected_q = tf.placeholder(tf.float32, shape=())

    def forward(self, features):
        raise Exception("Forward method must be implemented by subclasses.")
    
    def backward(self, loss):
        raise Exception("Forward method must be implemented by subclasses.")

class LinearQScore(QScoreModel):
    
    def __init__(self, num_features, lr, sess):
        super().__init__(num_features, lr, sess)
        self.weights = tf.Variable(tf.random_normal(shape=[self.num_features]))
        self.forward_q = tf.tensordot(self.weights, self.features, 1)
        print(self.forward_q.shape)
        self.loss = (self.expected_q - self.forward_q) ** 2
        self.optimizer = tf.train.GradientDescentOptimizer(self.learning_rate).minimize(self.loss)
    
    def forward(self, features):
        return self.sess.run(self.forward_q, feed_dict={self.features: features})
    
    def backward(self, expected, features):
        self.sess.run([self.optimizer, self.loss],
            feed_dict={self.features: features, self.expected_q: expected})