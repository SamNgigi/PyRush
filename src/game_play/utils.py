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
  Write a function that takes in a non-empty array of integers and returns the
  maximum sum that can be obtained by summing up all of the integers in a
  non-empty subarray of the input array. A subarray must only contain adjacent
  numbers (numbers next to each other in the input array).
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
</pre>
<h3>Sample Output</h3>
<pre>19 <span class="CodeEditor-promptComment">// [1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1]</span>
</pre>
</div>
"""
    plain_text = strip_html_tags(html_snippet)
    print(plain_text)
