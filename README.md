Docker commands:

1) BUILD IMAGE : docker build -t colors_api .
2) RUN IMAGE: docker run -t -p 5000:5000 colors_api

Build from source:

1) Create virtual enviroment:
python -m venv colors_api
2) Activate it
colors_api/Scripts/activate
3) Clone the repo and move the files inside the virtual env folder colors_api
git clone https://github.com/Agustyn98/Colors-Api.git
4) Run the app
python /src/router.py