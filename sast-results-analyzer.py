# It analyze the results of sonar cloud sast analysis result file in a Gitlab Job. In case of any issues found in the measure, i.e, code_smells, bugs, vulnerabilitie, it will raise an error. 
# API Endpoint to get the results
# curl -s -u "${SONAR_TOKEN}:" "https://sonarcloud.io/api/measures/component?component=<project-id>&metricKeys=code_smells,bugs,vulnerabilities&branch=${CI_COMMIT_REF_NAME}" > sast-result.json

import json
f = open("sast-result.json")
data = json.load(f)
for measure in data["component"]["measures"]:
    if int(measure["value"]) > 0:
        raise Exception("SAST Tool detected issues, details can be found in the job artifact")
f.close()
