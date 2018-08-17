# Keras examples directory

## Vision models examples

- [mnist_mlp.ipynb](mnist_mlp.ipynb)
Trains a simple deep multi-layer perceptron on the MNIST dataset.

- [mnist_cnn.ipynb](mnist_cnn.ipynb)
Trains a simple convnet on the MNIST dataset.

- [cifar10_cnn.ipynb](cifar10_cnn.ipynb)
Trains a simple deep CNN on the CIFAR10 small images dataset.

- [cifar10_resnet.ipynb](cifar10_resnet.ipynb)
Trains a ResNet on the CIFAR10 small images dataset.

- [conv_lstm.ipynb](conv_lstm.ipynb)
Demonstrates the use of a convolutional LSTM network.

- [image_ocr.ipynb](image_ocr.ipynb)
Trains a convolutional stack followed by a recurrent stack and a CTC logloss function to perform optical character recognition (OCR).

- [mnist_acgan.ipynb](mnist_acgan.ipynb)
Implementation of AC-GAN (Auxiliary Classifier GAN) on the MNIST dataset

- [mnist_hierarchical_rnn.ipynb](mnist_hierarchical_rnn.ipynb)
Trains a Hierarchical RNN (HRNN) to classify MNIST digits.

- [mnist_siamese.ipynb](mnist_siamese.ipynb)
Trains a Siamese multi-layer perceptron on pairs of digits from the MNIST dataset.

- [mnist_swwae.ipynb](mnist_swwae.ipynb)
Trains a Stacked What-Where AutoEncoder built on residual blocks on the MNIST dataset.

- [mnist_transfer_cnn.ipynb](mnist_transfer_cnn.ipynb)
Transfer learning toy example.

----

## Text & sequences examples

- [addition_rnn.ipynb](addition_rnn.ipynb)
Implementation of sequence to sequence learning for performing addition of two numbers (as strings).

- [babi_rnn.ipynb](babi_rnn.ipynb)
Trains a two-branch recurrent network on the bAbI dataset for reading comprehension.

- [babi_memnn.ipynb](babi_memnn.ipynb)
Trains a memory network on the bAbI dataset for reading comprehension.

- [imdb_bidirectional_lstm.ipynb](imdb_bidirectional_lstm.ipynb)
Trains a Bidirectional LSTM on the IMDB sentiment classification task.

- [imdb_cnn.ipynb](imdb_cnn.ipynb)
Demonstrates the use of Convolution1D for text classification.

- [imdb_cnn_lstm.ipynb](imdb_cnn_lstm.ipynb)
Trains a convolutional stack followed by a recurrent stack network on the IMDB sentiment classification task.

- [imdb_fasttext.ipynb](imdb_fasttext.ipynb)
Trains a FastText model on the IMDB sentiment classification task.

- [imdb_lstm.ipynb](imdb_lstm.ipynb)
Trains an LSTM model on the IMDB sentiment classification task.

- [lstm_stateful.ipynb](lstm_stateful.ipynb)
Demonstrates how to use stateful RNNs to model long sequences efficiently.

- [pretrained_word_embeddings.ipynb](pretrained_word_embeddings.ipynb)
Loads pre-trained word embeddings (GloVe embeddings) into a frozen Keras Embedding layer, and uses it to train a text classification model on the 20 Newsgroup dataset.

- [reuters_mlp.ipynb](reuters_mlp.ipynb)
Trains and evaluate a simple MLP on the Reuters newswire topic classification task.

----

## Generative models examples

- [lstm_text_generation.ipynb](lstm_text_generation.ipynb)
Generates text from Nietzsche's writings.

- [conv_filter_visualization.ipynb](conv_filter_visualization.ipynb)
Visualization of the filters of VGG16, via gradient ascent in input space.

- [deep_dream.ipynb](deep_dream.ipynb)
Deep Dreams in Keras.

- [neural_doodle.ipynb](neural_doodle.ipynb)
Neural doodle.

- [neural_style_transfer.ipynb](neural_style_transfer.ipynb)
Neural style transfer.

- [variational_autoencoder.ipynb](variational_autoencoder.ipynb)
Demonstrates how to build a variational autoencoder.

- [variational_autoencoder_deconv.ipynb](variational_autoencoder_deconv.ipynb)
Demonstrates how to build a variational autoencoder with Keras using deconvolution layers.

----

## Examples demonstrating specific Keras functionality

- [antirectifier.ipynb](antirectifier.ipynb)
Demonstrates how to write custom layers for Keras.

- [mnist_sklearn_wrapper.ipynb](mnist_sklearn_wrapper.ipynb)
Demonstrates how to use the sklearn wrapper.

- [mnist_irnn.ipynb](mnist_irnn.ipynb)
Reproduction of the IRNN experiment with pixel-by-pixel sequential MNIST in "A Simple Way to Initialize Recurrent Networks of Rectified Linear Units" by Le et al.

- [mnist_net2net.ipynb](mnist_net2net.ipynb)
Reproduction of the Net2Net experiment with MNIST in "Net2Net: Accelerating Learning via Knowledge Transfer".

- [reuters_mlp_relu_vs_selu.ipynb](reuters_mlp_relu_vs_selu.ipynb)
Compares self-normalizing MLPs with regular MLPs.

- [mnist_tfrecord.ipynb](mnist_tfrecord.ipynb)
MNIST dataset with TFRecords, the standard TensorFlow data format.

- [mnist_dataset_api.ipynb](mnist_dataset_api.ipynb)
MNIST dataset with TensorFlow's Dataset API.