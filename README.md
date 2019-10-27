# Close-Price-Forecasting

This project presents a computational approach for predicting the stock price. A neural network based model has been used in predicting the direction of the movement of the closing value of the Nifty 50index. The model presented in the project also confirms that it can be used to predict price index value of the stock market. 

After studying the various features of the network model, an optimal model is proposed for the purpose of forecasting. The model has used the preprocessed data set of closing value of Nifty 50 Index. The data set encompassed the trading days from 1st January, 2001 to 31st December, 2017. 

In the project, the model has been validated across 5 years of the trading days. Accuracy of the performance of the neural network is compared using various out of sample performance measures. The average performance of the network in terms of accuracy in predicting the direction of the closing value of the index is reported at 74%. 

## Software and Libraries

Python programming was executed using the Anaconda software, as Python as a programming language itself must be installed first and then there are many packages to install. Anaconda has all the packages already installed it has the most useful packages for Mathematics, Science and Engineering already inbuilt installed. Through our project, we explored various libraries of python software for various tasks like data extraction, manipulation, mathematical calculations, visualization, valuation metrics, etc.
 
NsePy
=====
This library is a very useful and powerful tool in extracting historical data of NSE. This is a great tool to large amounts of historical data and also various types like Futures data, Options data and also the strike prices along with expiry can be extracted using NsePy library
.
For the data to be stored in a proper structured format and mathematical calculations and manipulations, Pandas and NumPy library were the most useful tool and made the further analysis easy.
 
Scikit Learn
=============
This is one of the most useful data analysis library which is extensively used for machine learning techniques where various machine learning techniques like regression, classification, clustering, multivariate techniques and many more can be implemented. This library has all the algorithms essential for model building, evaluation metrics and also validation techniques like k-fold cross validation can be done using this.
 
Keras 
======
It is an open source neural network library written in Python. It is capable of running on top of MXNet, Deeplearning4j, TensorFlow, Microsoft Cognitive Toolkit or Theano.


>  Methodology

In this project, initially Feed Forward Backpropagation Neural Network was used for the prediction. Feed forward Neural Networks is unidirectional connection between the neurons that means the information can flow only in forward direction. Input has been fed into first layer and with the help of hidden layers connected to the last layer that produces the output. There is no connection among neurons in the same layer. Since information is constantly feeding forward from one layer to the next. Hence it is called feed forward neural network.

The backpropagation algorithm falls into the general category of gradient descent algorithms. Purpose of gradient descent algorithm is to find the minima/maxima of a function by iteratively moving in the direction of negative slope of the function that we want to minimize/maximize. In our problem objective is to minimize the error function.

In Back-propagation algorithm the network is trained by repeatedly processing the training data set and comparing the network output with the actual output to reduce the mean square error. Weights of the connections between various neurons has been modified and this process has been continued till the error comes within threshold value. It is Backpropagation algorithm as errors from output is back-propagating towards the input layer during training sessions with the objective of minimizing the mean square error. As back-propagated model can be continuously updated to minimize error.

In addition to Feed Forward and Feed Forward Backpropagation Neural Network, Recurrent Neural Networks are also used for this project. A recurrent neural network (RNN) is a class of artificial neural network where connections between units form a directed cycle. This allows it to exhibit dynamic temporal behavior. Unlike feedforward neural networks, RNNs can use their internal memory to process arbitrary sequences of inputs. This makes them applicable to tasks such as unsegmented, connected handwriting recognition or speech recognition. Recurrent neural networks were developed in the 1980s. Hopfield networks were invented by John Hopfield in 1982. In 1993, a neural history compressor system solved a "Very Deep Learning" task that required more than 1000 subsequent layers in an RNN unfolded in time.
