# It analyzes the results of the detect-secrets (python package) result file in a Gitlab Job. In case of any issues in the result, it will raise an exception. 

import json
f = open("secret-detection-job.json")
data = json.load(f)
# In case of any secret detection, the result key in the json is going to have values in it.
if len(list(data["results"])) > 0:
    raise Exception("Secrets found, details can be found in the job artifact")
f.close()
