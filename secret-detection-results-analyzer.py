# It analyzes the results of the detect-secrets (python package) result file in a Gitlab Job. In case of any issues found in the measure, it will raise an error. 

import json
f = open("secret-detection-job.json")
data = json.load(f)
if len(list(data["results"])) > 0:
    raise Exception("\n\n\n *******************************\n Secrets found, details can be found in the job artifact \n ******************************* \n\n\n")
f.close()
