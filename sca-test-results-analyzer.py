# It analyzes the results of opensca-cli result file in a Gitlab Job. In case of any issues found, it will raise an error. 

import json
f = open("sca.json")
data = json.load(f)
if ("indirect_vulnerabilities" in list(data)) and ((data["indirect_vulnerabilities"] > 0)):
    raise Exception("SCA Tool detected issues,  details can be found in the job artifact")
f.close()
