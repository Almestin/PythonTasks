candidates = [
    {"name": "Олексій", "skills": {"Python", "Django", "Git", "SQL", "English"}},
    {"name": "Марія", "skills": {"Java", "Spring", "SQL", "English", "Docker"}},
    {"name": "Іван", "skills": {"Python", "Git", "Linux"}},
    {"name": "Оксана", "skills": {"Python", "FastAPI", "PostgreSQL", "Git", "English",
                                  "Docker"}}
]

find_results = []

vacancy_requirements = {"Python", "Django", "Git", "SQL", "Docker"}


def calculate_match(candidate_skills, required_skills):
    match_percent = int(len(required_skills.intersection(candidate_skills)) * 100 / len(vacancy_requirements))
    missing_skills = vacancy_requirements - candidate_skills
    if match_percent == 100:
        is_perfect = True
    else:
        is_perfect = False
    return {"match_percent": match_percent, "missing_skills": missing_skills, "is_perfect": is_perfect}


def find_best_candidates(candidates_db, vacancy):
    for candidate in candidates_db:
        if calculate_match(candidate["skills"], vacancy)["match_percent"] >= 50:
            find_results.append([candidate["name"], calculate_match(candidate["skills"], vacancy)["match_percent"], \
                                 calculate_match(candidate["skills"], vacancy)["missing_skills"]])


def print_report(results):
    for result in results:
        print(f"""Кандидат: {result[0]} 
- Відповідність: {result[1]} %
- Не вистачає: {result[2]} 
                """)


find_best_candidates(candidates, vacancy_requirements)
print_report(find_results)
