#!/usr/bin/python

import json
import sys
from optparse import OptionParser

def has_property(feature, property_name, property_value):
    '''
    Check if a feature has a particular property.

    @param feature: A GeoJSON feature
    @param property_name: The name of the property
    @param property_value: The value that this property should have
    @return: True or False
    '''
    if property_name in feature['properties']:
        if feature['properties'][property_name].find(property_value) >= 0:
            return True
        else:
            return False

def filter_geojson(json_object, property_name, property_value):
    '''
    Iterate over the features in a GeoJSON object and return only
    the ones that have the feature property_name and it has a value
    'property_value'

    @param json_object: A GeoJSON object
    @param property_name: The property to filter on
    @param property_value: The value the property should have
    @return: A filtered json object
    '''

    new_features = [f for f in json_object['features'] if has_property(f, property_name, property_value)]
    json_object['features'] = new_features

    return json_object

def main():
    usage = """
    python filter_geojson.py file.json property_name property_value

    Filter a GeoJSON file and return a JSON which contains only contains the Features
    who have a property_name equal to property_value
    """
    num_args= 1
    parser = OptionParser(usage=usage)

    #parser.add_option('-o', '--options', dest='some_option', default='yo', help="Place holder for a real option", type='str')
    #parser.add_option('-u', '--useless', dest='uselesss', default=False, action='store_true', help='Another useless option')

    (options, args) = parser.parse_args()

    if len(args) < num_args:
        parser.print_help()
        sys.exit(1)

    with open(args[0], 'r') as f:
        json_object = json.load(f)
        filtered_json_object = filter_geojson(json_object, args[1], args[2])

        print json.dumps(filtered_json_object)

if __name__ == '__main__':
    main()

