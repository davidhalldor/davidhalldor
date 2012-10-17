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
from google.appengine.ext import db

class PersonalData(db.Model):
    '''The data model'''
    name = db.StringProperty(required=True);
    address = db.StringProperty(required=True);
    telePhone = db.StringProperty(required=True);
    cellPhone = db.StringProperty(required=True);
    email = db.StringProperty(required=True);
    dateOfBirth = db.StringProperty(required=True);
    placeOfBirth = db.StringProperty(required=True);
    citizenship = db.StringProperty(required=True);
    maritalStatus = db.StringProperty(required=True);
    spoucesName = db.StringProperty(required=True);
    children = db.StringProperty(required=True);
    sex = db.StringProperty(required=True);
    highSchool = db.StringProperty(required=True);
    university = db.StringProperty(required=True);
    
    '''Returning db object to dict obj'''
    def to_dict(self):
        return db.to_dict(self, {'id':self.key().id()})

class WorkData(db.Model):
    '''The data model'''
    employee = db.StringProperty(required=True);
    status = db.StringProperty(required=True);
    
    '''Returning db object to dict obj'''
    def to_dict(self):
        return db.to_dict(self, {'id':self.key().id()})

class SkillsData(db.Model):
    '''The data model'''
    employee = db.StringProperty(required=True);
    status = db.StringProperty(required=True);
    
    '''Returning db object to dict obj'''
    def to_dict(self):
        return db.to_dict(self, {'id':self.key().id()})

class API(webapp2.RequestHandler):
    def get(self):
        '''Fetching 10 records from db model'''
        data = PersonalData.all().fetch(limit=1)
        #logging.info([d.to_dict() for d in data])
        '''Returning the db records as list of dictonaries for ez json conversion'''
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps([d.to_dict() for d in data]))

    def post(self):
        dictonary = json.loads(self.request.body)
        data = PersonalData(name = dictonary['name'],
                            address = dictonary['address'],
                            telePhone = dictonary['telePhone'],
                            cellPhone = dictonary['cellPhone'],
                            email = dictonary['email'],
                            dateOfBirth = dictonary['dateOfBirth'],
                            placeOfBirth = dictonary['placeOfBirth'],
                            citizenship = dictonary['citizenship'],
                            maritalStatus = dictonary['maritalStatus'],
                            spoucesName = dictonary['spoucesName'],
                            children = dictonary['children'],
                            sex = dictonary['sex'],
                            highSchool = dictonary['highSchool'],
                            university = dictonary['university'])
        data.put()

app = webapp2.WSGIApplication([
    ('/api/personal.*', API)
], debug=True)