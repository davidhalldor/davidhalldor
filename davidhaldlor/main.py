#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import logging
import json
import os
from google.appengine.ext import db
from google.appengine.ext.webapp import template 

class Data(db.Model):
    '''The data model'''
    tag = db.StringProperty(required=True);
    authorName = db.StringProperty(required=True);
    
    '''Returning db object to dict obj'''
    def to_dict(self):
        return db.to_dict(self, {'id':self.key().id()})

class API(webapp2.RequestHandler):
    def get(self):
        '''Fetching 10 records from db model'''
        data = Data.all().fetch(limit=10)
        #logging.info([d.to_dict() for d in data])
        '''Returning the db records as list of dictonaries for ez json conversion'''
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps([d.to_dict() for d in data]))

    def post(self):
        dictonary = json.loads(self.request.body)
        data = Data(tag = dictonary['tag'], authorName = dictonary['authorName'])
        data.put()

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, None))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/api.*', API)
], debug=True)