#Dependencies
from flask import Flask
from flask import render_template
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps

import json

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'diabetes'
COLLECTION_NAME = 'diabetes_nutr'
FIELDS = {'ID_x': True, 
            'ALCOHOL': True, 
            'B12_ADDED': True, 
            'CAFFEINE':True,
            'CARBOHYDRATES': True, 
            'CHOLESTEROL': True, 
            'FIBER': True,
            'IRON':True,
            'CALORIES':True, 
            'FOODCOMPONENT': True,
            'MAGNESIUM': True, 
            'MONOSATURATED_FAT':True,
            'POTASSIUM':True,
            'PROTEIN':True,
            'SATURATED_FAT':True,
            'SODIUM':True,
            'SUGAR':True,
            'TRANS_FAT':True,
            'B12':True,
            'VITAMIN_D':True,
            'DRABF':True,
            'DRDINT':True,
            'SEQN':True,
            'WTDR2D':True,
            'WTDRD1':True,
            'ID_y':True,
            'AgeToldDiabetes':True,
            'LenTakingInsulin':True,
            'SeenDocPastYr':True,
            '#ChkGlucose':True,
            'DocDBPread':True,
            'DocSBPread':True,
            'RcntLDL#':True,
            'DocLDLread':True,
            'DocChkFeet#':True,
            'PrsnlChkFeet':True,
            'DocToldDiabetes':True,
            'TakeInsulin':True,
            'UOMmmyy':True,
            'TakePillsLwrBS':True,
            'DiaAffectEyes':True,
            'EvrToldPreDia':True,
            'EvrToldPreDia(Bi)':True,
            'EvrToldHeaRskDia':True,
            'FeelRiskForDia':True,
            'FamHistory':True,
            'Overweight':True,
            'Age':True,
            'PoorDiet':True,
            'Race':True,
            'HadBabyOvr9lb':True,
            'LackOfPhyAct':True,
            'HighBP':True,
            'HighBS':True,
            'HighChol':True,
            'Hypoglycemic':True,
            'ExtrmHunger':True,
            'TingInHdsFeet':True,
            'BlurredVision':True,
            'IncFatigue':True,
            'AnyAtRisk':True,
            'DocWarning':True,
            'Other':True,
            'GestationDia':True,
            'FreqUrination':True,
            'Thirst':True,
            'CraveEatSugr':True,
            'Medication':True,
            'PolycysticOvSyn':True,
            'BloodTst3Yrs':True,
            'LenSeenDiaSpec':True,
            'OneDocDia':True,
            'UOMd_w_m_y':True,
            'PastYrChkA1C':True,
            'LastA1Clvl':True,
            'DocSayA1C':True,
            'RcntDBP':True,
            'RcntSBP':True,
            'UOMd_w_m_yDocRcntDBPsbp':True,
            'LastPupilsDilated':True,
            '_id':False
         }

@app.route("/")
def index():
    return render_template("dash.html")

@app.route("/Final_Project")
def project_diabetes():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    pre_diabetes = collection.find(projection=FIELDS, limit=1000)
    json_diabetes = []
    for i in pre_diabetes:
        json_diabetes.append(i)
    json_diabetes = json.dumps(json_diabetes, default=json_util.default)
    connection.close()
    return json_diabetes

if __name__ == '__main__':
    app.run(debug=True)