#!/usr/bin/python
import sys
import models

''' check for usage and process input '''
if len(sys.argv) < 2:
    print "Please enter an action"
elif (sys.argv[1] == "create"):
    models.BaseModel.create_table()
    print "create"
elif (sys.argv[1] == "print"):
    if len(sys.argv) < 3:
        pass
    elif (sys.argv[2] == "school"):
        print models.my_models_db.School()
    elif (sys.argv[2] == "batch"):
        print models.my_models_db.Batch()
    elif (sys.argv[2] == "user"):
        print models.my_models_db.User()
    elif (sys.argv[2] == "student"):
        print models.my_models_db.Student()
elif (sys.argv[1] == "insert"):
    if len(sys.argv) < 3:
        pass
    elif (sys.argv[2] == "school"):
        models.School.create_table();
    elif (sys.argv[2] == "batch"):
        models.School.create_table();
    elif (sys.argv[2] == "user"):
        models.School.create_table();
    elif (sys.argv[2] == "student"):
        models.School.create_table();
    print "insert"
elif (sys.argv[1] == "delete"):
    print "delete"
else:
    print "Undefined action " + sys.argv[1]
