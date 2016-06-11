#!/usr/bin/python
import sys
import models

''' check for usage and process input '''
if len(sys.argv) < 2:
    print "Please enter an action"
elif (sys.argv[1] == "create"):
    models.my_models_db.connect()
    models.my_models_db.create_tables(
        [
            models.School,
            models.Batch,
            models.User,
            models.Student
        ], safe=True)
    models.my_models_db.close()
elif (sys.argv[1] == "print"):
    if (sys.argv[2] == "school"):
        for school in models.School().select():
            print school
    elif (sys.argv[2] == "batch"):
        for batch in models.Batch().select():
            print batch
    elif (sys.argv[2] == "user"):
        for user in models.User().select():
            print user
    elif (sys.argv[2] == "student"):
        for student in models.Student().select():
            print student
elif (sys.argv[1] == "insert"):
    if (sys.argv[2] == "school"):
        school = models.School.create(name=sys.argv[3])
        school.save()
        print "New " + sys.argv[2] + ": %s" % school
    elif (sys.argv[2] == "batch"):
        batch = models.Batch.create(
            school=sys.argv[3],
            name=sys.argv[4]
            )
        batch.save()
        print "New " + sys.argv[2] + ": %s" % batch
    elif (sys.argv[2] == "student"):
        student = models.Student.create(
            batch=sys.argv[3],
            age=sys.argv[4],
            last_name=sys.argv[5],
            first_name=sys.argv[6]
            )
        student.save()
        print "New " + sys.argv[2] + ": %s" % student
elif (sys.argv[1] == "delete"):
    if (sys.argv[2] == "school"):
        try:
            school = models.School.get(models.School.id == sys.argv[3])
            school.delete_instance()
            print "Deleted: " + sys.argv[2] + ": %s" % school
        except models.School.DoesNotExist:
            print "Nothing to delete"
    elif (sys.argv[2] == "batch"):
        try:
            batch = models.Batch.get(models.Batch.id == sys.argv[3])
            batch.delete_instance()
            "Deleted: " + sys.argv[2] + ": %s" % batch
        except models.Batch.DoesNotExist:
            print "Nothing to delete"
    elif (sys.argv[2] == "student"):
        try:                
            student = models.Student.get(models.Student.id == sys.argv[3])
            student.delete_instance()
            "Deleted: " + sys.argv[2] + ": %s" % student
        except models.Student.DoesNotExist:
            print "Nothing to delete"
elif (sys.argv[1] == "print_batch_by_school"):
    try:
        models.School.get(models.School.id == sys.argv[2])
        for batch in models.Batch.select().where(models.Batch.school == sys.argv[2]):
            print batch
    except models.School.DoesNotExist:
        print "School not found"
elif (sys.argv[1] == "print_student_by_batch"):
    try:
        models.Batch.get(models.Batch.id == sys.argv[2])
        for student in models.Student.select().where(models.Student.batch == sys.argv[2]):
            print student
    except models.Batch.DoesNotExist:
        print "Batch not found"
elif (sys.argv[1] == "print_student_by_school"):
    try:
        models.School.get(models.School.id == sys.argv[2])
        '''        for student in (
            models.Student
            .select()
            .join(models.Batch)
            .where(models.Batch.school == sys.argv[2])
            ):
            print student'''
        for student in (models
                        .Batch.select()
                        .where(models.Batch.school == sys.argv[2])
                        .get().students):
            print student
    except models.School.DoesNotExist:
        print "School not found"
else:
    print "Undefined action " + sys.argv[1]
