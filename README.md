# D42 pack for ST2

# Install 

- install this pack on your stackstorm server using st2 install
```
$ st2 pack install https://github.com/deusofnull/d42_st2_pack
```

# Config

- generate API keys for Device42 to utilize when executing webhook requests to the st2 server.  Reference Stackstorm documentation here: https://docs.stackstorm.com/authentication.html#api-keys

- Navigate to Device42 > Tools > Webhooks > Endpoints 

- Configure an endpoint to point towards a webhook sensor implemented via a st2 rule.  Example is upcoming. 
-- Select "ignore certificate errors" for simplicity's sake
-- In the header arguments, set a field 'St2-Api-Key' to the API key created by st2. 
-- Set 'Content-Type' to 'application/json'

- Navigate to Device42 > Tools > Webhooks > Actions 

- Configure a webhook action that responds to create, update, and delete events on any of your device42 objects, devices themselves for example.  Set the actions endpoint to the endpoint created in the previous step. 

- Now your D42 should publish webhook events to Stackstorm.  

- If you are querying Device42 from Stackstorm, you will need to provide information about your Device42 instance to stackstorm in schema config file.  This file is located in the d42 pack directory on the stackstorm server at `/opt/stackstorm/packs/d42/config.schema.yaml`.  Set your host, api path (typically /api/1.0/), username, and password.  These will now be the default values used by the actions found in this pack, should you not provide them.  

# Todo: 
- Complie documentation 
- Write tutorial
- Merge with existing D42 package for device42... 


