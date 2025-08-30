from django.core.management.base import BaseCommand
from portfolio.models import Profile, Education, Skill, Project

class Command(BaseCommand):
    help = "Seed the database with starter profile, skills, education, and projects."

    def handle(self, *args, **kwargs):
        profile, _ = Profile.objects.get_or_create(
            name="Poorna Chandra Rao",
            defaults=dict(
                tagline="Integrated M.Sc. Mathematics @ NIT Surat | Data Science & Backend Developer",
                email="poornachandra6304@gmail.com",
                phone="+91 6304598599",
                location="Surat, India",
                linkedin="https://www.linkedin.com/in/poorna-chandra-rao-66134b243",
                github="https://github.com/poorna-9",
                about=(
                    "I’m an Integrated M.Sc. Mathematics student at NIT Surat (graduating in 2026). "
                    "I enjoy building ML/DL models from scratch, working on backend systems with Django, "
                    "and solving algorithmic problems."
                )
            )
        )

        Education.objects.get_or_create(
            degree="Integrated M.Sc. Mathematics",
            institution="National Institute of Technology, Surat (NIT Surat)",
            start_year=2021,
            end_year=2026,
            defaults=dict(cgpa="7.5/10", details="Relevant coursework: DSA, Linear Algebra, Probability & Stats, DBMS, Web Frameworks; Stanford CS229 ML.")
        )

        skills = [
            ("Programming Languages", "Python", "Advanced"),
            ("Programming Languages", "JavaScript", "Intermediate"),
            ("Programming Languages", "SQL", "Intermediate"),
            ("Data Science & ML", "Scikit-learn", "Advanced"),
            ("Data Science & ML", "XGBoost", "Intermediate"),
            ("Data Science & ML", "Random Forest", "Advanced"),
            ("Data Science & ML", "Regression/Classification", "Advanced"),
            ("Data Science & ML", "Time Series Analysis", "Intermediate"),
            ("Deep Learning", "TensorFlow", "Advanced"),
            ("Deep Learning", "Keras", "Advanced"),
            ("Deep Learning", "PyTorch (Conceptual)", "Intermediate"),
            ("Deep Learning", "ANN/CNN/RNN/LSTM/Transformers", "Advanced"),
            ("Deep Learning", "Word2Vec, Attention", "Intermediate"),
            ("Web Development", "Django", "Advanced"),
            ("Web Development", "RESTful APIs", "Intermediate"),
            ("Web Development", "MySQL", "Intermediate"),
            ("Tools", "Git & GitHub", "Advanced"),
            ("Tools", "Jupyter Notebooks", "Advanced"),
        ]
        for cat, name, level in skills:
            Skill.objects.get_or_create(category=cat, name=name, defaults=dict(level=level))

        projects = [
            dict(
                title="Deep Learning Models Implemented from Scratch",
                description=(
                    "Implemented ANN, CNN, RNN, LSTM, GNN, and Transformer architectures using only NumPy and Python. "
                    "Built forward/backward propagation, loss functions (Cross-Entropy, MSE), and activations. "
                    "Trained on MNIST, CIFAR-10, and a toy translation dataset."
                ),
                technologies="Python, NumPy",
                github_url="https://github.com/poorna-9",
                demo_url="",
                featured=True,
                order=1
            ),
            dict(
                title="Stock Price Prediction using ML & DL",
                description=(
                    "Predicted stock prices for Google and Tesla using ML/DL. "
                    "Handled missing data, removed outliers, engineered features; "
                    "compared models using RMSE/MAE; LSTM showed 15% improvement over SMA baseline."
                ),
                technologies="Scikit-learn, XGBoost, TensorFlow, Pandas, NumPy",
                github_url="",
                demo_url="",
                featured=False,
                order=2
            ),
            dict(
                title="E-commerce Website (Full-Stack)",
                description=(
                    "Django + MySQL site with authentication, order handling, product management. "
                    "RESTful APIs + JavaScript for dynamic cart updates and improved UX."
                ),
                technologies="Django, MySQL, HTML, CSS, JavaScript",
                github_url="https://github.com/poorna-9/cricscore",
                demo_url="",
                featured=False,
                order=3
            ),
        ]
        for p in projects:
            Project.objects.get_or_create(title=p["title"], defaults=p)

        self.stdout.write(self.style.SUCCESS("Database seeded."))