<h1 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 36px;">0x07. Rotate 2D Matrix</h1>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(219, 62, 62);font-size: 14px;">Algorithm</span></strong><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(219, 62, 62);font-size: 14px;">Python</span></strong></div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <ul style="font-size: 11px;">
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">Weight: 1</li>
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">Project will start <span title=""><span style="border-bottom: 0.5px dashed currentcolor;">Jul 15, 2024 6:00 AM</span></span>, must end by <span title=""><span style="border-bottom: 0.5px dashed currentcolor;">Jul 19, 2024 6:00 AM</span></span></li>
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">Checker was released at <span title=""><span style="border-bottom: 0.5px dashed currentcolor;">Jul 16, 2024 6:00 AM</span></span></li>
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">An auto review will be launched at the deadline</li>
    </ul>
</div>
<div style="text-align: start;color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);font-size: 14px;border: 1px solid rgb(221, 221, 221);">
    <div>
        <p>For the &ldquo;0. Rotate 2D Matrix&rdquo; project, you are tasked with implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python. Below are the key concepts and resources that you need to grasp in order to successfully complete this project.</p>
        <h3 style="color: inherit;font-size: 24px;">Concepts Needed:</h3>
        <ol>
            <li>
                <p><strong><strong>Matrix Representation in Python</strong></strong>:</p>
                <ul>
                    <li>Understanding how 2D matrices are represented using lists of lists in Python.</li>
                    <li>Accessing and modifying elements in a 2D matrix.</li>
                </ul>
            </li>
            <li>
                <p><strong><strong>In-place Operations</strong></strong>:</p>
                <ul>
                    <li>Performing operations on data without creating a copy of the data structure.</li>
                    <li>The importance of minimizing space complexity by modifying the matrix in place.</li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Matrix Transposition</strong></strong>:</p>
                <ul>
                    <li>Understanding the concept of transposing a matrix (swapping rows and columns).</li>
                    <li>Implementing matrix transposition as a step in the rotation process.</li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Reversing Rows in a Matrix</strong></strong>:</p>
                <ul>
                    <li>Manipulating rows of a matrix by reversing their order as part of the rotation process.</li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Nested Loops</strong></strong>:</p>
                <ul>
                    <li>Using nested loops to iterate through 2D data structures like matrices.</li>
                    <li>Modifying elements within nested loops to achieve the desired rotation.</li>
                </ul>
            </li>
        </ol>
        <h3 style="color: inherit;font-size: 24px;">Resources:</h3>
        <ul>
            <li>
                <p><strong><strong>Python Official Documentation</strong></strong>:</p>
                <ul>
                    <li><a href="https://intranet.alxswe.com/rltoken/eZc_ELGxUgkuc4kkE_fd7Q" title="Data Structures (list comprehensions, nested list comprehension)" target="_blank" style="color: transparent;">Data Structures (list comprehensions, nested list comprehension)</a></li>
                    <li><a href="https://intranet.alxswe.com/rltoken/0ORj179giGhGe8jpcxBkXg" title="More on Lists" target="_blank" style="color: transparent;">More on Lists</a></li>
                </ul>
            </li>
            <li>
                <p><strong><strong>GeeksforGeeks Articles</strong></strong>:</p>
                <ul>
                    <li><a href="https://intranet.alxswe.com/rltoken/9T8w4mtiIIRDtfLSmEmrLA" title="Inplace rotate square matrix by 90 degrees" target="_blank" style="color: transparent;">Inplace rotate square matrix by 90 degrees</a></li>
                    <li><a href="https://intranet.alxswe.com/rltoken/JdIFvtej2hMW-Wd9ABHMOA" title="Transpose a matrix in Single line in Python" target="_blank" style="color: transparent;">Transpose a matrix in Single line in Python</a></li>
                </ul>
            </li>
            <li>
                <p><strong><strong>TutorialsPoint</strong></strong>:</p>
                <ul>
                    <li><a href="https://intranet.alxswe.com/rltoken/rFmzUTpaLGqDXjGA6D9eYw" title="Python Lists" target="_blank" style="color: transparent;">Python Lists</a> for basics of list manipulation in Python.</li>
                </ul>
            </li>
        </ul>
        <p>By understanding these concepts and utilizing the provided resources, you will be able to approach the problem methodically, first transposing the matrix and then reversing each row to achieve a 90-degree clockwise rotation. This project not only tests your ability to manipulate 2D matrices but also challenges you to think about optimizing your solution to operate in-place, thus improving their problem-solving and algorithmic thinking skills in Python.</p>
        <h2 style="color: inherit;font-size: 30px;">Additional Resources</h2>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/4GPWA9C2AJHtpdGxuIHEPA" title="Mock Technical Interview" target="_blank" style="color: transparent;">Mock Technical Interview</a></li>
        </ul>
        <h2 style="color: inherit;font-size: 30px;">Requirements</h2>
        <h3 style="color: inherit;font-size: 24px;">General</h3>
        <ul>
            <li>Allowed editors: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">vi</code>, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">vim</code>, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">emacs</code></li>
            <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">python3</code> (version 3.8.10)</li>
            <li>All your files should end with a new line</li>
            <li>The first line of all your files should be exactly <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">#!/usr/bin/python3</code></li>
            <li>A <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>Your code should use the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">pycodestyle</code> style (version 2.8.0)</li>
            <li>You are not allowed to import any module</li>
            <li>All modules and functions must be documented</li>
            <li>All your files must be executable</li>
        </ul>
    </div>
</div>
<h2 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 30px;">Tasks</h2>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">0. Rotate 2D Matrix</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Given an <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">n</code> x <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">n</code> 2D matrix, rotate it 90 degrees clockwise.</p>
            <ul>
                <li>Prototype: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def rotate_2d_matrix(matrix):</code></li>
                <li>Do not return anything. The matrix must be edited <strong><strong>in-place</strong></strong>.</li>
                <li>You can assume the matrix will have 2 dimensions and will not be empty.</li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">jessevhedden$ cat main_0.py
#!/usr/bin/python3
&quot;&quot;&quot;
Test 0x07 - Rotate 2D Matrix
&quot;&quot;&quot;
rotate_2d_matrix = __import__(&apos;0-rotate_2d_matrix&apos;).rotate_2d_matrix

if __name__ == &quot;__main__&quot;:
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$</code></pre>
        </div>
    </div>
</div>