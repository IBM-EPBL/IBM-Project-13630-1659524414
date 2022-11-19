import ibm_db
try:
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=32286;PROTOCOL=TCPIP;SECURITY=SSL; SSLServerCertificate=DigiCertGlobalRootCA.crt; UID=nxp43498; PWD=mvsmq51v7jDuWj0I;",'', '') 
    print("db connection successfully")
except:
    print("db connection failed")
