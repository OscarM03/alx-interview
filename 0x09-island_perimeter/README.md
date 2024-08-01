<h1 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 36px;">Island Perimeter</h1>
<article style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div>
        <div>
            <div>
                <div>
                    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
                        <div>
                            <p>For the &ldquo;0. Island Perimeter&rdquo; project, you will need to apply your knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers. Understanding how to navigate and analyze 2D arrays and apply logical operations to determine the conditions for perimeter calculation is crucial for this task.</p>
                            <h3 style="color: inherit;font-size: 24px;">Concepts Needed:</h3>
                            <ol>
                                <li>
                                    <p><strong><strong>2D Arrays (Matrices)</strong></strong>:</p>
                                    <ul>
                                        <li>Accessing and iterating over elements in a 2D array.</li>
                                        <li>Understanding how to navigate through adjacent cells (horizontally and vertically).</li>
                                    </ul>
                                </li>
                                <li>
                                    <p><strong><strong>Conditional Logic</strong></strong>:</p>
                                    <ul>
                                        <li>Applying conditions to determine whether a cell contributes to the perimeter of the island.</li>
                                    </ul>
                                </li>
                                <li>
                                    <p><strong><strong>Counting Techniques</strong></strong>:</p>
                                    <ul>
                                        <li>Developing a method to count the edges that contribute to the island&rsquo;s perimeter.</li>
                                    </ul>
                                </li>
                                <li>
                                    <p><strong><strong>Problem-Solving Strategies</strong></strong>:</p>
                                    <ul>
                                        <li>Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.</li>
                                    </ul>
                                </li>
                                <li>
                                    <p><strong><strong>Python Programming</strong></strong>:</p>
                                    <ul>
                                        <li>Nested loops for iterating over grid cells.</li>
                                        <li>Conditional statements to check the status of adjacent cells.</li>
                                    </ul>
                                </li>
                            </ol>
                            <h3 style="color: inherit;font-size: 24px;">Resources:</h3>
                            <ul>
                                <li>
                                    <p><strong><strong>Python Official Documentation</strong></strong>:</p>
                                    <ul>
                                        <li><a href="https://intranet.alxswe.com/rltoken/8SPalOgoGDWQChVbct0p1g" title="Nested Lists" target="_blank" style="color: transparent;">Nested Lists</a>: Understanding how to work with lists within lists in Python.</li>
                                    </ul>
                                </li>
                                <li>
                                    <p><strong><strong>GeeksforGeeks Articles</strong></strong>:</p>
                                    <ul>
                                        <li><a href="https://intranet.alxswe.com/rltoken/IYcYmeVlCfF-F7Szn1fzfQ" title="Python Multi-dimensional Arrays" target="_blank" style="color: transparent;">Python Multi-dimensional Arrays</a>: A guide to working with 2D arrays in Python effectively.</li>
                                    </ul>
                                </li>
                                <li>
                                    <p><strong><strong>TutorialsPoint</strong></strong>:</p>
                                    <ul>
                                        <li><a href="https://intranet.alxswe.com/rltoken/TZ8UtQaRxN5cFf8c1TB-rw" title="Python Lists" target="_blank" style="color: transparent;">Python Lists</a>: Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.</li>
                                    </ul>
                                </li>
                                <li>
                                    <p><strong><strong>YouTube Tutorials</strong></strong>:</p>
                                    <ul>
                                        <li><a href="https://intranet.alxswe.com/rltoken/H7SwlI_XYDpwYonNYKXQfg" title="Python 2D arrays and lists" target="_blank" style="color: transparent;">Python 2D arrays and lists</a></li>
                                    </ul>
                                </li>
                            </ul>
                            <p>By understanding these concepts and utilizing the provided resources, you will be equipped to approach the problem methodically. You&rsquo;ll need to iterate over the grid, apply logical operations to identify the perimeter of the island, and account for the specific conditions described in the task. This project not only tests your algorithmic thinking but also reinforces your ability to manipulate data structures and apply logical reasoning to solve problems.</p>
                            <h2 style="color: inherit;font-size: 30px;">Additional Resources</h2>
                            <ul>
                                <li><a href="https://intranet.alxswe.com/rltoken/9ZYjQgC9HvOLZiHxmgd89Q" title="Mock Technical Interviews" target="_blank" style="color: transparent;">Mock Technical Interviews</a></li>
                            </ul>
                            <h2 style="color: inherit;font-size: 30px;">Requirements</h2>
                            <h3 style="color: inherit;font-size: 24px;">General</h3>
                            <ul>
                                <li>Allowed editors: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">vi</code>, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">vim</code>, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">emacs</code></li>
                                <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">python3</code> (version 3.4.3)</li>
                                <li>All your files should end with a new line</li>
                                <li>The first line of all your files should be exactly <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">#!/usr/bin/python3</code></li>
                                <li>A <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">README.md</code> file, at the root of the folder of the project, is mandatory</li>
                                <li>Your code should use the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">PEP 8</code> style (version 1.7)</li>
                                <li>You are not allowed to import any module</li>
                                <li>All modules and functions must be documented</li>
                                <li>All your files must be executable</li>
                            </ul>
                        </div>
                    </div>
                    <h2 style="color: inherit;font-size: 30px;">Tasks</h2>
                    <div>
                        <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
                            <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
                                <h3 style="color: rgb(51, 51, 51);font-size: 16px;">0. Island Perimeter</h3>
                                <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
                            </div>
                            <div>
                                <p>Create a function <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def island_perimeter(grid):</code> that returns the perimeter of the island described in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">grid</code>:</p>
                                <ul>
                                    <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">grid</code>is a list of list of integers:<ul>
                                            <li>0 represents water</li>
                                            <li>1 represents land</li>
                                            <li>Each cell is square, with a side length of 1</li>
                                            <li>Cells are connected horizontally/vertically (not diagonally).</li>
                                            <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">grid</code> is rectangular, with its width and height not exceeding 100</li>
                                        </ul>
                                    </li>
                                    <li>The grid is completely surrounded by water</li>
                                    <li>There is only one island (or nothing).</li>
                                    <li>The island doesn&rsquo;t have &ldquo;lakes&rdquo; (water inside that isn&rsquo;t connected to the water surrounding the island).</li>
                                </ul>
                                <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
&quot;&quot;&quot;
0-main
&quot;&quot;&quot;
island_perimeter = __import__(&apos;0-island_perimeter&apos;).island_perimeter

if __name__ == &quot;__main__&quot;:
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

guillaume@ubuntu:~/0x09$ 
guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$ 
</code></pre>
                            </div>
                            <div>
                                <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                                    <p><strong><strong>Repo:</strong></strong></p>
                                    <ul>
                                        <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-interview</code></li>
                                        <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x09-island_perimeter</code></li>
                                        <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0-island_perimeter.py</code></li>
                                    </ul>
                                </div>
                            </div>
                            <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
                                <div>
                                    <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button></div>
                                    <div style="font-size: 1.5rem !important;"><br></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</article>