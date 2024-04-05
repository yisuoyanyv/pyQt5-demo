import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName("sportsdatabase.db")

    if not db.open():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.critical)
        msg.setText("Error in Database Creation")
        retval = msg.exec_()
        return False
    query = QSqlQuery()

    query.exec_("create table sportsmen( id int primary key, "" firstname varchar(20), lastname varchar(20) )")
    query.exec_("insert into sportsmen values(101,'Roger','Federer')")
    query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
    query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
    query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
    query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
    return True




if __name__ ==  "__main__":
    app=QApplication(sys.argv)
    createDB()