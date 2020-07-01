import tensorflow as tf


if __name__ == "__main__":
    print(tf.__version__)
    print(tf.test.gpu_device_name())
