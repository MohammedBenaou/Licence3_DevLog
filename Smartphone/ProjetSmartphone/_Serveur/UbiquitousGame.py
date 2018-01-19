# coding=utf-8
import random
import pickle

LISTEDESSITES = [{'num': '10', 'lat': '46.15885', 'lon': '-1.1466669444', 'name': "Porte Maubec", 'color': 'vert', 'bikeCount': '2 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '11', 'lat': '46.167222', 'lon': '-1.150378', 'name': "Porte Dauphine", 'color': 'vert', 'bikeCount': '4 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '20', 'lat': '46.146667', 'lon': '-1.157856', 'name': "Faculte de Sciences 2", 'color': 'vert', 'bikeCount': '3 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '05', 'lat': '46.162778', 'lon': '-1.1525', 'name': "Hetel de Police", 'color': 'vert', 'bikeCount': '5 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '26', 'lat': '46.138096', 'lon': '-1.152222', 'name': "Maison du Departement", 'color': 'vert', 'bikeCount': '3 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '04', 'lat': '46.161389', 'lon': '-1.148989', 'name': "Marche", 'color': 'vert', 'bikeCount': '3 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '17', 'lat': '46.152878', 'lon': '-1.145856', 'name': "Gare 2", 'color': 'vert', 'bikeCount': '4 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '06', 'lat': '46.162322', 'lon': '-1.153711', 'name': "Place de Verdun", 'color': 'vert', 'bikeCount': '4 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '08', 'lat': '46.156767', 'lon': '-1.153989', 'name': "Vieux Port", 'color': 'vert', 'bikeCount': '7 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '03', 'lat': '46.1599', 'lon': '-1.148711', 'name': "Arsenal", 'color': 'vert', 'bikeCount': '5 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '21', 'lat': '46.1483', 'lon': '-1.153611', 'name': "Technoforum 1", 'color': 'vert', 'bikeCount': '1 v&eacute;lo', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '15', 'lat': '46.15505', 'lon': '-1.149822', 'name': "Office de Tourisme", 'color': 'vert', 'bikeCount': '3 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '24', 'lat': '46.140556', 'lon': '-1.153651', 'name': "EIGSI 1", 'color': 'noir', 'bikeCount': '0 v&eacute;lo', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '01', 'lat': '46.1598916667', 'lon': '-1.1512888889', 'name': "Hetel de Ville", 'color': 'vert', 'bikeCount': '3 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '13', 'lat': '46.153889', 'lon': '-1.152778', 'name': "Mediatheque", 'color': 'vert', 'bikeCount': '4 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '16', 'lat': '46.152978', 'lon': '-1.145656', 'name': "Gare 1", 'color': 'vert', 'bikeCount': '5 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '22', 'lat': '46.162978', 'lon': '-1.145833', 'name': "Place des Cordeliers", 'color': 'vert', 'bikeCount': '7 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '14', 'lat': '46.152222', 'lon': '-1.153611', 'name': "Bibliotheque Universitaire ", 'color': 'vert', 'bikeCount': '2 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '07', 'lat': '46.15699', 'lon': '-1.156844', 'name': "Prefecture", 'color': 'vert', 'bikeCount': '4 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '25', 'lat': '46.142044', 'lon': '-1.1527', 'name': "IUT 2", 'color': 'vert', 'bikeCount': '7 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '02', 'lat': '46.1577111111', 'lon': '-1.1505777778', 'name': "Quai Valin", 'color': 'noir', 'bikeCount': '0 v&eacute;lo', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '23', 'lat': '46.163651', 'lon': '-1.146767', 'name': "Place Cacaud", 'color': 'noir', 'bikeCount': '0 v&eacute;lo', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '25', 'lat': '46.142044', 'lon': '-1.1526', 'name': "IUT 1", 'color': 'vert', 'bikeCount': '6 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '20', 'lat': '46.146667', 'lon': '-1.158056', 'name': "Faculte de Sciences 1", 'color': 'vert', 'bikeCount': '5 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '12', 'lat': '46.168611', 'lon': '-1.153611', 'name': "Piscine", 'color': 'vert', 'bikeCount': '3 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '09', 'lat': '46.1556638889', 'lon': '-1.1490972222', 'name': "Porte St Nicolas", 'color': 'vert', 'bikeCount': '2 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '27', 'lat': '46.175', 'lon': '-1.219722', 'name': "Belvedere", 'color': 'gris', 'bikeCount': '0 v&eacute;lo', 'freelockCount': '0', 'lockCount': '0 place'}, {'num': '28', 'lat': '46.161944', 'lon': '-1.21145', 'name': "Ecole de La Pallice", 'color': 'vert', 'bikeCount': '1 v&eacute;lo', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '29', 'lat': '46.168056', 'lon': '-1.200278', 'name': "Mairie Annexe de Laleu", 'color': 'vert', 'bikeCount': '2 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '30', 'lat': '46.169822', 'lon': '-1.183889', 'name': "Centre Cial. Louis Guillet", 'color': 'vert', 'bikeCount': '3 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '31', 'lat': '46.1658', 'lon': '-1.17865', 'name': "Mairie Annexe de Mireuil", 'color': 'vert', 'bikeCount': '5 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '32', 'lat': '46.164344', 'lon': '-1.175833', 'name': "Place St Maurice", 'color': 'vert', 'bikeCount': '1 v&eacute;lo', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '33', 'lat': '46.1594', 'lon': '-1.1798', 'name': "Marche de Port Neuf", 'color': 'vert', 'bikeCount': '3 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '34', 'lat': '46.16865', 'lon': '-1.16895', 'name': "Maison de l'Emploi", 'color': 'vert', 'bikeCount': '3 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '36', 'lat': '46.15965', 'lon': '-1.1659', 'name': "La Genette", 'color': 'vert', 'bikeCount': '2 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '37', 'lat': '46.1558', 'lon': '-1.1608', 'name': "Plage de la Concurrence 1", 'color': 'vert', 'bikeCount': '2 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '37', 'lat': '46.1557', 'lon': '-1.1606', 'name': "Plage de la Concurrence 2", 'color': 'vert', 'bikeCount': '2 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '39', 'lat': '46.177225', 'lon': '-1.1516027778', 'name': "Vieljeux", 'color': 'vert', 'bikeCount': '4 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '40', 'lat': '46.167222', 'lon': '-1.140556', 'name': "Cite Administrative Mangin", 'color': 'vert', 'bikeCount': '1 v&eacute;lo', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '42', 'lat': '46.161175', 'lon': '-1.1277', 'name': "LEP de Rompsay", 'color': 'vert', 'bikeCount': '5 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '43', 'lat': '46.1518438889', 'lon': '-1.1227780556', 'name': "Mairie Annexe de Villeneuve", 'color': 'vert', 'bikeCount': '2 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '44', 'lat': '46.1521', 'lon': '-1.12508', 'name': "Centre Cial. de Villeneuve", 'color': 'vert', 'bikeCount': '5 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '45', 'lat': '46.152778', 'lon': '-1.140378', 'name': "P+R Jean-Moulin", 'color': 'vert', 'bikeCount': '2 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '46', 'lat': '46.148433', 'lon': '-1.143989', 'name': "Eglise de Tasdon", 'color': 'vert', 'bikeCount': '5 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '21', 'lat': '46.1483', 'lon': '-1.153711', 'name': "Technoforum 2", 'color': 'noir', 'bikeCount': '0 v&eacute;lo', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '48', 'lat': '46.14135', 'lon': '-1.17035', 'name': "Plage des Minimes 1", 'color': 'vert', 'bikeCount': '6 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '49', 'lat': '46.1414', 'lon': '-1.17045', 'name': "Plage des Minimes 2", 'color': 'vert', 'bikeCount': '5 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '24', 'lat': '46.1406', 'lon': '-1.153651', 'name': "EIGSI 2", 'color': 'noir', 'bikeCount': '0 v&eacute;lo', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '51', 'lat': '46.138811', 'lon': '-1.145', 'name': "Gymnase Universitaire", 'color': 'vert', 'bikeCount': '5 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '38', 'lat': '46.1559444444', 'lon': '-1.1695555556', 'name': "Clinique du Mail", 'color': 'vert', 'bikeCount': '2 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '53', 'lat': '46.162456', 'lon': '-1.15916', 'name': "Les Parcs", 'color': 'vert', 'bikeCount': '3 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '55', 'lat': '46.176272', 'lon': '-1.134768', 'name': "Hopital Marius Lacroix", 'color': 'vert', 'bikeCount': '2 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '54', 'lat': '46.160401', 'lon': '-1.171026', 'name': "Eglise de La Genette", 'color': 'vert', 'bikeCount': '5 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}, {'num': '56', 'lat': '46.1587888889', 'lon': '-1.1443055556', 'name': "Hopital St Louis", 'color': 'vert', 'bikeCount': '3 v&eacute;los', 'freelockCount': '0', 'lockCount': '8 places'}]

class UbiquitousGame(object):
    def __init__(self):
        self.EPS = 0.0001
        self.data=dict()
        self.data['equipe1']=dict()
        self.data['equipe2']=dict()
        random.shuffle(LISTEDESSITES)
        self.liste=LISTEDESSITES[1:10]

        # Les 2 equipes commencent avec le meme objectif
        self.data['equipe1']['nextgoal']=0
        self.data['equipe2']['nextgoal']=0
        self.data['equipe1']['names']=dict()
        self.data['equipe2']['names']=dict()
        self.data['equipe1']['messages']=[]
        self.data['equipe2']['messages']=[]

    def add_team_member(self,team,name):
        # On initialise le nom avec la localization
        print "Team",team
        self.data[team]['names'][name]=(None,None)

    def del_team_member(self,team,name):
        print "Del team member", team,self.data[team]['names']
        del self.data[team]['names'][name]
    
    def list_team(self):
        print "*** List team ***"
        return self.data
    
    def list_team_members(self,team):
        print "*** List team members ***"
        return self.data[team]['names']
    
    def get_next_goal(self,team):
        try:
            lieu = self.liste[int(self.data[team]['nextgoal'])]
            return (lieu['name'],lieu['lat'],lieu['lon'])
        except:
            return None
        
    def get_team_member_location(self,team,name):
        return self.data[team]['names'][name]
    
    def set_localization(self,team,name,lat,long):
        self.data[team]['names'][name]=(lat,long)
        lieu = self.get_next_goal(team)
        print lieu
        dist = abs(float(lat) - float(lieu[1]))+abs(float(long)-float(lieu[2]))
        print dist
        if dist < self.EPS:  # Le lieu a ete trouve
            # On met a jour le prochain lieu
            self.data[team]['nextgoal']=self.data[team]['nextgoal']+1
            return True
        else:
            return False

    def save(self):
        fichier = open("dump.pick", "w")
        pickle.dump(self.data, fichier)
        fichier.close()
     
    def load(self):
        fichier = open("dump.pick","r")
        self.data=pickle.load(fichier)
        fichier.close()
        
    def init_game(self):
        self.data['equipe1']['nextgoal']=0
        self.data['equipe2']['nextgoal']=0
        self.data['equipe1']['messages']=[]
        self.data['equipe2']['messages']=[]
        
    def send_message_to_team(self,team,message):
        self.data[team]['messages'].append(message)
        
    def get_last_message_to_team(self,team):
        return self.data[team]['messages'].pop()

