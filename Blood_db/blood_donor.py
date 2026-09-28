import mysql.connector
class bloodDonor:
    def __init__(self):
        self.connection=mysql.connector.connect(user='root',password='root',host='localhost',database='blood_db')
        self.cursor=self.connection.cursor()
        print('Successfully  Connected to MySQL database')

    def post(self,name,bloodgroup,phone,city,last_donation):
        query='insert into donor_detail  (name,bloodgroup,phone,city,last_donation) values(%s,%s,%s,%s,%s)'
        data=(name,bloodgroup,phone,city,last_donation)
        self.cursor.execute(query,data)
        self.connection.commit()
        print('Successfully created donor Data')

    def get(self,id):
        query='select * from donor_detail where id=%s'
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
          return record

    def get_id(self,id):
        query='select * from donor_detail  where id=%s'
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            return record

    def delete(self,id):
        query='delete from donor_detail  where id=%s'
        data=(id,)
        self.cursor.execute(query,data)
        print('Successfully Deleted Donor Data')

    def put(self,id,name,bloodgroup,phone,city,last_donation):
        query='update donor_detail  set name=%s,bloodgroup=%s,phone=%s,city=%s,last_donation where id=%s'
        data=(name,bloodgroup,phone,city,last_donation,id)
        self.cursor.execute(query,data)
        print('Successfully Updated Donor Data')

c=bloodDonor()
# p=c.post('Karthik','B+',8590710038,'Wayanad','2026-12-06')
# print(p)
# p=c.get(3)
# print(p)
