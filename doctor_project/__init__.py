import pymysql

# Add this line to trick Django's version check
pymysql.version_info = (1, 4, 3, "final", 0)

pymysql.install_as_MySQLdb()