from distutils.core import setup

setup(
    name="autotesttables",
    packages=["autotesttables"],
    version="0.1",
    license="MIT",
    description="AutoTestTables is Python package made to further automate testing, by automatically generating test tables.",  # Give a short description about your library
    author="Ethan",
    author_email="skelmis.craft@gmail.com",  # Type in your E-Mail
    url="https://github.com/user/reponame",  # Provide either the link to your github or to your website
    download_url="https://github.com/user/reponame/archive/v_01.tar.gz",  # I explain this later on
    keywords=[
        "SOME",
        "MEANINGFULL",
        "KEYWORDS",
    ],  # Keywords that define your package best
    install_requires=["xlsxwriter",],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
