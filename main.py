import sys
import json
from rules_mapper import MAPPER
argv = sys.argv
output = 'output.json'
argv_len = len(argv)
if(argv_len >= 2):
    report = {}
    if(argv_len == 3):
        output = argv[2]
    configuration_path = argv[1]

    with open(configuration_path, 'r', encoding='utf-8') as t:
        CONFIGURATION = json.load(t)

    for rule in CONFIGURATION['rules']:
        rule_config = CONFIGURATION['rules'][rule]
        if(rule_config['enable'] and rule in MAPPER):
            rule_obj = MAPPER[rule](
                CONFIGURATION['base-url'], rule_config['coverage'], rule_config['data'])

            response = rule_obj()
            report[rule]=response.toJson()
    with open(output, 'w', encoding='utf-8') as t:
        t.write(json.dumps(report, indent=2))
else:
    print('You have to pass the configuration file path.')
