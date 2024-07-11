<div style="text-align: start;color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);font-size: 14px;border: 1px solid rgb(221, 221, 221);">
    <div>
        <p>The &ldquo;0. Star Wars Characters&rdquo; project requires you to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with several key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.</p>
        <h3 style="color: inherit;font-size: 24px;">Concepts Needed:</h3>
        <ol>
            <li>
                <p><strong><strong>HTTP Requests in JavaScript</strong></strong>:</p>
                <ul>
                    <li>Understanding how to make HTTP requests to external services using the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request</code> module or alternatives like <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">fetch</code> in Node.js.</li>
                    <li><a href="https://intranet.alxswe.com/rltoken/iRse23lnV4gAsD9JJTJMMQ" title="A Complete Guide to Making HTTP Requests in Node.js" target="_blank" style="color: transparent;">A Complete Guide to Making HTTP Requests in Node.js</a></li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Working with APIs</strong></strong>:</p>
                <ul>
                    <li>Understanding the basics of RESTful APIs and how to interact with them.</li>
                    <li>Parsing JSON data returned by APIs.</li>
                    <li><a href="https://intranet.alxswe.com/rltoken/KyGS_uB68mLaP5irrH8JVA" title="Working with APIs in JavaScript" target="_blank" style="color: transparent;">Working with APIs in JavaScript</a></li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Asynchronous Programming</strong></strong>:</p>
                <ul>
                    <li>Managing asynchronous operations with callbacks, promises, and async/await syntax.</li>
                    <li>Handling API response data asynchronously.</li>
                    <li><a href="https://intranet.alxswe.com/rltoken/tdKMGJrRstCkXSReNfRFpQ" title="Asynchronous Programming in JavaScript" target="_blank" style="color: transparent;">Asynchronous Programming in JavaScript</a></li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Command Line Arguments in Node.js</strong></strong>:</p>
                <ul>
                    <li>Using the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">process.argv</code> array to access command-line arguments passed to a Node.js script.</li>
                    <li><a href="https://intranet.alxswe.com/rltoken/oWBOWJZLF_D9GfOydPz6Kg" title="How to Parse Command Line Arguments in Node.js" target="_blank" style="color: transparent;">How to Parse Command Line Arguments in Node.js</a></li>
                </ul>
            </li>
            <li>
                <p><strong><strong>Array Manipulation and Iteration</strong></strong>:</p>
                <ul>
                    <li>Iterating over arrays and manipulating data structures to format and display character names.</li>
                    <li><a href="https://intranet.alxswe.com/rltoken/8zdG036OYYvVco_AZTExoA" title="JavaScript Array Methods" target="_blank" style="color: transparent;">JavaScript Array Methods</a></li>
                </ul>
            </li>
        </ol>
        <p>By familiarizing yourself with these concepts and resources, you will be able to efficiently retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API, demonstrating your ability to work with external APIs and manage asynchronous code in JavaScript.</p>
        <h2 style="color: inherit;font-size: 30px;">Additional Resources</h2>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/du6hlPQm6qi4A7eEursNhQ" title="Mock Technical Interview" target="_blank" style="color: transparent;">Mock Technical Interview</a></li>
        </ul>
        <h2 style="color: inherit;font-size: 30px;">Requirements</h2>
        <h3 style="color: inherit;font-size: 24px;">General</h3>
        <ul>
            <li>Allowed editors: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">vi</code>, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">vim</code>, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">emacs</code></li>
            <li>All your files will be interpreted on Ubuntu 20.04 LTS using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">node</code> (version 10.14.x)</li>
            <li>All your files should end with a new line</li>
            <li>The first line of all your files should be exactly <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">#!/usr/bin/node</code></li>
            <li>A <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>Your code should be <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">semistandard</code> compliant. <a href="https://intranet.alxswe.com/rltoken/9P3gH5mVdJCEKL87E-IMaA" title="Rules of Standard" target="_blank" style="color: transparent;">Rules of Standard</a> + <a href="https://intranet.alxswe.com/rltoken/WjMvQfBMKBdsNUuHyg55Dw" title="semicolons on top" target="_blank" style="color: transparent;">semicolons on top</a>. Also as reference: <a href="https://intranet.alxswe.com/rltoken/Xp81RT-Sfi7uE_kNCSXunw" title="AirBnB style" target="_blank" style="color: transparent;">AirBnB style</a></li>
            <li>All your files must be executable</li>
            <li>The length of your files will be tested using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">wc</code></li>
            <li>You are not allowed to use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">var</code></li>
        </ul>
        <h2 style="color: inherit;font-size: 30px;">More Info</h2>
        <h3 style="color: inherit;font-size: 24px;">Install Node 10</h3>
        <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code></pre>
        <h3 style="color: inherit;font-size: 24px;">Install semi-standard</h3>
        <p><a href="https://intranet.alxswe.com/rltoken/WjMvQfBMKBdsNUuHyg55Dw" title="Documentation" target="_blank" style="color: transparent;">Documentation</a></p>
        <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">$ sudo npm install semistandard --global
</code></pre>
        <h3 style="color: inherit;font-size: 24px;">Install <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 21.6px;">request</code> module and use it</h3>
        <p><a href="https://intranet.alxswe.com/rltoken/BWz2gc45S-nZaxEY6GA6Zw" title="Documentation" target="_blank" style="color: transparent;">Documentation</a></p>
        <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
</code></pre>
    </div>
</div>
<h2 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 30px;">Tasks</h2>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">0. Star Wars Characters</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Write a script that prints all characters of a Star Wars movie:</p>
            <ul>
                <li>The first positional argument passed is the Movie ID - example: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">3</code> = &ldquo;Return of the Jedi&rdquo;</li>
                <li>Display one character name per line <strong><strong>in the same order as the &ldquo;characters&rdquo; list in the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">/films/</code> endpoint</strong></strong></li>
                <li>You must use the <a href="https://intranet.alxswe.com/rltoken/gh_NaSUk9QlXHVoACFU-tg" title="Star wars API" target="_blank" style="color: transparent;">Star wars API</a></li>
                <li>You must use the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request</code> module</li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$ </code></pre>
        </div>
    </div>
</div>