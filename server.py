import cherrypy
import json
from marrow.mailer import Mailer, Message
import sys
import smtplib

# This file should define a username and password field
from credentials import *

# Credentials (if needed)
# The actual mail send
def send_email(msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(username, username, msg)
    server.quit()


class Root(object):
    @cherrypy.expose
    def index(self):
        with open("index.html") as fp:
            return fp.readlines()

    @cherrypy.expose
    def email(self, address):
        print (address)
        msg = "Subject: Ava Referral \n\n Email %s about an ava referral" %  address
        send_email(msg) 
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return json.dumps({'name': address.split('@')[0]})

if __name__ == '__main__':

    cherrypy.config.update({
        'server.socket_host':'173.255.255.143',
        'server.socket_port':8087,
    })

    cherrypy.quickstart(Root(), '/ava', 'prod.conf')
