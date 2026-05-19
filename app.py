from flask import Flask, render_template, request
import os

app = Flask(__name__)

def calculate_wage(data):
    import joblib
    path = os.path.join("model", "v1")
    model = joblib.load(os.path.join(path, "income_model.pkl"))
    imputer = joblib.load(os.path.join(path, "imputer.pkl"))

    input_data = {
        "Company HQ": data['company_hq'],
        "Company Size": data['company_size'],
        "Experience": data['experience'],
        "Gender": data['gender'],
        "Remote / On-Site / Both": data['way_of_working'],
        "Team Leader": team_leader["Όχι"],
        "Education": data['education'],
        "AI / ML": 0,
        "Architect": 0,
        "Automation": 0,
        "BI": 0,
        "Backend": 0,
        "Big Data": 0,
        "Bioinformatics": 0,
        "Blockchain": 0,
        "CRM": 0,
        "Cybersecurity": 0,
        "Data Science": 0,
        "Data engineer": 0,
        "Database": 0,
        "Desktop apps": 0,
        "DevOps": 0,
        "ERP": 0,
        "Embedded": 0,
        "Engineering Manager": 0,
        "FPGA/ASIC": 0,
        "Fintech": 0,
        "Framework Building": 0,
        "Frontend": 0,
        "Full Stack": 0,
        "Gaming": 0,
        "Hardware": 0,
        "Helpdesk": 0,
        "IT Engineer": 0,
        "IT Manager": 0,
        "Integration Engineering": 0,
        "Mobile apps": 0,
        "Networking": 0,
        "QA Automation Engineer": 0,
        "Research Engineer": 0,
        "Robotics": 0,
        "SAP Developer": 0,
        "SDET": 0,
        "SaaS Engineer": 0,
        "Simulation": 0,
        "Site reliability engineering": 0,
        "Software Engineer": 0,
        "Solutions Engineer": 0,
        "System Engineer": 0,
        "Systems": 0,
        "Test engineer": 0,
        "ABAP": 0,
        "AL": 0,
        "Angular": 0,
        "Apex": 0,
        "Assembly": 0,
        "Bash": 0,
        "Bootstrap": 0,
        "C": 0,
        "C#": 0,
        "C++": 0,
        "C/AL": 0,
        "CSS": 0,
        "Cobol": 0,
        "Dart": 0,
        "Delphi": 0,
        "FORTRAN": 0,
        "Flutter": 0,
        "Go": 0,
        "Groovy": 0,
        "HCL": 0,
        "HTML": 0,
        "Java": 0,
        "JavaScript": 0,
        "Kotlin": 0,
        "Kubernetes": 0,
        "LaTeX": 0,
        "MySQL": 0,
        "Node": 0,
        "NodeJS": 0,
        "Objective-C": 0,
        "PHP": 0,
        "PL/SQL": 0,
        "Perl": 0,
        "PostgreSQL": 0,
        "PowerBuilder": 0,
        "Python": 0,
        "R": 0,
        "React": 0,
        "React Native": 0,
        "Ruby": 0,
        "Rust": 0,
        "SAS": 0,
        "SQL": 0,
        "Scala": 0,
        "Solidity": 0,
        "Swift": 0,
        "SystemVerilog": 0,
        "T-SQL": 0,
        "TCL": 0,
        "Terraform": 0,
        "TypeScript": 0,
        "VB.NET": 0,
        "VHDL": 0,
        "Visual Basic": 0,
        "Vue": 0,
        "Wordpress": 0,
        "X++": 0,
        "YAML": 0
    }
    keys_list = list(input_data.values())
    new_data = [keys_list]

    new_data = imputer.transform(new_data)

    prediction = model.predict(new_data)

    print("Predicted Yearly Income:", prediction[0])
    print("Monthly Income:", prediction[0] / 14)

