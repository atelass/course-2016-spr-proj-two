'''
Generate the overall provenance information for scripts in this directory to
create plan.json.

This does output times as well, hand edit to remove those while maintaining
valid JSON. We could get more clever and filter those here, but keep it simple
for now. You can validate JSON at http://jsonlint.com/.
'''

import prov.model
import datetime
import json
# grab our specific scripts
import get_boarding_info
import get_green_line_branch_info
import make_stop_gps_db
import make_walk_dist_db
import make_nearest_stops
import make_people_seconds

# Don't need time and won't keep it, but the individual methods expect it.
time = datetime.datetime.now()
json_arr_str = '['

for mod in [get_boarding_info, get_green_line_branch_info, make_stop_gps_db, make_walk_dist_db, make_nearest_stops, make_people_seconds]:
    doc = mod.create_prov(time, time)
    json_arr_str += doc.serialize() + ','

# The last character will be a trailing comma, just overwrite with end
# of array.
json_arr_str = json_arr_str[:-1] + ']'

pretty_str = json.dumps(json.loads(json_arr_str), indent=2, sort_keys=True)

print(pretty_str)

with open('plan.json', 'w') as f:
    f.write(pretty_str)
