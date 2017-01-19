import pymysql
# 打开数据库连接
db = pymysql.connect("localhost","bfchen","123456","mysql")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")


# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME) 
         VALUES
         ('Mac', 'Mohan1', 20, 'M', 2000),
         ('Mac', 'Mohan2', 20, 'M', 2000), 
         ('Mac', 'Mohan3', 20, 'M', 2000),
         ('Mac', 'Mohan4', 20, 'M', 2000),
         ('Mac', 'Mohan5', 20, 'M', 2000);
         """

try:
   # 执行sql语句
   for i in range(0,100000):
      cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()


# 关闭数据库连接
db.close()
