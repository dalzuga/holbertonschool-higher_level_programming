import peewee

my_models_db = peewee.SqliteDatabase("my_models.db", pragmas=(
('foreign keys', True),
))

class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique=True)
    class Meta:
        database = my_models_db
        order_by = ('id', )

class School(BaseModel):
    name = peewee.CharField(128, null = False)

    def __str__(self):
        return "School: %s (%d)" % (self.name, self.id)

class Batch(BaseModel):
    school = peewee.ForeignKeyField(School, related_name='batches', on_delete="CASCADE")
    name = peewee.CharField(128, null = False)

    def __str__(self):
        return "Batch: %s (%d)" % (self.name, self.id)

class User(BaseModel):
    first_name = peewee.CharField(128, null = False)
    last_name = peewee.CharField(128, null = False)
    age = peewee.IntegerField(null = False)

    def __str__(self):
        return "User: %s %s (%d)" % (self.first_name, self.last_name, self.id)

class Student(User):
    batch = peewee.ForeignKeyField(Batch, related_name='students', on_delete="CASCADE")

    def __str__(self):
        return "Student: %s %s (%d)" % (self.first_name, self.last_name, self.id)
