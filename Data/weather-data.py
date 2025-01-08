#%% 
"""
Notes to self about the visual crossing API. 
- Max query size is 1000 at free usage level where 1 query = 1 day for any number of params 
- Includes temp and windspeed
- Key stored locally 

TO DO: 
-[] Finish unpacking data
-[] Record metadata somewhere
"""

import pandas as pd 
import requests
from datetime import datetime


#%%

# %%
cutoff = pd.Timestamp("2025-01-01")
query_one = cutoff - pd.Timedelta(days=999)
query_two = query_one - pd.Timedelta(days=999)
query_three = query_two - pd.Timedelta(days=999)


# %%

url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/england/2015-09-01/2025-01-22?unitGroup=uk&elements=name%2Clatitude%2Clongitude%2Ctemp%2Cwindspeedmean&include=days%2Cfcst%2Cobs%2Cremote&key=S7KPK4HL9JBWDAMCPPVAC2GQC&contentType=json"
# %%
r = requests.get(url)

# %%
q1 = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/england/{query_one.strftime('%Y-%m-%d')}/{cutoff.strftime('%Y-%m-%d')}?unitGroup=uk&elements=name%2Clatitude%2Clongitude%2Ctemp%2Cwindspeedmean&include=days%2Cfcst%2Cobs%2Cremote&key=S7KPK4HL9JBWDAMCPPVAC2GQC&contentType=json"
q2 = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/england/{query_two.strftime('%Y-%m-%d')}/{query_one.strftime('%Y-%m-%d')}?unitGroup=uk&elements=name%2Clatitude%2Clongitude%2Ctemp%2Cwindspeedmean&include=days%2Cfcst%2Cobs%2Cremote&key=S7KPK4HL9JBWDAMCPPVAC2GQC&contentType=json"
q3 = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/england/{query_three.strftime('%Y-%m-%d')}/{query_two.strftime('%Y-%m-%d')}?unitGroup=uk&elements=name%2Clatitude%2Clongitude%2Ctemp%2Cwindspeedmean&include=days%2Cfcst%2Cobs%2Cremote&key=S7KPK4HL9JBWDAMCPPVAC2GQC&contentType=json"
# %%
r1 = requests.get(q1)
q2 = requests.get(q2)
q3 = requests.get(q3)
# %%
