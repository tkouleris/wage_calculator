from flask import Flask, render_template, request

app = Flask(__name__)

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
            "team_leader": request.form.get('team_leader')
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
