
# Notes


## TensorFlow Keras Notes

### Epochs and Batch

Given this code from Keras:

```
model.fit(train_df, train_labels, epochs=5, batch_size=128)
```
According to `Deep Learning with Python` this means:
* the model is fitted with the entire set of data five times (`epochs=5`)
* Each iteration of model training/ft, 128 rows of data are used.
    - During each iteration, the network will compute the gradients of the 
      weights with regard to the loss on the batch and upate the weights
      accordingly.

From the example in the book, 

* the model under consideration is two layers of 512 and 10 nodes.
* the training data is 6000 rows by 784 columns (flattened pixel array: 28x28=784)  for training data.
* the training label column is separate

Furthermore, the book says that after 5 epochs, 2,345 (469 per epoch) gradients will be performed.

How does he arrive at this number?

Each batch has this many rows:

> 6000/128=46.875

Each iteration 768 pixel values are loaded into first layer and passed to the 10 output layers.

> 46.875*10=469 (<--- 469 per epoch)

There are 5 epochs used to train the model. ie. 5 iterations of training.

> 5*469=2345 (<--- 2,345 total)



# regarding the -1

The -1 reduces the axis by one.  Since the vector is 1D, this reduces the result to a scalar, ie a tensor
of 0D.

## Hi-lites on orig repo

Some of this came from a hackathon repo I did previously.

| code                 | Notes                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| src/ML-try-007.ipynb | Was the final submission code                                                                     |
|                      | Sets up the notebook to use tensorboard.                                                          |
|                      | I doubt tensorboard works in watsonx - remove it                                                  |
|                      | Uses ./csv/usgs_gsvb_v2.csv for data                                                              |
|                      | The input has 9K rows and 8 columns                                                               |
|                      | Should break this up into a single file to generate the clean data including a yaml data contract |
|                      | adds new columns, normalizes the data                                                             |
|                      | -- cut off for cleaning data --                                                                   |
|                      |  The rest of the code has:                                                                        |
|                      |     * Defining model                                                                              |
|                      |     * training model                                                                              |
|                      |     * testing model                                                                               |
| csv/usgs_gsvb_v2     | Initial set of *raw* data                                                                         |
|                      | Originally this data came from two sources USGS and Greenstream sensor data                       |
|                      | This dataset has been massaged and combined previously to make the current file.                  |



## URLS

* [keras underfitting and overfitting](https://www.tensorflow.org/tutorials/keras/overfit_and_underfit)