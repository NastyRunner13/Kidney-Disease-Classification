import setuptools

__version__ = "0.0.1"

REPO_NAME = "Kidney-Disease-Classification"
AUTHOR_USER_NAME = "NastyRunner13"
SRC_REPO = "KidneyDiseaseClassifier"
AUTHOR_EMAIL = "princegupta1586@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package to classify kidney disease",
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
