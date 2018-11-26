def get_html(gif_url, width, height):
    css = get_css()
    response = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>{css}</style>
        <title>A E S T H E T I C S</title>
    </head>
    <body>
        <div class="container">
            <div class="title">
                <div class="title-big">A E S T H E T &nbsp; C S</div>
                <img src="https://media.giphy.com/media/MU5rUkHwnEWppqwExa/giphy.gif" class="thunder" alt="thunder">
            </div>
            <iframe src="{gif_url}" width="{width}" height="{height}" frameBorder="0" class="giphy-embed gif-container" allowFullScreen></iframe>
            <a href="https://github.com/hamitb" class="github-link">
                <img src="https://media.giphy.com/media/fCTqwThlbodeP5s607/giphy.gif" class="what" alt="what">
            </a>
        </div>
    </body>
    </html>
    """
    return response

def get_css():
    return """
    @import url("https://fonts.googleapis.com/css?family=Press+Start+2P");

    html, body {
        width: 100%;
        height: 100%;
        margin: 0;
        background-image: url("https://i.pinimg.com/originals/af/3c/09/af3c090f6a81b6a526e3ce48e018a9c7.png");
        background-size: 200%;
        min-width: 1240px;
    }
    .container {
        width: 100%;
        height: 100%;
        color: white;
        padding: 70px 20px;
        text-align: center; 
    }
    .container .title {
        display: inline-block;
        color: white;
        margin: 15px auto;
        position: relative;
    }
    .container .title .thunder {
        width: 70px;
        margin-left: 40px;
        margin-right: 50px;
        position: absolute;
        bottom: 5px;
        right: 205px;
    }
    .container .github-link .what {
        width: 40px;
        height: 40px;
    }
    .container .gif-container {
        display: block;
        margin: 50px auto;
        border: 30px solid #f000ff;
    }
    .container .title .title-big {
        background: linear-gradient(-45deg, #EE7752, #E73C7E, #23A6D5, #23D5AB);
        background-size: 300% 300%;
	    -webkit-background-clip: text;
	    -webkit-text-fill-color: transparent;
        -webkit-animation: Gradient 10s ease infinite;
        -moz-animation: Gradient 10s ease infinite;
        animation: Gradient 10s ease infinite;
        font-family: 'Press Start 2P', cursive;
        font-size: 65px;
        display: inline-block;
    }

    @-webkit-keyframes Gradient {
        0% {
            background-position: 50% 0%
        }
        50% {
            background-position: 50% 100%
        }
        100% {
            background-position: 50% 0%
        }
    }

    @-moz-keyframes Gradient {
        0% {
            background-position: 50% 0%
        }
        50% {
            background-position: 50% 100%
        }
        100% {
            background-position: 50% 0%
        }
    }

    @keyframes Gradient {
        0% {
            background-position: 0% 50%
        }
        50% {
            background-position: 100% 50%
        }
        100% {
            background-position: 0% 50%
        }
    }
    """