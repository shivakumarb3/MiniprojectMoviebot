import http.server
import json
import asyncio

from botbuilder.schema import (Activity, ActivityTypes, ChannelAccount)
from botframework.connector import ConnectorClient
from botframework.connector.auth import (MicrosoftAppCredentials,
                                         JwtTokenValidation, SimpleCredentialProvider)
from services.Person import *
#from services.Review import *
from services.Scrap import *
from services.Scrap2 import *
from services.Scrap3 import *
from services.Scrap4 import *
from services.Scrap5 import *


APP_ID = ''
APP_PASSWORD = ''
 

class BotRequestHandler(http.server.BaseHTTPRequestHandler):

    @staticmethod
    def __create_reply_activity(request_activity, text):
        return Activity(
            type=ActivityTypes.message,
            channel_id=request_activity.channel_id,
            conversation=request_activity.conversation,
            recipient=request_activity.from_property,
            from_property=request_activity.recipient,
            text=text,
            service_url=request_activity.service_url)

    def __handle_conversation_update_activity(self, activity):
        self.send_response(202)
        self.end_headers()
        if activity.members_added[0].id != activity.recipient.id:
            credentials = MicrosoftAppCredentials(APP_ID, APP_PASSWORD)
            reply = BotRequestHandler.__create_reply_activity(activity, 'Hello and welcome to the MOVIE BOT ! 📽')
            connector = ConnectorClient(credentials, base_url=reply.service_url)
            connector.conversations.send_to_conversation(reply.conversation.id, reply)

    def __handle_message_activity(self, activity):
        self.send_response(200)
        self.end_headers()
        credentials = MicrosoftAppCredentials(APP_ID, APP_PASSWORD)
        connector = ConnectorClient(credentials, base_url=activity.service_url)
        a=''
        b=''
        res=''
        res=activity.text
        p1=Person(activity.text)
        a=p1.getIntent()
        b=p1.getEntity() 
        print("intent:"+a)
        print("entitty:"+b)
        if(a=="starters"):
            res="hello I am a movie bot \n I will give you ratings, reviews, cast and crew and all other movie details  😊 "
        elif(a=="review" or a=="rating"):
            r=Scrap(b,a)
            res=r.getAnswer()
        elif(a=="grattitude"):
            res="you are welcome \n I am your assistant after all  😊"
        elif(a=="crew"):
            r=Scrap4(b,a)
            res=r.getAnswer()
        elif(a=="details"):
            r=Scrap2(b,a)
            res=r.getAnswer()
        elif(a=="movie collections"):
            r=Scrap3(b,a)
            res=r.getAnswer()
        elif(a=="trending movies"):
            r=Scrap5(b,a)
            res=r.getAnswer()


        #res=a+" "+b

            
        #here databse comes into role where movie name matches with the reviews
        l="🤟"
        res=res+" "+l
        reply = BotRequestHandler.__create_reply_activity(activity, 'movie bot: %s' % res)
        print (activity.text)
        connector.conversations.send_to_conversation(reply.conversation.id, reply)

    def __handle_authentication(self, activity):
        credential_provider = SimpleCredentialProvider(APP_ID, APP_PASSWORD)
        loop = asyncio.new_event_loop()
        try:
            loop.run_until_complete(JwtTokenValidation.authenticate_request(
                activity, self.headers.get("Authorization"), credential_provider))
            return True
        except Exception as ex:
            self.send_response(401, ex)
            self.end_headers()
            return False
        finally:
            loop.close()

    def __unhandled_activity(self):
        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        body = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(str(body, 'utf-8'))
        activity = Activity.deserialize(data)

        if not self.__handle_authentication(activity):
            return

        if activity.type == ActivityTypes.conversation_update.value:
            self.__handle_conversation_update_activity(activity)
        elif activity.type == ActivityTypes.message.value:
            self.__handle_message_activity(activity)
        else:
            self.__unhandled_activity()


try:
    SERVER = http.server.HTTPServer(('0.0.0.0', 9000), BotRequestHandler)
    print('Started http server')
    SERVER.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down server')
    SERVER.socket.close()
#app = web.Application()
#app.router.add_post('/', messages)

#try:
    #web.run_app(app, host='localhost', port='9000')
    #print('started http server')
#except Exception as e:
    #aise e