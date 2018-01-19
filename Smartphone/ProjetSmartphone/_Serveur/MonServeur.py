from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import cgi    
import UbiquitousGame

model = UbiquitousGame.UbiquitousGame()

class HTTPHandler (SimpleHTTPRequestHandler):
        server_version = "MonServeurHTTP/0.1"
        
#        def __init__(self,model):
#            self.model=mode
        
        def do_GET(self):
            # La requete contient-elle des parametres
            if self.path.find('?') != -1:
                self.path, self.requete = self.path.split('?', 1)
                # On parse les arguments
                args=dict(cgi.parse_qsl(self.requete))
                # On cherche la commande concernee
                try:
                    cmd=args["cmd"]
                    print args
                
                    if cmd=="addteammember":
                        team  =   args["team"]
                        name  =   args["name"]
                        return self.add_team_member(team,name)
                    if cmd=="delteammember":
                        team  =   args["team"]
                        name  =   args["name"]
                        return self.del_team_member(team,name)
                    
                    if cmd=="listteammembers":
                        team  =   args["team"]
                        return self.list_team_members(team)
                
                    if cmd=="listteam":
                        return self.list_team()
                                       
                    if cmd=="setlocalization":
                        name    =   args["name"]
                        team    =   args["team"]
                        lat     =   args["latitude"]
                        long    =   args["longitude"]
                        return self.set_localization(team,name,lat,long)
                    
                    if cmd=="getteammemberlocation": 
                        name    =   args["name"]
                        team    =   args["team"]
                        return self.get_team_member_location(team,name)
                    
                    if cmd=="sendmessagetoteam":
                        team    =   args["team"]
                        msg     =   args["message"]
                        return self.send_message_to_team(team,msg)
                    
                    if cmd=="getlastmessagetoteam":
                        team    =   args["team"]
                        return self.get_last_message_to_team(team)
                    
                    if cmd=="getnextgoal":
                        team    =   args["team"]
                        return self.get_next_goal(team)

                    if cmd=="save":
                        return self.save()

                    if cmd=="load":
                        return self.load()
                    
                    if cmd=="initgame":
                        return self.init_game()

                    
                except:
                    return self.erreur()
                
            SimpleHTTPRequestHandler.do_GET(self)
            
        def get_team_member_location(self,team,name):
            self.reponse()
            s=model.get_team_member_location(team,name)
            self.wfile.write(s)
            return None

        def send_message_to_team(self,team,msg):
            self.reponse()
            model.send_message_to_team(team, msg)
            self.wfile.write('Message envoye a %s' % team)
#            self.wfile.write('<h2>dans l\'equipe %s</h2>' % team)
            return None
        
        def get_last_message_to_team(self,team):
            self.reponse()
            msg=model.get_last_message_to_team(team)
            self.wfile.write('%s' % msg)
#            self.wfile.write('<h2>dans l\'equipe %s</h2>' % team)
            return None
            
        def add_team_member(self,team,name):
            self.reponse()
            model.add_team_member(team, name)
            self.wfile.write('Ajout de %s ' % name)
            self.wfile.write('dans %s' % team)
            return None
        
        def del_team_member(self,team,name):
            print "*** Del team member ***"
            self.reponse()
            model.del_team_member(team, name)
            self.wfile.write('Suppression de %s ' % name)
            self.wfile.write('dans %s' % team)
            return None
        
        def list_team_members(self,team):
            self.reponse()
            liste=model.list_team_members(team)
            for i in liste:
                self.wfile.write('%s,' % i)
            return None

        def list_team(self):
            self.reponse()
            liste=model.list_team()
            for i in liste:
                self.wfile.write('%s,' % i)
            return None
        
        def set_localization(self,team,name,lat,long):
            self.reponse()
            res=model.set_localization(team, name, lat, long)
            if res==True:
                self.wfile.write('Vous avez trouve le lieu')
                model.send_message_to_team(team, 'Le lieu a ete trouve par votre equipe')
                #self.send_message_to_team(team, 'Le lieu a ete trouve par votre equipe')
            return None
        
        def get_next_goal(self,team):
            self.reponse()
            res = model.get_next_goal(team)
            print res
            if res == None:
                self.wfile.write('Le jeu est gagne par l\'equipe %s'  % team)
            else:
                self.wfile.write('Prochain but %s <br>' % res[0])
                self.wfile.write('%s,' % res[1])    # Latitude
                self.wfile.write('%s' % res[2])     # Longitude
            return None
        
        def save(self):
            self.reponse()
            model.save()
            self.wfile.write('<h1>Sauvegarde OK</h1>')
            return None
        
        def load(self):
            self.reponse()
            model.load()
            self.wfile.write('<h1>Chargement OK</h1>')
            return None        
        
        def init_game(self):
            self.reponse()
            model.init_game()
            self.wfile.write('<h1>Init OK</h1>')
            return None 
                         
        def erreur(self):
            self.send_error(404, "Je n'arrive pas a trouver ce que vous voulez %s" % self.path)
            return None

        def reponse(self):
            self.send_response(200, 'OK')
            self.send_header('Content-type', 'text/html')
            self.end_headers()           

        def do_POST(self):
            return self.erreur()
        

#            self.requete = self.rfile.read(int(self.headers['Content-Length']))
#            self.reponse()
         
if __name__ == '__main__':
    httpd = HTTPServer(('', 8000), HTTPHandler)
    print "<<< Serveur lance >>>"
    httpd.serve_forever()