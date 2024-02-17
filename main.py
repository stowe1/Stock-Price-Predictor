# import csv
# import numpy as np
# from sklearn.svm import SVR
# import matplotlib.pyplot as plt
# from polygon import RESTClient

# # # plt.switch_backend('new_backend')
# # dates = []
# # prices = [] 

# # def get_data(filename):
# #     with open(filename, 'r') as csvfile:
# #         csvFileReader = csv.reader(csvfile)
# #         next(csvFileReader)
# #         for row in csvFileReader:
# #             dates.append(int(row[0].split('/')[0]))
# #             prices.append(float(row[1]))
# #     return

# # def predict_prices(dates, prices, x):
# #     dates = np.reshape(dates, (len(dates), 1))
    
# #     # linear support vector regression model
# #     svr_len = SVR(kernel='linear', C=1e3)
# #     svr_poly = SVR(kernel='poly', C=1e3, degree=2)
# #     svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
# #     svr_rbf.fit(dates, prices)
# #     svr_len.fit(dates, prices)
# #     svr_poly.fit(dates, prices)
    
# #     plt.scatter(dates, prices, color='black', label='Data')
# #     plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
# #     plt.plot(dates, svr_len.predict(dates), color='green', label='Linear model')
# #     plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
# #     plt.xlabel('Date')
# #     plt.ylabel('Price')
# #     plt.title('Support Vector Regression')
# #     plt.legend()
# #     plt.show()
    
# #     return svr_rbf.predict(x)[0], svr_len.predict(x)[0], svr_poly.predict(x)[0]

# # get_data('TSLA.csv')
# # predicted_price = predict_prices(dates, prices, 29)

# # print(predicted_price)



# client = RESTClient("hwFj6xOsypub5kCqRKykMRk6tiCzIl8o")

# aggs = []
# for a in client.list_aggs(
#     "AAPL",
#     1,
#     "minute",
#     "2022-01-01",
#     "2023-02-03",
#     limit=5,
# ):
#     aggs.append(a)

# print(aggs)

# print("we made it to the end of the file!")





