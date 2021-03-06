## 
##################     IMPORTING PACKAGES       ###############################

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from math import sqrt
from numpy import concatenate
from subprocess import check_output
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from sklearn.model_selection import  train_test_split
import time #helper libraries
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from numpy import newaxis
from sklearn.metrics import mean_squared_error
import math
from numpy.random import seed
seed(1)
import csv
import pandas as pd
import io
import requests
import time
import datetime 
from pandas.tseries.offsets import CustomBusinessDay
from datetime import datetime
from datetime import date
from dateutil.parser import parse
from datetime import datetime		
from nsepy import get_history
from datetime import date
import glob
import shutil

def getEvaluationDays(startdate, enddate):
	holidays = ['20150126', '20150217', '20150306', '20150402', '20150403', '20150501', \
					'20150815', '20150917', '20151002', '20151022', '20151111', '20151112', \
					'20151125', '20151225', '20160126', '20160307', '20160324', '20160325', \
					'20160414', '20160415', '20160419', '20160706', '20160815', '20160905', \
					'20160913', '20161011', '20161012', '20161031', '20161114', '20170126', \
					'20170224', '20170313', '20170404', '20170414', '20170501', '20170626', \
					'20170815', '20170825', '20171002', '20171019', '20171020', '20171225']
	evaluationDays = list()
	startday = datetime.strptime(str(startdate), '%Y%m%d')
	endday = datetime.strptime(str(enddate), '%Y%m%d')
	allholidays = [datetime.strptime(holidaydate, '%Y%m%d') for holidaydate in holidays]
	businessday = CustomBusinessDay(holidays=allholidays)
	temp = startday
	while temp <= endday:
		if temp == (temp + 1 * businessday) - 1 * businessday:
			dayStr = temp.strftime('%Y%m%d')
			evaluationDays.append(dayStr)
			temp = temp + 1 * businessday
		else:
			temp = temp + 1 * businessday
			dayStr = temp.strftime('%Y%m%d')
			evaluationDays.append(dayStr)
			temp = temp + 1 * businessday
	return evaluationDays
  
  z=getEvaluationDays('20170101','20170201')
f_name = 'aaa.csv' 
csvfile = open(f_name,'wb')
fieldnames = ['Date_1','Open','High','Low','Actual_Close','Predicted_Close_1','Date_2','Predicted_Close_2']
writer = csv.DictWriter(csvfile, fieldnames = fieldnames, dialect=csv.excel)
writer.writeheader()


