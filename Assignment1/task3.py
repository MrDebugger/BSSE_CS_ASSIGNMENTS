#Task 3
print('|'.join([f'{h:^10}' for h in ['Roll No','First Name','Last Name','Semester','SGPA']]))
with open('record.txt') as fp:
    for line in fp.readlines():
        form = [f'{data.strip():^10}' for data in line.split(',') if data]
        print('|'.join(form))
