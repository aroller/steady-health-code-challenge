# Steady Health Code Challenge

This is the code challenge for Steady Health and the objective is to build a wiki web app.

The requirements of the app are the following:

* A page is accessed through the URL pattern /(page_title) and should render the page title and text content.
* Each word in the text content should be linked to a page, if it matches the title of an existing page.
* The home page should list and link all existing pages.

## Example

Given the pages Hypertext, Cunningham and Wiki (see /pages folder), the page for /Wiki should be rendered as:

A <a href="/Wiki">Wiki</a> is a website on which users collaboratively modify <a href="/Hypertext">Hypertext</a>
and structure it directly from the web browser.

Ward <a href="/Cunningham">Cunningham</a>, the developer of the first wiki software,
originally described it as "the simplest online database that could possibly work".

## Additional Hints

* Editing or creating pages is not expected for this challenge.
* Using the flat files in pages as the data source is recommended.
* Page titles can be restricted to CamelCase (no spaces and special characters).
* Case sensitive matching for titles is acceptable, but they should still be linked if followed by punctuation characters. (i.e. "Hypertext, hyperlink" links to /Hypertext, but not to /Hypertext.)

The focus should be on clean, maintainable and secure code.
The choice of programming language, frameworks, tools and libraries is up to you.

Once you’re satisfied with your solution, please push your code to a GitHub repo and let us know.
We'll then continue with a 30 minute call to walkthrough your solution.

If you have any questions, please reach out to jake@steady.health.

We hope you enjoy this challenge and value the time you put into this.

Thank you!

The Steady Team.
