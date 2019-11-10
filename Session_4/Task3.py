import csv


def top_students(file_path, num_of_students):
    output = []

    with open(file_path, newline='') as csvf:
        csvf_content = csv.reader(csvf)
        sorted_csvf = sorted(csvf_content, key=lambda row: row[2], reverse=True)

        for row in sorted_csvf[1:num_of_students+1]:
            output.append(row[0])
    return output


def student_in_age_order(file_path):
    with open(file_path) as csvf:
        csvf_content = csv.reader(csvf)
        csvf_content = sorted(csvf_content, key=lambda row: row[1], reverse=True)

    with open('data/sorted_by_age.csv', 'w', newline='') as csvf:
        writer = csv.writer(csvf)
        for row in csvf_content:
            writer.writerow(row)


print(top_students('data/students.csv', 5))
student_in_age_order('data/students.csv')
