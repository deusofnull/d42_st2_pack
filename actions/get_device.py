from st2actions.runners.pythonrunner import Action
import time, requests, json, sys 

class GetDevice(Action):
    
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

    def run(self, device_id, d42_host, d42_api_path, d42_user, d42_pass):
        
        with open('/home/stanley/update_device.out', 'a') as out:
            out.write("get device ran at: %s" % time.strftime("%Y-%m-%d %H:%M") ) 
        
        print "hey we're running at: %s " % time.strftime("%Y-%m-%d %H:%M")  
        
        url = d42_host + d42_api_path + 'devices/id/' + str(device_id) + '/'
        
        response = self.get(url, d42_user, d42_pass) 
        
        full_device = json.loads(response.text)        
        
        print full_device 
        
        return full_device 

