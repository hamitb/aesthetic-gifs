def get_html(gif_url, width, height):
    css = get_css()
    response = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>{css}</style>
        <title>title</title>
    </head>
    <body>
        <div class="container">
            <div class="title">
                <div class="title-big">A E S T H E T</div>
                <img src="https://media.giphy.com/media/MU5rUkHwnEWppqwExa/giphy.gif" class="thunder" alt="thunder">
                <div class="title-big">C S</div>
            </div>
            <iframe src="{gif_url}" width="{width}" height="{height}" frameBorder="0" class="giphy-embed gif-container" allowFullScreen></iframe>
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
        min-width: 1210px;
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
    }
    .container .title .thunder {
        width: 70px;
        margin-left: 40px;
        margin-right: 50px;
    }
    .container .gif-container {
        display: block;
        margin: 50px auto;
        border: 30px solid white;
    }
    .container .title .title-big     {
        font-family: 'Press Start 2P', cursive;
        font-size: 65px;
        display: inline-block;
    }
    """