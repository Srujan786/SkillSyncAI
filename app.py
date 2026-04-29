import os
from flask import Flask, request, render_template

app = Flask(__name__)

skill_roadmap = {
    "python": "Basics, OOP, Data Structures, NumPy, Pandas, Flask/Django",
    "java": "OOP, Collections, JDBC, Spring Boot",
    "c": "Pointers, Memory Management, Data Structures",
    "javascript": "ES6, DOM, React, Node.js",
    "html": "Forms, Semantic Tags",
    "css": "Flexbox, Grid, Responsive Design"
}

def analyze_skills(syllabus, market):
    syllabus_skills = set([s.strip().lower() for s in syllabus.split(",")])
    market_skills = set([m.strip().lower() for m in market.split(",")])

    matched = syllabus_skills & market_skills
    missing = market_skills - syllabus_skills

    score = (len(matched) / len(market_skills)) * 100 if market_skills else 0

    suggestions = []
    for skill in missing:
        if skill in skill_roadmap:
            suggestions.append(f"Learn {skill} → {skill_roadmap[skill]}")
        else:
            suggestions.append(f"Learn {skill}")

    return matched, missing, round(score, 2), suggestions

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        domain = request.form.get("domain", "General")
        syllabus = request.form["syllabus"]
        market = request.form["market"]

        matched, missing, score, suggestions = analyze_skills(syllabus, market)
        
        roadmap = skill_roadmap.get(syllabus.lower(), "No detailed roadmap available for this skill.")

        return render_template("index.html",
                               domain=domain,
                               syllabus=syllabus,
                               market=market,
                               matched=matched,
                               missing=missing,
                               score=score,
                               suggestions=suggestions,
                               roadmap=roadmap)

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)