<div style="text-align: start;color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);font-size: 14px;border: 1px solid rgb(221, 221, 221);">
    <div>
        <h2 style="color: inherit;font-size: 30px;">Must Know</h2>
        <p>To successfully complete this project, you should revise the following Python concepts:</p>
        <ol>
            <li>
                <p><strong><strong>Lists and List Comprehensions</strong></strong>:</p>
                <ul>
                    <li>Understand how to create, access, modify, and iterate over lists.</li>
                    <li>Utilize list comprehensions for more concise and readable code, especially for generating rows of Pascal&rsquo;s Triangle.</li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Functions</strong></strong>:</p>
                <ul>
                    <li>Know how to define and call functions.</li>
                    <li>Pass parameters and return values, particularly how to return a list of lists representing Pascal&rsquo;s Triangle.</li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Loops</strong></strong>:</p>
                <ul>
                    <li>Use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">for</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">while</code> loops to iterate through sequences.</li>
                    <li>Nested loops may be necessary for generating each row and calculating the values of Pascal&rsquo;s Triangle.</li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Conditional Statements</strong></strong>:</p>
                <ul>
                    <li>Apply <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">if</code>, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">elif</code>, and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">else</code> conditions to implement logic based on the position within Pascal&rsquo;s Triangle (e.g., the edges of the triangle always being 1).</li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Recursion (Optional)</strong></strong>:</p>
                <ul>
                    <li>While not strictly necessary, understanding recursion can provide an alternative approach to generating Pascal&rsquo;s Triangle.</li>
                    <li>Recognize base cases and recursive cases for a function that generates the triangle&rsquo;s rows.</li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Arithmetic Operations</strong></strong>:</p>
                <ul>
                    <li>Perform addition, a fundamental operation for calculating each element of Pascal&rsquo;s Triangle as the sum of the two elements directly above it.</li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Indexing and Slicing</strong></strong>:</p>
                <ul>
                    <li>Access elements and slices of lists, crucial for identifying and summing the correct elements when constructing each row of the triangle.</li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Memory Management</strong></strong>:</p>
                <ul>
                    <li>Be mindful of how lists are stored and copied, especially when creating new rows based on the values of the previous row.</li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Error and Exception Handling (Optional)</strong></strong>:</p>
                <ul>
                    <li>Use try-except blocks as needed to handle potential errors, such as invalid input types or values.</li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Efficiency and Optimization</strong></strong>:</p>
                <ul>
                    <li>Consider the time and space complexity of different approaches to generating Pascal&rsquo;s Triangle.</li>
                    <li>Evaluate and apply optimizations to improve the performance of the solution.</li>
                </ul>
            </li>
        </ol>
        <p>By revisiting these concepts, you will be well-prepared to tackle the challenges of implementing Pascal&rsquo;s Triangle in Python, applying both your mathematical understanding and programming skills to develop an efficient and effective solution.</p>
    </div>
</div>
<h2 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 30px;">Tasks</h2>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">0. Pascal&apos;s Triangle</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Create a function <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def pascal_triangle(n):</code> that returns a list of lists of integers representing the Pascal&rsquo;s triangle of <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">n</code>:</p>
            <ul>
                <li>Returns an empty list if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">n &lt;= 0</code></li>
                <li>You can assume <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">n</code> will be always an integer</li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
&quot;&quot;&quot;
0-main
&quot;&quot;&quot;
pascal_triangle = __import__(&apos;0-pascal_triangle&apos;).pascal_triangle

def print_triangle(triangle):
    &quot;&quot;&quot;
    Print the triangle
    &quot;&quot;&quot;
    for row in triangle:
        print(&quot;[{}]&quot;.format(&quot;,&quot;.join([str(x) for x in row])))


if __name__ == &quot;__main__&quot;:
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ </code></pre>
        </div>
    </div>
</div>