company_hq = {
    "Αθήνα": 0,
    "Θεσσαλονίκη": 1,
    "Επαρχία": 2,
    "Εξωτερικό": 3,
}

way_of_working = {
    "Απομακρυσμένα": 0,
    "Στον χώρο του εργοδότη": 1,
    "Και τα δύο": 2
}

company_size ={
    "1 - 10": 0,
    "11 - 50": 1,
    "51 - 100": 2,
    "101 - 200": 3,
    "201 - 500": 4,
    "501+": 5
}

education = {
    "Χωρίς Δευτεροβάθμια Εκπαίδευση": 0,
    "Λύκειο": 1,
    "ΙΕΚ": 2,
    "Bachelor's": 3,
    "Master": 4,
    "PhD": 5
}

gender = {
    "Άντρας": 0,
    "Γυναίκα": 1
}

team_leader = {
    "Όχι": 0,
    "Ναι": 1
}

job_roles = [
    "AI / ML", "Architect", "Automation", "BI", "Backend", "Big Data",
    "Bioinformatics", "Blockchain", "CRM", "Cybersecurity", "Data Science",
    "Data engineer", "Database", "Desktop apps", "DevOps", "ERP", "Embedded",
    "Engineering Manager", "FPGA/ASIC", "Fintech", "Framework Building",
    "Frontend", "Full Stack", "Gaming", "Hardware", "Helpdesk", "IT Engineer",
    "IT Manager", "Integration Engineering", "Mobile apps", "Networking",
    "QA Automation Engineer", "Research Engineer", "Robotics", "SAP Developer",
    "SDET", "SaaS Engineer", "Simulation", "Site reliability engineering",
    "Software Engineer", "Solutions Engineer", "System Engineer", "Systems",
    "Test engineer"
]

technologies = [
    "ABAP", "AL", "Angular", "Apex", "Assembly", "Bash", "Bootstrap", "C", "C#",
    "C++", "C/AL", "CSS", "Cobol", "Dart", "Delphi", "FORTRAN", "Flutter", "Go",
    "Groovy", "HCL", "HTML", "Java", "JavaScript", "Kotlin", "Kubernetes",
    "LaTeX", "MySQL", "Node", "NodeJS", "Objective-C", "PHP", "PL/SQL", "Perl",
    "PostgreSQL", "PowerBuilder", "Python", "R", "React", "React Native",
    "Ruby", "Rust", "SAS", "SQL", "Scala", "Solidity", "Swift", "SystemVerilog",
    "T-SQL", "TCL", "Terraform", "TypeScript", "VB.NET", "VHDL", "Visual Basic",
    "Vue", "Wordpress", "X++", "YAML"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Collect values (just for demonstration as no formula was provided)
        data = {
            "company_hq": request.form.get('company_hq'),
            "way_of_working": request.form.get('way_of_working'),
            "company_size": request.form.get('company_size'),
            "education": request.form.get('education'),
            "gender": request.form.get('gender'),
            "team_leader": request.form.get('team_leader'),
            "experience": request.form.get('experience'),
        }
        
        # Collect job roles (binary selection)
        selected_roles = request.form.getlist('job_roles')
        role_values = {role: (1 if role in selected_roles else 0) for role in job_roles}
        data.update(role_values)
        
        # Collect technologies (binary selection)
        selected_techs = request.form.getlist('technologies')
        tech_values = {tech: (1 if tech in selected_techs else 0) for tech in technologies}
        data.update(tech_values)
        

        result = "Selection received! (Calculation logic not defined yet)"
        try:
            calculate_wage(data)
        except Exception as e:
            print(f"Error in calculation: {e}")
    return render_template('index.html', 
                           company_hq=company_hq,
                           way_of_working=way_of_working,
                           company_size=company_size,
                           education=education,
                           gender=gender,
                           team_leader=team_leader,
                           job_roles=job_roles,
                           technologies=technologies,
                           result=result)

if __name__ == '__main__':
    app.run(debug=True)
