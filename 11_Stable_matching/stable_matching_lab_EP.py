import math

def stable_matching(capacities, student_prefs, uni_scores_matrix):
    """
    Chcemy znaleźć stabilne przypisania studentów do uczelni (zakładając, że to studenci iteracyjnie składają podania)

    Argumenty:
    - capacities: List[int], liczba miejsc na każdym uniwersytecie
    - student_prefs: List[List[int]], indeksy uniwersytetów uszeregowanych przez studentów od najlepszego do najgorszego
    - uni_scores_matrix: List[List[float]], macierz z punktami studentów w rekrutacji na daną uczelnię

    Output:
    - Dict[int, List[int]], słownik w którym do każdego uniwersytetu jest przypisana lista studentów
    """

    match = {i: [] for i in range(len(capacities))}
    students = [i for i in range(len(student_prefs))]

    while students:
        stud = students[0]
        uni = student_prefs[stud][0]
        scores = uni_scores_matrix[uni]
        if len(match[uni]) < capacities[uni]:
            match[uni].append(stud)          #dodaj studenta jesli jest wolne miejsce
            students.remove(stud)
        else:
            to_be_accepted = False
            min_score = math.inf
            min_score_id = -1
            for i in range(capacities[uni]):
                if scores[stud] > scores[match[uni][i]]:
                    to_be_accepted = True
                    if scores[match[uni][i]] < min_score:    #patrzymy jakiego studenta jednak wyrzucamy
                        min_score = scores[match[uni][i]]
                        min_score_id = match[uni][i]
                    break
            if to_be_accepted:
                match[uni].remove(min_score_id)
                student_prefs[min_score_id].remove(uni)
                students.append(min_score_id)
                match[uni].append(stud)
                students.remove(stud)
            else:
                student_prefs[stud].remove(uni)
                students.remove(stud)
                students.append(stud)

    return match

# Example usage:
if __name__ == "__main__":
    caps = [2, 2, 3, 1, 2]
    student_prefs = [
        [0, 1, 2, 3, 4],
        [1, 0, 4, 2, 3],
        [2, 1, 0, 4, 3],
        [3, 2, 0, 1, 4],
        [4, 0, 2, 3, 1],
        [0, 1, 2, 3, 4],
        [1, 4, 3, 2, 0],
        [3, 0, 1, 2, 4],
        [2, 3, 1, 0, 4],
        [4, 1, 2, 3, 0],
    ]

    uni_scores = [
        [90, 80, 85, 88, 92, 75, 78, 86, 89, 91],  # uni0
        [85, 95, 88, 84, 90, 83, 79, 87, 91, 93],  # uni1
        [80, 89, 94, 91, 85, 88, 92, 90, 86, 84],  # uni2
        [70, 75, 72, 95, 88, 90, 89, 93, 77, 76],  # uni3
        [93, 90, 87, 85, 94, 86, 82, 88, 91, 89],  # uni4
    ]

    match = stable_matching(caps, student_prefs, uni_scores)
    for u, studs in match.items():
        print(f"University {u}: assigned students {studs}")

# Example output
# University 0: assigned students [0, 7]
# University 1: assigned students [1, 5]
# University 2: assigned students [2, 8, 6]
# University 3: assigned students [3]
# University 4: assigned students [4, 9]
