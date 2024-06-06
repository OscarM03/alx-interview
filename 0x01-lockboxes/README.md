<div style="text-align: start;color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);font-size: 14px;border: 1px solid rgb(221, 221, 221);">
    <div>
        <h2 style="color: inherit;font-size: 30px;">Must Know</h2>
        <p>For this project, you will need a solid understanding of several key concepts in order to develop a solution that can efficiently determine if all boxes can be opened. Here&rsquo;s a list of concepts and resources that will be instrumental in tackling this project:</p>
        <h3 style="color: inherit;font-size: 24px;">Concepts Needed:</h3>
        <ol>
            <li>
                <p><strong><strong>Lists and List Manipulation</strong></strong>:</p>
                <ul>
                    <li>Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.</li>
                    <li><a href="https://intranet.alxswe.com/rltoken/TtGNy9p1p1d0O5G1rdY1Aw" title="Python Lists (Python Official Documentation)" target="_blank" style="color: transparent;">Python Lists (Python Official Documentation)</a></li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Graph Theory Basics</strong></strong>:</p>
                <ul>
                    <li>Although not explicitly required, knowledge of graph theory (especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful in solving this problem, as the boxes and keys can be thought of as nodes and edges in a graph.</li>
                    <li><a href="https://intranet.alxswe.com/rltoken/eVcYI8g-6nF0Na46xnRdhw" title="Graph Theory (Khan Academy)" target="_blank" style="color: transparent;">Graph Theory (Khan Academy)</a></li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Algorithmic Complexity</strong></strong>:</p>
                <ul>
                    <li>Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms.</li>
                    <li><a href="https://intranet.alxswe.com/rltoken/01qym1qAJUkLrb47PvqnKg" title="Big O Notation (GeeksforGeeks)" target="_blank" style="color: transparent;">Big O Notation (GeeksforGeeks)</a></li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Recursion</strong></strong>:</p>
                <ul>
                    <li>Some solutions might require a recursive approach to traverse through the boxes and keys.</li>
                    <li><a href="https://intranet.alxswe.com/rltoken/zpEuvv0l9EHohIx-HwiAAA" title="Recursion in Python (Real Python)" target="_blank" style="color: transparent;">Recursion in Python (Real Python)</a></li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Queue and Stack</strong></strong>:</p>
                <ul>
                    <li>Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes.</li>
                    <li><a href="https://intranet.alxswe.com/rltoken/CQLm4RJrdwyo2DAcNCtwIA" title="Python Queue and Stack (GeeksforGeeks)" target="_blank" style="color: transparent;">Python Queue and Stack (GeeksforGeeks)</a></li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Set Operations</strong></strong>:</p>
                <ul>
                    <li>Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.</li>
                    <li><a href="https://intranet.alxswe.com/rltoken/zkmtaPqAbKyxx41kRw7ulA" title="Python Sets (Python Official Documentation)" target="_blank" style="color: transparent;">Python Sets (Python Official Documentation)</a></li>
                </ul>
            </li>
        </ol>
        <p>By reviewing these concepts and utilizing these resources, you will be well-equipped to develop an efficient solution for this project, applying both your algorithmic thinking and Python programming skills.</p>
        <h2 style="color: inherit;font-size: 30px;">Additional Resources</h2>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/TJ0FJhWeEGolIqMpwBn7Pg" title="Mock Technical Interview" target="_blank" style="color: transparent;">Mock Technical Interview</a></li>
        </ul>
        <h2 style="color: inherit;font-size: 30px;">Requirements</h2>
        <h3 style="color: inherit;font-size: 24px;">General</h3>
        <ul>
            <li>Allowed editors: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">vi</code>, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">vim</code>, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">emacs</code></li>
            <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">python3</code> (version 3.4.3)</li>
            <li>All your files should end with a new line</li>
            <li>The first line of all your files should be exactly <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">#!/usr/bin/python3</code></li>
            <li>A <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>Your code should be documented</li>
            <li>Your code should use the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">PEP 8</code> style (version 1.7.x)</li>
            <li>All your files must be executable</li>
        </ul>
    </div>
</div>
<h2 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 30px;">Tasks</h2>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">0. Lockboxes</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>You have <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">n</code> number of locked boxes in front of you. Each box is numbered sequentially from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0</code> to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">n - 1</code> and each box may contain keys to the other boxes.</p>
            <p>Write a method that determines if all the boxes can be opened.</p>
            <ul>
                <li>Prototype: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def canUnlockAll(boxes)</code></li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">boxes</code> is a list of lists</li>
                <li>A key with the same number as a box opens that box</li>
                <li>You can assume all keys will be positive integers<ul>
                        <li>There can be keys that do not have boxes</li>
                    </ul>
                </li>
                <li>The first box <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">boxes[0]</code> is unlocked</li>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">True</code> if all boxes can be opened, else return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">False</code></li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__(&apos;0-lockboxes&apos;).canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
</code></pre>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$</code></pre>
        </div>
    </div>
</div>