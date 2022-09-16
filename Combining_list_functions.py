from functools import reduce
# Combining List Functions

# list of employees data stored as dictionaries inside a list
employees = [
    {
        'name': 'Jane',
        'salary': 90000,
        'job_title': 'developer'
    }, {
        'name': 'Bill',
        'salary': 50000,
        'job_title': 'writer'
    }, {
        'name': 'Kathy',
        'salary': 120000,
        'job_title': 'executive'
    },
    {
        'name': 'James',
        'salary': 95000,
        'job_title': 'developer'
    },
    {
        'name': 'Albert',
        'salary': 70000,
        'job_title': 'marketing specialist'
    }
]


def is_developer(employee):
    return employee['job_title'] == 'developer'


def is_not_developer(employee):
    return employee['job_title'] != 'developer'


non_developers = list(filter(is_developer, employees))

developers = list(filter(is_developer, employees))


def get_salary(employee):
    return employee['salary']


developer_salaries = list(map(get_salary, developers))
non_developer_salaries = list(map(get_salary, non_developers))


print(developer_salaries)

sum(developer_salaries)


def get_sum(acc, x):
    return acc + x


total_developer_salaries = reduce(get_sum, developer_salaries)
average_developer_salary = total_developer_salaries / len(developer_salaries)
print(average_developer_salary)
print(total_developer_salaries)
