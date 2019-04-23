

# an employee has an identifier, first name, last name, and a list of worked jobs
class Employee:

    def __init__(self, employee_id, firstname, lastname):
        self.employee_id = employee_id
        self.firstname = firstname
        self.lastname = lastname
        self.worked_jobs = []

    def add_worked_job(self, new_worked_job):
        self.worked_jobs.append(new_worked_job)

    def get_total_hours(self):
        total_hours = 0
        for job in self.worked_jobs:
            total_hours += job.hours
        return total_hours

    def get_total_pay(self):
        total_pay = 0
        for job in self.worked_jobs:
            hours = job.hours
            pay_rate = job.pay_rate
            total_pay += (hours * pay_rate)
        return total_pay

    def to_string(self):
        return ("Employee " + str(self.employee_id) + " (" + self.firstname + " " + self.lastname + ")" + "\n\t"
                "Hours: " + str(self.get_total_hours()) + "\n\t"
                "Pay: $" + str(self.get_total_pay()))
