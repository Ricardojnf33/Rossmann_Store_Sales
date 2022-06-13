import pickle
import pandas as pd
from flask import Flask, request, Response
from rossmann.Rossmann import Rossmann

# loading model

model = pickle.load( open( '/content/Rossmann_Store_Sales/Model trained/model_rossmann.pkl', 'rb') )

# inicialize API
app = Flask( __name__) 
            
@app.route( '/rossmann/predict', methods=['POST'] )
def rossmann_predict():
    test_jason = request.get_json()

    if test_json: # there is data
        if isinstance( test_json, dict ): # unique example
            test_raw = pd.DataFrame( test_json, index=[0] )

        else: # multiple example
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )

        # Instantiate Rossmann class
        pipeline = Rossmann()

        # data cleaning
        df1 = pipeline.data_cleaning( test_raw )

        # feature enginerering
        df2 = pipeline.feature_engineering( df1 )

        # data preparation
        df3 = pipeline.data_prediction( df2 )

        # prediction
        df_response = pipeline.get_prediction( model, test_raw, df3 )

    else:
        return Response( '{}', status=200, mimetype='application/json' )

if __name__ == '__main__':
    app.run( '0.0.0.0' )