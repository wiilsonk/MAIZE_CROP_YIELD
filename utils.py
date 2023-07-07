from CropYieldModel import CropYieldModel
import pandas as pd
import numpy as np
from keras.models import load_model

model = load_model("./model/dlmodel.h5")

# Return a data model that is standardised
def standardise(data: CropYieldModel) -> CropYieldModel :

    data.rainfall = data.rainfall / 3137.584672529126
    data.pesticides = data.pesticides / -196.3119315471652
    data.temp = data.temp / -24.76292187351093
    data.rainfall = float(data.rainfall)
    data.pesticides = float(data.pesticides)
    data.temp = float(data.temp)

    return data

def predict_yield(unstd : CropYieldModel) -> float:
  
  data = standardise(unstd)
  
  X = [data.area ,data.crop, data.rainfall, data.pesticides, data.temp]
  
  # Transforming B into a numpy array   
  X = np.array(X).reshape(1, -1)

  Xdf = pd.DataFrame(X, columns=["Area","Item", "average_rain_fall_mm_per_year","pesticides_tonnes","avg_temp"])
  
#   Type Conversion
  Xdf["average_rain_fall_mm_per_year"] = Xdf["average_rain_fall_mm_per_year"].astype(float)
  Xdf["pesticides_tonnes"] = Xdf["pesticides_tonnes"].astype(float)
  Xdf["Area"] = Xdf["Area"].astype(float)
  Xdf["Item"] = Xdf["Item"].astype(float)
  Xdf["avg_temp"] = Xdf["avg_temp"].astype(float)
  
  T = np.asarray(Xdf)
  ypredd = model.predict(T)[0][0]
  ypredd
  return ypredd