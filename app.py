from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder=".")

# ── Serve the frontend ─────────────────────────────────────────
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

# ── Main generation endpoint ───────────────────────────────────
@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        

        # Extract fields
        name         = data.get("name", "").strip()
        email        = data.get("email", "").strip()
        phone        = data.get("phone", "").strip()
        location     = data.get("location", "").strip()
        job_title    = data.get("jobTitle", "").strip()
        company_name = data.get("companyName", "").strip()
        skills       = data.get("skills", "").strip()
        experience   = data.get("experience", "").strip()
        education    = data.get("education", "").strip()
        achievements = data.get("achievements", "").strip()
        job_desc     = data.get("jobDescription", "").strip()
        tone         = data.get("tone", "professional").strip()

        if not name or not job_title:
            return jsonify({"error": "Name and Job Title are required."}), 400

        # ── MOCK AI RESPONSE ─────────────────────────────────────
        raw = f"""
---RESUME---

{name} is a highly motivated candidate with strong skills in {skills}.
With experience in {experience}, they have developed solid technical
and problem-solving abilities.

Summary:
Enthusiastic professional targeting the role of {job_title}.

Skills:
{skills}

Experience:
{experience}

Education:
{education}

Achievements:
{achievements}

---COVER LETTER---

Dear Hiring Manager,

I am excited to apply for the position of {job_title} at {company_name}.
With my background in {education} and experience in {skills},
I am confident in my ability to contribute effectively to your team.

I am particularly interested in this opportunity because:
{job_desc}

I look forward to discussing how I can add value to your organization.

Sincerely,
{name}
"""

        # Split response into resume + cover letter
        resume_text = ""
        cover_letter_text = ""

        if "---RESUME---" in raw and "---COVER LETTER---" in raw:
            parts = raw.split("---COVER LETTER---")
            resume_text = parts[0].replace("---RESUME---", "").strip()
            cover_letter_text = parts[1].strip()
        else:
            resume_text = raw

        return jsonify({
            "resume": resume_text,
            "coverLetter": cover_letter_text
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)