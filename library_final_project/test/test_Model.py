import unittest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from pandas.testing import assert_frame_equal
from EinesDeJardiner.Model import return_trained_model_RandomForestClassifier, fill_df_predictions, calc_auc_score

class Test_Model(unittest.TestCase):
    def test_return_trained_model(self):
        data = {
            "age" : [18,22],
            "beautifullness":[9,4],
            "followers":[10000, 244]
        }

        df = pd.DataFrame(data = data)
        X = df[["age", "beautifullness"]]
        Y = df["followers"]

        model = return_trained_model_RandomForestClassifier(X, Y, SEED=0)
        model_expected = RandomForestClassifier()
        assert model.__class__ == model_expected.__class__
    
    def test_fill_df_predictions(self):
        data = {
            "age" : [18,22],
            "beautifullness":[9,4],
            "followers":[10000, 244]
        }

        df = pd.DataFrame(data = data)
        X = df[["age", "beautifullness"]]
        Y = df["followers"]

        model = RandomForestClassifier()
        model.fit(X,Y)

        df_test = df.copy()
        df_test = fill_df_predictions(X, model)

        df_expected = df.copy()
        df_expected = df_expected.drop("followers", axis = 1)
        df_expected["predictions"] = model.predict_proba(X)[:, 1]

        assert_frame_equal(df_test, df_expected)
   

    def test_calc_auc_score(self):
        y = [1,0,1,1,0,0,1,1,1,0,1]
        y_pred = [0,1,1,1,1,0,1,0,0,0,1]
        auc = calc_auc_score(y, y_pred)
        auc_expected = roc_auc_score(y,y_pred)
        self.assertEqual(auc, auc_expected)


if __name__ == '__main__':
    unittest.main()

