import tensorflow_datasets as tfds
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

(train_data, train_labels), (test_data, test_labels) = tfds.load('tiny_shakespeare', split='train', with_info=True)