#!/usr/bin/python3
"""
Script documentation goes here.
"""
import sys
import importlib.util

spec = importlib.util.spec_from_file_location("save_to_json_file", "5-save_to_json_file.py")
save_to_json_file = importlib.util.module_from_spec(spec)
spec.loader.exec_module(save_to_json_file)

spec = importlib.util.spec_from_file_location("load_from_json_file", "6-load_from_json_file.py")
load_from_json_file = importlib.util.module_from_spec(spec)
spec.loader.exec_module(load_from_json_file)

filename = "add_item.json"

try:
    items_list = load_from_json_file.load_from_json_file(filename)
except FileNotFoundError:
    items_list = []

items_list.extend(sys.argv[1:])
save_to_json_file.save_to_json_file(items_list, filename)
