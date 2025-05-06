from html.parser import HTMLParser


class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []

    def handle_data(self, data):
        self.result.append(data)

    def get_data(self):
        return "".join(self.result)
    

def strip_html_tags(html):
    stripper = HTMLStripper()
    stripper.feed(html)
    return stripper.get_data()



if __name__ == "__main__":

    html_snippet = """
<div class="html">
<p>
  You're given a list of arbitrary jobs that need to be completed; these jobs
  are represented by distinct integers. You're also given a list of dependencies. A
  dependency is represented as a pair of jobs where the first job is a
  prerequisite of the second one. In other words, the second job depends on the
  first one; it can only be completed once the first job is completed.
</p>
<p>
  Write a function that takes in a list of jobs and a list of dependencies and
  returns a list containing a valid order in which the given jobs can be
  completed. If no such order exists, the function should return an empty array.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">jobs</span> = [1, 2, 3, 4]
<span class="CodeEditor-promptParameter">deps</span> = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
</pre>
<h3>Sample Output</h3>
<pre>[1, 4, 3, 2] or [4, 1, 3, 2]
</pre>
</div>
"""
    plain_text = strip_html_tags(html_snippet)
    print(plain_text)
