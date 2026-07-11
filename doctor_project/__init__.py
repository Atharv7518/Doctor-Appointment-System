import pymysql

# Update this line to trick Django into seeing version 2.2.3 instead of 1.4.6
pymysql.version_info = (2, 2, 3, "final", 0)

pymysql.install_as_MySQLdb()