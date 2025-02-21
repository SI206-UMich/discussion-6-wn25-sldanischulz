import unittest
import os
import csv


def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    # use this 'full_path' variable as the file that you open

    with open(full_path, newline='') as cf:
        reader = csv.DictReader(cf)
        output = {}
        tempdict2020 = {}
        tempdict2021 = {}
        tempdict2022 = {}

        for row in reader:
            for key,val in row.items():
                if key == "2020":
                    tempdict2020[row['Month']] = val
                    #print(tempdict2020)
                    
                if key == "2021":
                    tempdict2021[row['Month']] = val
                if key == "2022":
                    tempdict2022[row['Month']] = val

            output['2020'] = tempdict2020
            output['2021'] = tempdict2021
            output['2022'] = tempdict2022

        #print('OUTPUT', output)

        return output 
    #pass


def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: year (str), month (str), and max (int) 
        max is the maximum value for a month in that year, month is the corresponding month

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
        You'll have to change vals to int to compare them. 
    '''
    output = []
    for key,val in d.items():
        high = 0
        m = ''
        #print(key)
        for month,num in val.items():
            n = int(num)
            if n > high:
                high = n
                m = month
                #print("NEW HIGH:", m, high)
        result = (key, m, high)
        output.append(result)

    #print(output)
    
    return output

    #pass

def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and vals are floats rounded to nearest whole num or int
        vals are the average vals for months in the year

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        You'll have to make the vals int or float here and round the avg to pass tests.
    '''
    output = {}

    for key,val in d.items():
        total = 0
        count = 0
        average = 0
        #print(key)
        for month,num in val.items():
            n = int(num)
            total = total + n
            count = count + 1
            #print(month, total, count)

        average = total/count
        output[key] = average
    
    #print(output)

    return output


    #pass

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

        
def main():

    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
