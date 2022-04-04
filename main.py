import argparse
import json
import os
import sys

from rules_mapper import MAPPER

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help = "Path to put the report")
parser.add_argument("-c", "--config", help = "Path of the configuration")
args = vars(parser.parse_args())

output = 'output.json'

if(args['config'] != None):
    status = True
    report = {}
    if(args['output'] != None):
        output = args['output']
    configuration_path = args['config']

    with open(configuration_path, 'r', encoding='utf-8') as t:
        CONFIGURATION = json.load(t)

    for rule_config in CONFIGURATION['rules']:
        rule_kind = rule_config['kind']
        rule_identifier = rule_config['identifier']
        if(rule_config['enable'] and rule_kind in MAPPER):
            rule_obj = MAPPER[rule_kind](
                CONFIGURATION['base-url'],
                rule_config['coverage'],
                rule_config['data']
            )
            response = rule_obj()
            report[rule_identifier] = response.toJson()
            status =  status and response.status
    final_response = {
        'status': 'failure-sv-report' if not status else 'success-sv-report',
        'rules': report
    }
    with open(output, 'w', encoding='utf-8') as t:
        t.write(json.dumps(final_response, indent=2))
    
    if(not status):
        print(status)
        os._exit(0)
else:
    print('You have to pass the configuration file path.')
