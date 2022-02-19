import html_generator_module as hg
import xml_generator_module as xg

# print(hg.create())
# print(xg.create())

import data_collection as dc
import journal as jour

# hg.new_create(dc.data_coll())
# xg.new_create(dc.data_coll())
jour.data_logger(dc.data_coll())
hg.new_create(xg.new_create(dc.data_coll()))
