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


class Person(db.Model):
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
    college = db.StringProperty(required=True);
    university = db.StringProperty(required=True);

    '''Returning db object to dict obj'''

    def to_dict(self):
        return db.to_dict(self, {'id': self.key().id()})


class Employee(db.Model):
    '''The data model'''
    name = db.StringProperty(required=True);

    person = db.ReferenceProperty(Person,
                                  collection_name='employees')

    '''Returning db object to dict obj'''

    def to_dict(self):
        return db.to_dict(self, {'id': self.key().id()})


class Skill(db.Model):
    '''The data model'''
    description = db.StringProperty(required=True);

    '''Returning db object to dict obj'''

    def to_dict(self):
        return db.to_dict(self, {'id': self.key().id()})


class PersonAPI(webapp2.RequestHandler):
    def get(self):
        '''Fetching 1 records from db model'''
        person = Person.all().fetch(limit=1)
        logging.info([p.to_dict() for p in person])
        '''Returning the db records as list of dictonaries for ez json conversion'''
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps([p.to_dict() for p in person]))

    def post(self):
        dictonary = json.loads(self.request.body)
        person = Person(name=dictonary['name'],
                        address=dictonary['address'],
                        telePhone=dictonary['telePhone'],
                        cellPhone=dictonary['cellPhone'],
                        email=dictonary['email'],
                        dateOfBirth=dictonary['dateOfBirth'],
                        placeOfBirth=dictonary['placeOfBirth'],
                        citizenship=dictonary['citizenship'],
                        maritalStatus=dictonary['maritalStatus'],
                        spoucesName=dictonary['spoucesName'],
                        children=dictonary['children'],
                        sex=dictonary['sex'],
                        college=dictonary['college'],
                        university=dictonary['university'])
        person.put()


class EmployeeAPI(webapp2.RequestHandler):
    def get(self):
        '''Fetching 1 records from db model'''
        employee = Employee.all().fetch(limit=1)
        logging.info([e.to_dict() for e in employee])
        '''Returning the db records as list of dictonaries for ez json conversion'''
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps([e.to_dict() for e in employee]))

    def post(self):
        dictonary = json.loads(self.request.body)
        employee = Employee(name=dictonary['name'])
        q = Person.all()
        q.filter('name =', dictonary['person'])
        person = q.get()
        employee.person = person
        employee.put()


app = webapp2.WSGIApplication([
                                  ('/api/person.*', PersonAPI),
                                  ('/api/employee.*', EmployeeAPI)
                              ], debug=True)