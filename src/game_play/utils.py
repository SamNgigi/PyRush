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
  You're given an integer <span>start</span> and a list <span>edges</span> of
  pairs of integers.
</p>
<p>
  The list is what's called an adjacency list, and it represents a graph. The
  number of vertices in the graph is equal to the length of <span>edges</span>,
  where each index <span>i</span> in <span>edges</span> contains vertex
  <span>i</span>'s outbound edges, in no particular order. Each individual edge
  is represented by an pair of two numbers,
  <span>[destination, distance]</span>, where the destination is a positive
  integer denoting the destination vertex and the distance is a positive integer
  representing the length of the edge (the distance from vertex
  <span>i</span> to vertex <span>destination</span>). Note that these edges are
  directed, meaning that you can only travel from a particular vertex to its
  destination—not the other way around (unless the destination vertex itself has
  an outbound edge to the original vertex).
</p>
<p>
  Write a function that computes the lengths of the shortest paths between
  <span>start</span> and all of the other vertices in the graph using Dijkstra's
  algorithm and returns them in an array. Each index <span>i</span> in the
  output array should represent the length of the shortest path between
  <span>start</span> and vertex <span>i</span>. If no path is found from
  <span>start</span> to vertex <span>i</span>, then
  <span>output[i]</span> should be <span>-1</span>.
</p>
<p>
  Note that the graph represented by <span>edges</span> won't contain any
  self-loops (vertices that have an outbound edge to themselves) and will only
  have positively weighted edges (i.e., no negative distances).
</p>
<p>
  If you're unfamiliar with Dijkstra's algorithm, we recommend watching the
  Conceptual Overview section of this question's video explanation before
  starting to code.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">start</span> = 0
<span class="CodeEditor-promptParameter">edges</span> = [
  [[1, 7]],
  [[2, 6], [3, 20], [4, 3]],
  [[3, 14]],
  [[4, 2]],
  [],
  [],
]
</pre>
<h3>Sample Output</h3>
<pre>[0, 7, 13, 27, 10, -1]
</pre>
</div>
"""
    plain_text = strip_html_tags(html_snippet)
    print(plain_text)
