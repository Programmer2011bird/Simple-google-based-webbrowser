from flask import *
from Browser import browser

SERVER: Flask = Flask(__name__)


@SERVER.route("/")
def Home() -> str:
    return render_template("index.html")


@SERVER.route("/search", methods = ["GET", "POST"])
def search():
    SEARCH_TEXT: str = str(request.form.get("searchText"))
    RESULTS: dict[str, str] = browser.search(self= browser, search= SEARCH_TEXT)
    HTML_RESULTS: str = """<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
        integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">"""

    for i in range(len(RESULTS)):
        TITLE: str = str(RESULTS[str(i)]["Title"])
        LINK: str = str(RESULTS[str(i)]["Link"])
        
        HTML: str = f"""
        <body class="bg-dark text-light">
            <div class="container position-relative">
                <h3><a href="{LINK}">{TITLE}</a></h3>
            </div>
        </body>
        """
        
        HTML_RESULTS += HTML


    return HTML_RESULTS


if __name__ == "__main__":
    SERVER.run(debug= True, host="0.0.0.0", port="5000")
