import argparse
import json
from rules_mapper import MAPPER

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help = "Path to put the report")
parser.add_argument("-c", "--config", help = "Path of the configuration")
args = vars(parser.parse_args())

output = 'output.json'

if(args['config'] != None):
    report = {}
    if(args['output'] != None):
        output = args['output']
    configuration_path = args['config']

    with open(configuration_path, 'r', encoding='utf-8') as t:
        CONFIGURATION = json.load(t)

    for rule in CONFIGURATION['rules']:
        rule_config = CONFIGURATION['rules'][rule]
        if(rule_config['enable'] and rule in MAPPER):
            rule_obj = MAPPER[rule](
                CONFIGURATION['base-url'],
                rule_config['coverage'],
                rule_config['data']
            )

            response = rule_obj()
            report[rule] = response.toJson()
    with open(output, 'w', encoding='utf-8') as t:
        t.write(json.dumps(report, indent=2))
else:
    print('You have to pass the configuration file path.')
