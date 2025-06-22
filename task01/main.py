def total_salary(path):
    try:
        salaries = []
        with open(path, 'r', encoding='utf-8') as file:
            developer_data = file.readlines()
            for developer in developer_data:
                salaries.append(developer.strip().split(',')[1])
    
        total = 0
        for salary in salaries:
            total += int(salary)

        avegare = int(total / len(salaries))

        return (total, avegare)
    except IndexError:
        print('File with salary info damaged')
        return(None, None)
    except FileNotFoundError:
        print('File with salary info doesn\'t exist')
        return(None, None)
    except:
        print('File with salary info doesn\'t exist or damaged')
        return(None, None)

if __name__ == '__main__':
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")