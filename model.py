import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import PIL
import pathlib
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

train_data_dir = pathlib.Path('/mnt/c/Users/maxxt/Downloads/Projects/Poker Reader/archive/train')
test_data_dir = pathlib.Path('/mnt/c/Users/maxxt/Downloads/Projects/Poker Reader/archive/test')

train_data_labels = pd.read_csv('/mnt/c/Users/maxxt/Downloads/Projects/Poker Reader/archive/Training_set.csv')['label'].tolist()
test_data_labels = pd.read_csv('/mnt/c/Users/maxxt/Downloads/Projects/Poker Reader/archive/Training_set.csv')['label'].tolist()

batch_size = 32
img_height = 224
img_width = 224

train_ds = tf.keras.utils.image_dataset_from_directory(
	train_data_dir,
	labels=train_data_labels,
	label_mode='categorical',
	seed=123,
	image_size=(img_height, img_width),
	batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory(
	test_data_dir,
	labels=test_data_labels,
	label_mode='categorical',
	seed=123,
	image_size=(img_height, img_width),
	batch_size=batch_size)

