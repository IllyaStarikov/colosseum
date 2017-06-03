hayword_count, job_description_count = [int(i) for i in input().split(' ')]
haywords = {}

for _ in range(hayword_count):
    keyword, salary = input().split(' ')
    salary = int(salary)
    
    haywords[keyword] = salary

for _ in range(job_description_count):
    sum = 0
    
    string = ""
    while string != ".":
        string = input()
        
        for word in string.split(' '):
            sum += haywords.get(word, 0)
                       
    print(sum)
    