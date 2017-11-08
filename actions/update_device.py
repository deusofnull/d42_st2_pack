from st2actions.runners.pythonrunner import Action
import time, requests, json, random, string 

class Update_Device(Action):

    def get(self, url, user, pw):
        try:
            res = requests.get(
                url,
                auth=(user, pw),
                headers={'Accept': 'application/json'},
                verify=False # https call to localhost requires skipping verification
            )
        except requests.exceptions.RequestsException as e: 
            self.logger.error( e ) 
            sys.exit(1) 
        self.logger.info("HTTP GET %s - status: %s " % (url, res.status_code) )   
        
        return res


    def put(self, url, payload, user, pw):
        
        try:  
            res = requests.put(
                url,
                auth=(user, pw),
                headers={'Accept': 'application/json'}, 
                data=payload,
                verify=False # https call to localhost requires skipping verification
            )
        except requests.exceptions.RequestsException as e:
            self.logger.error( e )
            sys.exit(1)
        self.logger.info("HTTP GET %s - status: %s " % (url, res.status_code) ) 
        
        return res 
        
         
    def run(self, identifier, identifier_type, changes, d42_host, d42_api_path, d42_user, d42_pass):
        full_device = {} 
        
        with open('/home/stanley/update_device.out', 'a') as out:
            out.write("update_device ran at: %s" % time.strftime("%Y-%m-%d %H:%M") ) 
        print "hey we're running at: %s " % time.strftime("%Y-%m-%d %H:%M")  
        
        
        # random_tag = [random.choice(string.letters) for i in range(10) ]
        # random_tag = ''.join(random_tag) 
        
        
        payload = {identifier_type: identifier}  
        payload.update(changes) # include the KVP changes meant to change the device 
        
        url = d42_host + d42_api_path + 'device/'
        
        print "wrote url as " + url 
        
        response = self.put(url, payload,  d42_user, d42_pass) 
        # full_device = json.loads(response.text)        
        # print full_device 
        return full_device 

