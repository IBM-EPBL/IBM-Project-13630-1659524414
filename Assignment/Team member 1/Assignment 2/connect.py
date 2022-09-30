import ibm_db

def list_all():
    sql = "SELECT * from STUDENT_DB"
    stmnt = ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmnt)
    while dictionary != False:
        print ("The ID is : ",  dictionary["e-mail"])
        print ("The Name is : ", dictionary["USERNAME"])
        print ("The Roll-no is : ", dictionary["roll-no"])
        print ("The Password is : ", dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmnt)

def insert_values(email,USERNAME,rollno,PASSWORD):
    sql = "INSERT INTO STUDENT_DB VALUES('{}','{}','{}','{}')".format(email,USERNAME, 'roll-no',PASSWORD)
    stmnt = ibm_db.exec_immediate(conn,sql)
    print("Number of affected rows: ", ibm_db.num_rows(stmnt))

try:
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=32286;PROTOCOL=TCPIP;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=nxp43498;PWD=92OJXkPynB06dP2L;",'', '') 
    print("connected to db")
    
    insert_values("123@gmail","123","6","1234")
    list_all()
    
except:
    print("connection failed")
