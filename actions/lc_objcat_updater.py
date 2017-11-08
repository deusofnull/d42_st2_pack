from st2actions.runners.pythonrunner import Action
from st2client.client import Client 
from st2client.models import KeyValuePair 
import time, requests, json, random, string 

class LC_ObjCat_Updater(Action):

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
         
    def run(self, 
            identifier, identifier_type, lc_type_id, 
            d42_host, d42_api_path, d42_user, d42_pass):
        
        full_device = {} 
         
        st2client = Client(base_url='http://localhost') 
        lc_type_name = st2client.keys.get_by_name(name=lc_type_id) 
        
        # add device identifier to payload   
        payload = {identifier_type: identifier}  
        
        # change obj cat with the LC name (as a basic example) 
        changes = {
            "new_object_category": "%s_lc" % (lc_type_name.value), 
            "tags": "%s_lc_processed" % (lc_type_name.value)  
        }
        
        payload.update(changes) 
 
        url = d42_host + d42_api_path + 'device/'
        print "wrote url as " + url 
        response = self.put(url, payload,  d42_user, d42_pass) 
        return full_device 

