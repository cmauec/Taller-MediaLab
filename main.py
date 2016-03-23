# -*- coding: utf-8 -*-
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
import jinja2
import os
from google.appengine.ext import ndb


class Saludo(ndb.Model):
	nombre = ndb.StringProperty()
	saludo = ndb.StringProperty()
	fecha_publicacion = ndb.DateTimeProperty(auto_now = True)

je = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
	)

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	values = {
    		'mensaje': 'Deja tu saludo a MediaLab'
    	}
    	template = je.get_template('view/index.html')
        self.response.write(template.render(values))

    def post(self):
    	nombre = self.request.get('nombre')
    	saludo = self.request.get('saludo')
    	entidad_saludo = Saludo(
    			nombre = nombre,
    			saludo = saludo
    		)
    	entidad_saludo.put()
    	values = {
    		'mensaje': 'Gracias por el saludo'
    	}
    	template = je.get_template('view/index.html')
    	self.response.write(template.render(values))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
