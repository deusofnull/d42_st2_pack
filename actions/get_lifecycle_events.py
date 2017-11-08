from st2actions.runners.pythonrunner import Action
import time, requests, json, sys 

class GetLifecycleEvents(Action):
    
    def get(self, url, user, pw, payload):
        try:
            res = requests.get(
                url,
                params=payload,
                auth=(user, pw),
                headers={'Accept': 'application/json'},
                verify=False # https call to localhost requires skipping verification
            )
        except requests.exceptions.RequestsException as e: 
            self.logger.error( e ) 
            sys.exit(1) 
        self.logger.info("HTTP GET %s - status: %s " % (url, res.status_code) )   
        return res

    def run(self, device, lc_type, asset, enduser, date_gt, date_lt,  d42_host, d42_api_path, d42_user, d42_pass):
        
        with open('/home/stanley/get_lifecycle_event.out', 'a') as out:
            out.write("get lifecycle eventran at: %s" % time.strftime("%Y-%m-%d %H:%M") ) 
        
        print "hey we're running at: %s " % time.strftime("%Y-%m-%d %H:%M")  
        
        url = d42_host + d42_api_path + 'lifecycle_event/?' 
        
        payload = {
            'device': device, 
            'type': lc_type, 
            'asset': asset, 
            'enduser': enduser, 
            'date_gt': date_gt, 
            'date_lt': date_lt
        }

        response = self.get(url, d42_user, d42_pass, payload) 
        
        full_device = json.loads(response.text)        
        
        print full_device 
        
        return full_device 