Lookback_period=2
Number_of_parametres=5
for i in z:
	i = datetime.strptime(i, "%Y%m%d").date()
	
		
	prices_dataset = get_history(symbol="NIFTY",
							start=date(2001,1,1),
							end=i,
							index=True)
		
	prices_dataset= prices_dataset.reset_index()
	A=4
	########################################## data ######################################
	stock_prices = prices_dataset[['Date','Open','High','Low','Close']] 
	stock_prices = np.array(stock_prices)
	
	# convert an array of values into a dataset matrix
	###################################### reshape into X=t and Y=t+1 #############################
	def create_dataset(dataset, look_back=Lookback_period):
		dataX, dataY = [], []
		for i in range(len(dataset)-look_back):
			a = dataset[i:(i+look_back-1), 0:Number_of_parametres]
			dataX.append(a)	
			dataY.append(dataset[i + look_back, 0:Number_of_parametres])
		return np.array(dataX), np.array(dataY)
	
	X,Y= create_dataset(stock_prices, look_back=Lookback_period)
	X = X.reshape(X.shape[0],Number_of_parametres)
	Y = Y.reshape(Y.shape[0],Number_of_parametres)
	
	############################################ min max #########################################
	scaler = MinMaxScaler()
	X[:,4:]= scaler.fit_transform(X[:,4:])
	Y[:,4:]=scaler.fit_transform(Y[:,4:])
	
	########################################### test train ################################
	########################################## Choose a train size, and split the data into a train and test set.		
	train_size = len(X)-2
	X_train = X[:train_size,:]
	Y_train = Y[:train_size]
	Y_test = Y[train_size:,:]
	X_test = X[train_size:,:]
	X_train = X_train[:,A:]
	Y_train = Y_train[:,A:]
	X_test = X_test[:,A:]
	
	X_train=X_train.reshape(X_train.shape[0],1,X_train.shape[1])  
	X_test=X_test.reshape(X_test.shape[0],1,X_test.shape[1])
	Y_train=Y_train.reshape(Y_train.shape[0],1)
	
	
	##################################################### model ################################## 

	model = Sequential()
	model.add(LSTM(10,return_sequences=True,input_shape=(1, 1)))
	model.add(LSTM(10, return_sequences=True))
	model.add(LSTM(10, return_sequences=False))
	model.add(Dense(1))
	model.compile(loss='mse', optimizer='adam')
	model.fit(X_train, Y_train, epochs=100, batch_size=128)
	testPredict = model.predict(X_test)
	# print "testPredict",testPredict
	
	
	############################################## rescale ########################################

	testPredict = scaler.inverse_transform(testPredict)
	Y_test[:,A:] = scaler.inverse_transform(Y_test[:,A:])
	print('Expected:', Y_test, 'Predicted', testPredict )
	
	
	############################################ export to excel ###########################################
	# testY=testY.reshape(testPredict.shape[0],1)
	Y_test=pd.DataFrame(Y_test)
	testPredict=pd.DataFrame(testPredict)
	testPredict['Predict_1']=testPredict[0][0]
	print "testPredict['Predict_1']",testPredict[0][0]
	testPredict['Predict_2']=testPredict[0][1]
	print "testPredict['Predict_2']",testPredict[0][0]
	Y_test['Date_1']=Y_test[0][0]
	Y_test['Date_2']=Y_test[0][1]
	print "Y_test['Date_1']",Y_test[0][0]
	print "Y_test['Date_1']",Y_test[0][1]
	del testPredict[0]
	del Y_test[0]
	testPredict=testPredict.drop([1])
	Y_test=Y_test.drop([1])
	T_data = pd.concat([Y_test,testPredict], axis=1)
	T_data.columns = ['Open','High','Low','Actual_Close','Date_1','Date_2','Predicted_Close_1','Predicted_Close_2']
	T_data=T_data[['Date_1','Open','High','Low','Actual_Close','Predicted_Close_1','Date_2','Predicted_Close_2']]
	T_data.to_csv("11111"+"   "+ " to " + str(i) + ".csv", index=False, header=True)	
	

	writer.writerow({'Date_1':T_data['Date_1'],'Open':T_data['Open'],'High':T_data['High'],'Low':T_data['Low'],'Actual_Close':T_data['Actual_Close'],'Predicted_Close_1':T_data['Predicted_Close_1'],'Date_2':T_data['Date_2'],'Predicted_Close_2':T_data['Predicted_Close_2']})

csvfile.close()
exit()		
		
#import csv files from folder
path = r'C:/Users/user/Desktop/One_day_prediction/UNIVARIATE'
allFiles = glob.glob(path + "/*.csv")
with open('Combined.csv', 'wb') as outfile:
    for i, fname in enumerate(glob.glob(path + "/*.csv")):
        with open(fname, 'rb') as infile:
            if i != 0:
                infile.readline()
            shutil.copyfileobj(infile, outfile)
            print(fname + " has been imported.")
	
	
	############## New Variables #############
	# T_data['lag'] = T_data["Actual_Close"].shift(1)
	# T_data['plag'] = T_data["Predicted_Close"].shift(1)
	# T_data=T_data.dropna()	
	
	# T_data["actual_signal"] = np.where(T_data["Actual_Close"]>T_data['lag'],"Buy","sell")
	# T_data["predict_signal"] = np.where(T_data["Predicted_Close"]>T_data['lag'],"Buy","sell")
	# T_data["Open_Close_actual"] = np.where(T_data["Actual_Close"]>T_data["Open"],1,0)
	# T_data["Open_Close_predict"] = np.where(T_data["Predicted_Close"]>T_data["Open"],1,0)
