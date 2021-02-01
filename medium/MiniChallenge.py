class programmer:
    '''Python Classes Mini Challenge'''
    def __init__(self, salary, work_hours):
        self.salary = salary
        self.work_hours = work_hours


    # Deletes the created object resources if you will
    def __del__(self):
        return "oof, {}, {}".format(self.salary, self.work_hours)


    # A custom comparizon that returns lowest sallary
    def compare(self, dev2):
        #prints the lowest salary
        if self.salary > dev2.salary:
            return dev2.salary
        else:
            return self.salary
        # If salary is the same, then it compares work hours instead
        if self.salary == dev2.salary:
            return min(self.work_hours, dev2.work_hours)





prog = programmer(35000, 5)
prog2 = programmer(30000, 10)

print(prog.compare(prog2))


