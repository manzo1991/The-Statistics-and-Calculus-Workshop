import unittest
import import_ipynb
from t_conf_int import *

class Test(unittest.TestCase):
    
    def test1(self):
        #Assume
        data = [2,3,5,6,9]
        con_lvl = 0.95
        #Action
        result = t_confidence_interval(data,con_lvl)
        result2 = tuple(map(lambda x: isinstance(x, float) and round(x, 2) or x, result))
        #Assert
        self.assertSequenceEqual(result2,(1.60,8.40))
        
    def test2(self):
        #Assume
        sample = [159,155,157,125,103,122,101,82,228,199,195,110,191,151,119,119,112,87,190,87]
        hypoth_value = 130
        sig_level = .05
        test_type = 'upper'
        #Action
        result = t_test(sample, hypoth_value, sig_level, test_type)
        result2 = tuple(map(lambda x: isinstance(x, float) and round(x, 4) or x, result))
        #Assert
        self.assertSequenceEqual(result2,(0.9956,0.166))
        
    def test3(self):
        #Assume
        x = [1,2,3,4,5]
        x = np.array(x).reshape(-1,1)
        y = [1,2,1.3,3.75,2.25]
        #Action
        model = lm.LinearRegression()
        model.fit(x,y)
        coeff = float(model.coef_)
        intercept = float(model.intercept_)
        #Assert
        self.assertEqual(round(intercept,3), 0.785)
        self.assertEqual(round(coeff,3), 0.425)
        
        
if __name__ == '__main__':
    unittest.main()
        
