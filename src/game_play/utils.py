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
<p>Implement a <span>MinHeap</span> class that supports:</p>
<ul>
  <li>Building a Min Heap from an input array of integers.</li>
  <li>Inserting integers in the heap.</li>
  <li>Removing the heap's minimum / root value.</li>
  <li>Peeking at the heap's minimum / root value.</li>
  <li>
    Sifting integers up and down the heap, which is to be used when inserting
    and removing values.
  </li>
</ul>
<p>Note that the heap should be represented in the form of an array.</p>
<p>
  If you're unfamiliar with Min Heaps, we recommend watching the
  Conceptual Overview section of this question's video explanation before
  starting to code.
</p>
<h3>Sample Usage</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

<span class="CodeEditor-promptComment">// All operations below are performed sequentially.</span>
<span class="CodeEditor-promptParameter">MinHeap</span>(array): - <span class="CodeEditor-promptComment">// instantiate a MinHeap (calls the buildHeap method and populates the heap)</span>
<span class="CodeEditor-promptParameter">buildHeap</span>(array): - <span class="CodeEditor-promptComment">[-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]</span>
<span class="CodeEditor-promptParameter">insert</span>(76): - <span class="CodeEditor-promptComment">[-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]</span>
<span class="CodeEditor-promptParameter">peek</span>(): -5
<span class="CodeEditor-promptParameter">remove</span>(): -5 <span class="CodeEditor-promptComment">[2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]</span>
<span class="CodeEditor-promptParameter">peek</span>(): 2
<span class="CodeEditor-promptParameter">remove</span>(): 2 <span class="CodeEditor-promptComment">[6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48]</span>
<span class="CodeEditor-promptParameter">peek</span>(): 6
<span class="CodeEditor-promptParameter">insert</span>(87): - <span class="CodeEditor-promptComment">[6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]</span>
</pre>
</div>
"""
    plain_text = strip_html_tags(html_snippet)
    print(plain_text)
