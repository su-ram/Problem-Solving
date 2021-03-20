def solution(table, languages, preference):
    answer = ''




    return answer


a = ["PYTHON", "C++", "SQL"]
b = [7,5, 5]
c = zip(a,b)
lang_pref = dict(zip(a,b))
table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
result = "zzz"
max_score = -1

for jobs in table:

        job = jobs.split()[0]
        splitted_array = jobs.split()
        job = splitted_array[0]
        job_lang = splitted_array[1:]
        scores = dict(zip(job_lang, list(range(5,0,-1))))

        score = 0
        for lang in lang_pref:
            score += lang_pref[lang] * scores.get(lang,0)

        print(job, score)
        if score > max_score:
            result = job
            max_score=score

        elif score == max_score and job < result:
            result = job
            max_score = score

print(result)

