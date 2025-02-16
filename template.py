template = {
    "post": """
f\"\"\"
<!DOCTYPE html>

<html>

<head>
    <meta charset="UTF-8">
    <title>{ARTICLE_NAME} | {conf.config["SITE_NAME"]}</title>
    <link rel="icon" href="/static/favicon.ico">
    <link rel="stylesheet" href="/static/css/default.css">
</head>

<body>
    <h1>{conf.config["SITE_NAME"]}</h1>
    <p>
        {conf.config["TOOL_BAR"]}
    </p>
    <hr>
    <pre>
<b>FROM</b>    {conf.config["AUTHOR_NAME"]}
<b>DATE</b>    {CREATION_TIME}
<b>SUBJECT</b> {ARTICLE_NAME}
{CONTENT}
    </pre>
</body>

</html>
\"\"\"
""",
    "front_page": """
f\"\"\"
<!DOCTYPE html>

<html>

<head>
    <meta charset="UTF-8">
    <title>Front page | {conf.config["SITE_NAME"]}</title>
    <link rel="icon" href="/static/favicon.ico">
    <link rel="stylesheet" href="/static/css/default.css">
</head>

<body>
    <h1>{conf.config["SITE_NAME"]}</h1>
    <p>
        {conf.config["TOOL_BAR"]}
    </p>
    <hr>
    <pre>
{POST_ITEM}
    </pre>
</body>

</html>
\"\"\"
""",
    "post_item": """
f\"\"\"
<b>FROM</b>    {conf.config["AUTHOR_NAME"]}
<b>DATE</b>    {CREATION_TIME}
<b>SUBJECT</b> {ARTICLE_NAME}
<a href="{conf.config["SITE_ADDR"]}/{PATH}">[GO]</a>

\"\"\"
"""
}