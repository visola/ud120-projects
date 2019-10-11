#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
names_file = open("../final_project/poi_names.txt").readlines()

names = []
for line in names_file:
    if line.startswith("("):
        line = line.replace(',', '')
        split = line.split()
        names.append( [split[1].upper(), split[2].upper()])

print "Names in file: ", len(names)
print "Number of records in the file:", len(enron_data)

print "--"

poi_count = 0
total_nan_total_payments = 0
total_nan_total_payments_poi = 0
for k, v in enron_data.items():
    if k == 'PRENTICE JAMES':
        print "Total stocks owned by James Prentice: ", v['total_stock_value']

    if k == 'COLWELL WESLEY':
        print "Total email from Wesley Colwell to POI: ", v['from_this_person_to_poi']

    if k == 'SKILLING JEFFREY K':
        print "Total stock options exercised from Jeffrey Skilling: ", v['exercised_stock_options']

    if v['total_payments'] == 'NaN':
        total_nan_total_payments = total_nan_total_payments + 1

    if v['poi']:
        key_split = k.split()
        name = [ key_split[0] ]
        poi_count = poi_count + 1
        if v['total_payments'] == 'NaN':
            total_nan_total_payments_poi = total_nan_total_payments_poi + 1

print "--"
print "Total number of persons of interest: ", poi_count
print "Total number of people without Total Payments: ", total_nan_total_payments, " (", float(total_nan_total_payments) / float(poi_count), ")"
print "Total number of people without Total Payments: ", total_nan_total_payments_poi, " (", float(total_nan_total_payments_poi) / float(poi_count), ")"
