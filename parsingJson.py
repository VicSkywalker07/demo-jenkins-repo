import json

# json in the form of string
json_string='{"key1":"val1","key2":"val2"}'

# convert json in form of string to python readable object
json_result=json.loads(json_string)

print(json_result)