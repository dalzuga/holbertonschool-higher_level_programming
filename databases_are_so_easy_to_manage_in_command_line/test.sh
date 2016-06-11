chmod +x ./main.py
rm my_models.db
./main.py create
./main.py insert school Avengers
./main.py insert school GoT
./main.py insert batch 1 0116sf
./main.py print school
./main.py insert batch 2 "winter 2017"
./main.py insert batch 1 "may batch"
./main.py insert student 1 25 Alzugaray Daniel
./main.py insert student 1 35 Stark Tony
./main.py insert student 1 60 Rogers Steve
./main.py insert student 2 30 Targaryen Daenerys
./main.py insert student 2 15 Stark Sansa
./main.py insert student 2 30 "of Tarth" Brienne
./main.py print_student_by_school 2