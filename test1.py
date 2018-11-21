# import pymongo
# from think_tank import start_urls_data
# conn = pymongo.MongoClient(host='39.108.191.166', port=27017)
# db = conn['test']
# collection = db['spider']
#
#
# collection.insert_many(start_urls_data.START_URLS_DATA)
# id = collection.find_one({'site': 'brookings'})
# print(id)
# print(start_urls_data.START_URLS_DATA)
# from think_tank import start_urls_data
#
# for k in start_urls_data.START_URLS_DATA:
#     print(k['id'])
# import re
# # str1 = ''
# list1 = ['1     1111 1  11   ', '   2', '   3   ']
# list2 = ['1']
# # for i in list2:
# #     j =  re.sub(r'\t|\r|\n|\s', '', i)
# #     str1 += j + ' '
# # print(str1.strip())
#
# str1 = ''.join(list1)
# str2 = re.sub(r'\r|\n|\s|\t','',str1)
# print(str1)
# print(str2)
import json

str1 = """
{"success":true,"data":{"data":"[{\"key\":\"1997\",\"values\":[{\"x\":\"IT\/telecom\/media\",\"y\":39.82804344},{\"x\":\"Manufacturing\",\"y\":42.35310182},{\"x\":\"Transport\/logistics\",\"y\":30.4231446},{\"x\":\"Retail trade\",\"y\":24.45696487},{\"x\":\"Finance\/insurance\",\"y\":25.9922625},{\"x\":\"Wholesale trade\",\"y\":24.5763704},{\"x\":\"All sectors\",\"y\":26.02160595},{\"x\":\"Administrative\",\"y\":21.77450252},{\"x\":\"Utilities\",\"y\":25.82618026},{\"x\":\"Real estate\",\"y\":18.51919619},{\"x\":\"Arts\/recreation\",\"y\":18.12682989},{\"x\":\"Education\",\"y\":20.91097964},{\"x\":\"Professional services\",\"y\":13.0336128},{\"x\":\"Accommodation\/catering\",\"y\":13.79128914},{\"x\":\"Health care\",\"y\":14.58666743},{\"x\":\"Other services\",\"y\":12.80540596}]},{\"key\":\"2012\",\"values\":[{\"x\":\"IT\/telecom\/media\",\"y\":47.36928054},{\"x\":\"Manufacturing\",\"y\":44.74349729},{\"x\":\"Transport\/logistics\",\"y\":41.08345307},{\"x\":\"Retail trade\",\"y\":39.63584728},{\"x\":\"Finance\/insurance\",\"y\":37.41336208},{\"x\":\"Wholesale trade\",\"y\":31.00932081},{\"x\":\"All sectors\",\"y\":32.38511588},{\"x\":\"Administrative\",\"y\":24.3618446},{\"x\":\"Utilities\",\"y\":24.24920688},{\"x\":\"Real estate\",\"y\":22.8719991},{\"x\":\"Arts\/recreation\",\"y\":18.37357083},{\"x\":\"Education\",\"y\":18.06397621},{\"x\":\"Professional services\",\"y\":16.80065888},{\"x\":\"Accommodation\/catering\",\"y\":15.99474232},{\"x\":\"Health care\",\"y\":13.05730201},{\"x\":\"Other services\",\"y\":12.73740994}]}]","options":"{\"dateFormat\":{\"enabled\":false,\"validated\":false,\"formatString\":\"\",\"failedAt\":\"IT\/telecom\/media\"},\"color\":[\"#1f77b4\",\"#aec7e8\",\"#ff7f0e\",\"#ffbb78\",\"#2ca02c\",\"#98df8a\",\"#d62728\",\"#ff9896\",\"#9467bd\",\"#c5b0d5\",\"#8c564b\",\"#c49c94\",\"#e377c2\",\"#f7b6d2\",\"#7f7f7f\",\"#c7c7c7\",\"#bcbd22\",\"#dbdb8d\",\"#17becf\",\"#9edae5\"],\"yDomain\":[0,50],\"type\":\"groupedBarChart\",\"showLegend\":true,\"showControls\":false,\"stacked\":false,\"reduceXTicks\":false,\"breakpoints\":{\"active\":0,\"values\":[{\"noMaxWidth\":true,\"maxWidth\":350,\"height\":400}]},\"xAxis\":{\"axisLabel\":\"Sector\",\"rotateLabels\":63},\"margin\":{\"bottom\":133,\"left\":60},\"yAxis\":{\"axisLabel\":\"Percent\",\"width\":60},\"tickFormatSettings\":{\"yAxis\":{\"locale\":22,\"showCurrencySymbol\":false,\"groupThousands\":false,\"prepend\":\"\",\"append\":\"\",\"decimalPlaces\":0,\"multiplier\":\".01\",\"usePercent\":true},\"locale\":22,\"showCurrencySymbol\":false,\"groupThousands\":true,\"prepend\":\"\",\"append\":\"\",\"decimalPlaces\":2,\"multiplier\":\"1\",\"usePercent\":false}}","metadata":"{\"title\":\"Top 4 firms' average share of total revenue\",\"caption\":\"\",\"credit\":\"Source: The Economist, \\u201cToo much of a good thing,\\u201d March 26, 2016.\",\"subtitle\":\"\"}","annotations":""}}"""
str2 = json.dumps(str1)
str3 = json.loads(str2)
print(str3)
