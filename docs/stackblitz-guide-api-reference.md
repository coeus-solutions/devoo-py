Introduction
WebContainers are a browser-based runtime for executing Node.js applications and operating system commands, entirely inside your browser tab. Apps that previously required cloud VMs to execute user code, in WebContainers can run entirely client-side with a number of benefits over the legacy cloud VM.

WebContainer API is perfect for interactive coding experiences. Among its most common use cases are AI applications, adding in-browser code execution to your existing product, programming tutorials, next-generation documentation, browser based IDEs, and employee onboarding platforms. WebContainers have been battle-tested by millions of users of StackBlitz, and inside the interactive learning environments built by the Svelte, Angular, and Nuxt teams among others.

Ready to try it out for yourself?

Check out this WebContainer API starter or see our Quickstart guide to get familiar with what's possible!

Key features
Native Node.js inside the browser running Node.js toolchains (for example, Webpack, Vite, and others)
Flexible: build next-generation coding experiences powered by WebContainers
Unmatched security: everything is contained in a browser tab
Fast: spinning up the entire dev environment in milliseconds
Always free for Open Source: you're the future of the web and we love you 💙
WebContainers versus cloud VM approach
WebContainers enables you to build applications that previously required running VMs in the cloud to execute user code. Instead, WebContainers run entirely client-side, providing a number of benefits over the legacy cloud VM approach:

Unmatched user experience. No latency. Faster than localhost. Works offline.
Cost effective. Compute is done locally. No paying by the minute for cloud VMs.
Scales to millions. Leverages modern CDN caching and client-side compute.
No risk of bad actors. Say goodbyte to bitcoin miners, malware, and phishing sites.
If you want to skip the Quickstart guide and jump stright into exploring the API, you can open the WebContainer starter project in StackBlitz here:

Open in StackBlitz

Who's using WebContainers?
Initially announced at Google I/O, WebContainers are developed by StackBlitz and have been battle-tested by millions of developers every month as they power the StackBlitz editor. Externally, WebContainers also power a number of popular interactive learning environments including those built by the Svelte, Angular, and Nuxt teams.

To see more examples of how WebContainers have been used so far, check out our Community Projects page.

Get started
To get started:

check out our WebContainer starter
follow our step-by-step tutorial and build your first WebContainer app
reading the API reference
get inspired by our Community projects
Community
Wanna ask a question, get some inspiration, or help us amplify your project? Join our Discord community!

---

Setup instructions for local development
Prerequisites
Before you proceed, make sure to have the following installed:

Node v14 or higher
npm (or pnpm or yarn)
Initialize a new Vite app with the vanilla JavaScript template:
If you're using the StackBlitz editor, you can skip this step.

In the terminal, run the following command to initialize a new Vite app:

bash
npm create vite webcontainers-express-app --template vanilla
You'll see a new directory called webcontainers-express-app with a Vite app. Enter that directory, install the dependencies, and run the dev server:

bash
cd webcontainers-express-app
npm install
npm run dev
When the dev server starts, you will see a localhost URL in the terminal - click on the link to see the preview page. You should see the following screen:

A Vite boilerplate welcome page featuring the logos of Vite and JS, a sign "Hello Vite!" and a counter

If you're already curious about the outcome of the tutorial, check out this demo 👀

1. Prepare the files in the Vite app
In your Vite app, there are only two files that you will need: index.html and main.js. Replace the contents of main.js with the following code:


main.js
js
import './style.css';

document.querySelector('#app').innerHTML = ``;
You can now remove counter.js as you won't need it anymore. Now your app looks very minimalistic:

A browser window with empty page and a tab featuring the title "My first WebContainers app" and StackBlitz logo

You might have noticed that we have also changed the name and the logo on the browser tab. You can do so in index.html.

2. Create and style a textarea and an iframe
Now let's set up HTML and styles for your app. You'll need to build two areas: a textarea in which the code will be featured, and an iframe to show the rendered output.

First, let's create a file called loading.html the entire contents of which are as follows:


loading.html
js
Installing dependencies...
We will add this file to an iframe that will be visible in the preview only when the WebContainer is getting ready. After that, it will be replaced with the WebContainer output.

Now, let's build a scaffolding by adding HTML to the #app element in main.js:


main.js
js
document.querySelector('#app').innerHTML = `
  <div class="container">
    <div class="editor">
      <textarea>I am a textarea</textarea>
    </div>
    <div class="preview">
      <iframe src="loading.html"></iframe>
    </div>
  </div>
`
Our page now features two boxes:

A page with two rectanglular boxes: a small one on top of a bigger one. The top one reads "I'm a textarea". The bottom one reads "Installing dependencies..."

Let's make it look nicer now. Replace the contents of style.css with the following code:


style.css
css
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  height: 100vh;
}

.container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  height: 100%;
  width: 100%;
}

textarea {
  width: 100%;
  height: 100%;
  resize: none;
  border-radius: 0.5rem;
  background: black;
  color: white;
  padding: 0.5rem 1rem;
}

iframe {
  height: 100%;
  width: 100%;
  border-radius: 0.5rem;
}
You should see something like this:

A page with two rectangles next to each other. The left one reads "I'm a textarea"

3. Setting references for elements
Before you add WebContainers, you need to enable access to the textarea and iframe elements. At the bottom of the main.js file, add this code that will locate the two elements:


main.js
js
/** @type {HTMLIFrameElement | null} */
const iframeEl = document.querySelector('iframe');

/** @type {HTMLTextAreaElement | null} */
const textareaEl = document.querySelector('textarea');
Next step
The scaffolding for the app is ready 👏 In the next step, you'll set up your WebContainer app.


---

Setting up WebContainers
Now that the scaffolding for your app is done, you'll make the dev server capable of running WebContainers and then, you'll boot up the WebContainers with your files.

1. Set up COOP/COEP headers
As stated in Quickstart, WebContainers can only run with the following headers set on the document:

yaml
Cross-Origin-Embedder-Policy: require-corp
Cross-Origin-Opener-Policy: same-origin
Let's get these set. Open your vite.config.js file (or create it in your app's root directory if it doesn't exist) and add the following code:


vite.config.js
js
import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    headers: {
      'Cross-Origin-Embedder-Policy': 'require-corp',
      'Cross-Origin-Opener-Policy': 'same-origin',
    },
  },
});
We need to restart the Vite app now. To do so, in your terminal stop the dev server (ctrl+c). Then, start it again by running npm run dev. Next, hard reload the page in the browser (cmd+shift+r on Mac and ctrl+shift+r on Windows and Linux). The headers are now enabled.

2. Install WebContainer API package
To add the WebContainer API to your app, install their npm package by running the following code in the terminal (in your app's root directory):

bash
npm i @webcontainer/api
3. Boot up a WebContainer instance
Add the following code to the main.js file after the first import statement:

js
import { WebContainer } from '@webcontainer/api';

/** @type {import('@webcontainer/api').WebContainer}  */
let webcontainerInstance;

window.addEventListener('load', async () => {
  // Call only once
  webcontainerInstance = await WebContainer.boot();
});
Congrats - your first WebContainer app is already running in the background 👏

3. Create the files
Let's now add an Express app to the WebContainer. It is going to have two files: index.js and package.json. The output of this app will be visible in the Preview window on the right.

For your reference, their contents are as follows (no need to copy):


index.js
js
import express from 'express';

const app = express();
const port = 3111;

app.get('/', (req, res) => {
  res.send('Welcome to a WebContainers app! 🥳');
});

app.listen(port, () => {
  console.log(`App is live at http://localhost:${port}`);
});
And, package.json:


package.json
json
{
  "name": "example-app",
  "type": "module",
  "dependencies": {
    "express": "latest",
    "nodemon": "latest"
  },
  "scripts": {
    "start": "nodemon --watch './' index.js"
  }
}
So, how to get these files inside the WebContainer?

First, in your app's root directory create a new file called files.js where you will store the object containing these files. Later on, you will then pass this object to a method called mount.

While you can keep them in main.js we suggest having a separate file in this tutorial for code clarity.


files.js
js
/** @satisfies {import('@webcontainer/api').FileSystemTree} */

export const files = {
  'index.js': {
    file: {
      contents: `
import express from 'express';
const app = express();
const port = 3111;

app.get('/', (req, res) => {
  res.send('Welcome to a WebContainers app! 🥳');
});

app.listen(port, () => {
  console.log(\`App is live at http://localhost:\${port}\`);
});`,
    },
  },
  'package.json': {
    file: {
      contents: `
{
  "name": "example-app",
  "type": "module",
  "dependencies": {
    "express": "latest",
    "nodemon": "latest"
  },
  "scripts": {
    "start": "nodemon --watch './' index.js"
  }
}`,
    },
  },
};
As you can see, we have a files object, which contains the files we want to load into the WebContainer.

TIP

If you struggle with the structure of this object, please visit the section on the mental model of the file system.

Last but not least, add another import statement to main.js:


main.js
js
import { files } from './files';
4. Load the files
Now, let's load these files into the WebContainer. Take a look at the highlighted line in the snippet below:


main.js
js
import './style.css';
import { WebContainer } from '@webcontainer/api';
import { files } from './files';

/** @type {import('@webcontainer/api').WebContainer}  */
let webcontainerInstance;

window.addEventListener('load', async () => {
  // Call only once
  webcontainerInstance = await WebContainer.boot();
  await webcontainerInstance.mount(files);
});
To confirm that it worked, let's read the contents of package.json from WebContainer by using the fs.readFile method provided by webcontainerInstance and log it into the console:

js
window.addEventListener('load', async () => {
  // Call only once
  webcontainerInstance = await WebContainer.boot();
  await webcontainerInstance.mount(files);

  const packageJSON = await webcontainerInstance.fs.readFile('package.json', 'utf-8');
  console.log(packageJSON);
});
Now, open the console of your dev tools and see the output:

The open dev tools console logs the contents of the package.json

You can now delete the last two lines.

Learn more: WebContainers behavior

At this point, you may notice that WebContainers send requests to staticblitz.com. This is our domain to host/serve our static assets and package manager-related requests. In some cases, you may see a few calls to this domain - for example when you're installing dependencies and don't have a lockfile, which will require a full dependency resolution and multiple calls to the npm registry.

5. Set textarea's value
Now that you have a file system, you can print the contents of a file in the textarea, for example, the index.js file:

js
window.addEventListener('load', async () => {
  textareaEl.value = files['index.js'].file.contents;
  
  // Call only once
  webcontainerInstance = await WebContainer.boot();
  await webcontainerInstance.mount(files);
});
Now you should see the contents of the file rendered in the textarea box:

The textarea now features the contents of the file

Next step
Your first WebContainer app is ready and running 🔥 In the next step, you'll install the dependencies.

--

Installing dependencies in WebContainers
You can run various commands inside WebContainers like, for example, npm install as follows:

js
webcontainerInstance.spawn('npm', ['install']);
This code runs npm with the install argument inside the WebContainer instance.

Tip

You can also use pnpm or yarn instead of npm. To do so, replace npm in the above code with your package manager of choice.

Syntax
Before we begin, let's take a look at the syntax: we break down commands into their constituent parts, and then pass them to the run method. In this way:

bash
cd hello-world
becomes:

js
webcontainerInstance.spawn('cd', ['hello-world']);
And if you have a command with two arguments, both arguments will be added to the array, like so:

bash
ls src -l
becomes:

js
webcontainerInstance.spawn('ls', ['src', '-l']);
1. Install dependencies
In the main.js file, add an installDependencies function:


main.js
js
async function installDependencies() {
  // Install dependencies
  const installProcess = await webcontainerInstance.spawn('npm', ['install']);
  // Wait for install command to exit
  return installProcess.exit;
}
This function will install the dependencies and return the exit code. If it's 0, it means the command exited successfully.

2. Call the function
Next, call installDependencies() inside the event listener you wrote earlier and you can add error handling:

js
window.addEventListener('load', async () => {
  textareaEl.value = files['index.js'].file.contents;
  // Call only once
  webcontainerInstance = await WebContainer.boot();
  await webcontainerInstance.mount(files);

  const exitCode = await installDependencies();
  if (exitCode !== 0) {
    throw new Error('Installation failed');
  };
});
Note that it is possible to read the output of this command.

js
  const installProcess = await webcontainerInstance.spawn('npm', ['install']);
  
  installProcess.output.pipeTo(new WritableStream({
    write(data) {
      console.log(data);
    }
  }));
The output property is capable of streaming the output.

This means that, for example, by running npm install, you will get every single line from npm installing the code:

Output of npm install logged in the dev tools console

Want to learn more about WritableStream?

For more information on the Writable Stream, check the Deep Dive on the "Running Processes" page.

Next step
Your WebContainer app is now installing dependencies ✨ In the next step, you'll run the dev server.

--

Running dev server in WebContainers
Now that your app is able to install dependencies, you can run the dev server. Let's add some code that will:

run npm run dev,
listen to server-ready event,
and then assign URL to the iframe.
WebContainers expose the server-ready event, which is emitted when the server is ready to accept requests. You can listen to this event using webcontainerInstance.on.

Let's add this code to the main.js file


main.js
js
async function startDevServer() {
  // Run `npm run start` to start the Express app
  await webcontainerInstance.spawn('npm', ['run', 'start']);

  // Wait for `server-ready` event
  webcontainerInstance.on('server-ready', (port, url) => {
    iframeEl.src = url;
  });
}
In your browser dev tools, after you run startDevServer() in the next step, you will be able to see the dev server running:

Browser console shows dependency installation output and reads: "App is live at http://localhost:3111"

Remember the iframeEl you defined at the beginning of this tutorial? Now is the time for it to shine! You are setting the iframeEl's src to the URL of the Express app, which will print its output in the iframe.

Let's call the function in the event listener:


main.js
js
window.addEventListener('load', async () => {
  textareaEl.value = files['index.js'].file.contents;
  // Call only once
  webcontainerInstance = await WebContainer.boot();
  await webcontainerInstance.mount(files);

  const exitCode = await installDependencies();
  if (exitCode !== 0) {
    throw new Error('Installation failed');
  };

  startDevServer();
});
Your Express app is running inside WebContainers!

Now the right box, so far empty, features the output of the Express server: "Welcome to a WebContainers app! 🥳"

Next step
Congratulations! You have an Express app running in your browser with WebContainers 🥳 In the next step, you'll edit the files.

---

Editing a file and updating the iframe in WebContainers
Your Express app is up and running in WebContainers, but if you edit the textarea, the changes are not reflected in the Preview window at all. Let's change that.

1. Create a function to write a file
To change the contents of a file, you will use the fs.writeFile method.

In this case, you're editing only index.js so the function will be quite concise.

js
/** @param {string} content*/

async function writeIndexJS(content) {
  await webcontainerInstance.fs.writeFile('/index.js', content);
};
2. Listen to textarea changes
Now that you have a function to write the file, you can listen to textarea value change and call this function. To do so, attach the input event listener to the textareaEl:

js
window.addEventListener('load', async () => {
  textareaEl.value = files['index.js'].file.contents;

  textareaEl.addEventListener('input', (e) => {
    writeIndexJS(e.currentTarget.value);
  });
});
Try changing the emoji now.

An app with a textarea showing express js index.js code on left, and its output on right side using an iframe

And voilà! We have a working editor with the Preview. You've built your own environment!

Next steps
Your application is now entirely up and running. However, it would be nice if you could see the output of all the commands inside your application instead of inside the DevTools console. In the next step, you'll attach a terminal to the WebContainer processes to show the output.

--

Connect a terminal
Your Express app is up and running and the preview window updates automatically when the textarea changes. However, opening the DevTools to see the WebContainers output is not the most productive. In this step, you'll add a terminal which shows the output.

1. Install Xterm.js
The terminal frontend component that we will use is Xterm.js. It's the same terminal that is used by Visual Studio Code and many other web-based IDEs. To install it, run the following command in your development terminal:

bash
npm install @xterm/xterm
2. Build terminal scaffolding
Your application terminal will be rendered in a new HTML element. Find the querySelector(#app) portion of the code in the main.js file and add a new div, like in the example below:


main.js
js
document.querySelector('#app').innerHTML = `
  <div class="container">
    <div class="editor">
      <textarea>I am a textarea</textarea>
    </div>
    <div class="preview">
      <iframe src="loading.html"></iframe>
    </div>
  </div>
  <div class="terminal"></div>
`;
This div will serve as a parent element for the terminal. Right now, you can't see any changes in your app yet but if you inspect the element in the browser DevTools, you will see it's there:

An app with the browser DevTools open featuring the terminal element

3. Set a reference
Let's add a way to reference the terminal div in the same way as earlier you referenced the textarea and iframe. Add the following line at the bottom of the main.js file:


main.js
js
/** @type {HTMLTextAreaElement | null} */
const terminalEl = document.querySelector('.terminal');
4. Create a terminal instance
Now that the referencable div is in place, you'll create a Terminal instance and render it.

First of all, import Xterm.js. To do so, add an import statement at the top of the main.js file:


main.js
js
import { Terminal } from '@xterm/xterm'
Next, create a new Terminal and attach it to terminalEl:


main.js
js
window.addEventListener('load', async () => {
  textareaEl.value = files['index.js'].file.contents;
  textareaEl.addEventListener('input', (e) => {
    writeIndexJS(e.currentTarget.value);
  });

  const terminal = new Terminal({
    convertEol: true,
  });
  terminal.open(terminalEl);

  // Call only once
  webcontainerInstance = await WebContainer.boot();
  await webcontainerInstance.mount(files);

  const exitCode = await installDependencies();
  if (exitCode !== 0) {
    throw new Error('Installation failed');
  };

  startDevServer();
});
The reason convertEol is set to true is to force the cursor to always start at the beginning of the next line. At this point, your terminal looks as follows:

An app with a black rectangle at the bottom

5. Style the terminal
The terminal looks a bit plain now. Fortunately, Xterm.js ships its own CSS styles and can be imported at the top of the main.js file.


main.js
js
import '@xterm/xterm/css/xterm.css';
As you see, now the terminal takes up 100% of the space of the parent div. Moreover, other styles have been shipped as well, which you'll use in a bit.

The black rectangle at the bottom now has the cursor and takes the whole div width

6. Send output to the terminal
Now that the terminal is set up, you can start redirecting the output of the WebContainer processes to it instead of to the browser DevTools.

To do that, get a hold of the Terminal instance inside the installDependencies and startDevServer methods. You can do this by saving it to a variable (terminal in the example below) and then passing it as an argument to those methods.


main.js
js
window.addEventListener('load', async () => {
  textareaEl.value = files['index.js'].file.contents;
  textareaEl.addEventListener('input', (e) => {
    writeIndexJS(e.currentTarget.value);
  });

  const terminal = new Terminal({
    convertEol: true,
  });
  terminal.open(terminalEl);

  // Call only once
  webcontainerInstance = await WebContainer.boot();
  await webcontainerInstance.mount(files);

  const exitCode = await installDependencies(terminal);
  if (exitCode !== 0) {
    throw new Error('Installation failed');
  };

  startDevServer(terminal);
});
Next, let's print the data to the terminal by refering to the terminal instance:


main.js
js
/**
 * @param {Terminal} terminal
 */
async function installDependencies(terminal) {
  // Install dependencies
  const installProcess = await webcontainerInstance.spawn('npm', ['install']);
  installProcess.output.pipeTo(new WritableStream({
    write(data) {
      terminal.write(data);
    }
  }))
  // Wait for install command to exit
  return installProcess.exit;
}
Refresh the page and you should see that the output of npm install is now shown in the terminal you have just created!

The terminal features the output of the npm install command

Let's make identical changes for the startDevServer method to also show the output of the npm run start command:


main.js
js
/**
 * @param {Terminal} terminal
 */
async function startDevServer(terminal) {
  // Run `npm run start` to start the Express app
  const serverProcess = await webcontainerInstance.spawn('npm', [
    'run',
    'start',
  ]);
  serverProcess.output.pipeTo(
    new WritableStream({
      write(data) {
        terminal.write(data);
      },
    })
  );

  // Wait for `server-ready` event
  webcontainerInstance.on('server-ready', (port, url) => {
    iframeEl.src = url;
  });
}
With these changes, you can see the output from both commands: npm install and npm run start.

The terminal features the output of the npm install and npm run start command

Try changing the code in the textarea - you will see that the dev server restarts because of these changes.

The changed code logs a message "it's alive" and a zombie emoji

Next step
The output is now visible in a terminal in your web application. This step improves User Experience - your users no longer have to open the DevTools console to see what's going on 🥳.

The terminal is currently only capable of showing the output. In the next step, you'll make it interactive, which will allow you to run your own commands from within your application!

---

Add interactivity
The terminal in your application prints logs with proper formatting. It doesn't, however, accept user input just yet. It would be nice if you could convert this experience to a real terminal which would allow you to install other packages or run different commands... Let's get started!

1. Remove code
Isn't it the best feeling when as a developer you get to remove code which isn't necessary anymore? In this step, you can remove both the installDependencies and startDevServer methods! You won't need them anymore as now it's your user who will type and run the commands.

The only thing that you'd need to keep is the listener for the server-ready event, which now will look as following:


main.js
js
window.addEventListener('load', async () => {
  textareaEl.value = files['index.js'].file.contents;
  textareaEl.addEventListener('input', (e) => {
    writeIndexJS(e.currentTarget.value);
  });

  const terminal = new Terminal({
    convertEol: true,
  });
  terminal.open(terminalEl);

  // Call only once
  webcontainerInstance = await WebContainer.boot();
  await webcontainerInstance.mount(files);

  // Wait for `server-ready` event
  webcontainerInstance.on('server-ready', (port, url) => {
    iframeEl.src = url;
  });
});
Open the loading.html file and change the message there as well:

html
Use the terminal to run a command!
The preview window now features the message "Use the terminal to run a command!"

2. Start the shell
To make the terminal a bit more usuable, we could spawn jsh, a custom shell that comes out of the box with WebContainer API.

Using jsh serves as an alternative to spawning commands separately. Create a new function called startShell which will write the output stream of the process to the Xterm.js terminal instance:


main.js
js
/**
 * @param {Terminal} terminal
 */
async function startShell(terminal) {
  const shellProcess = await webcontainerInstance.spawn('jsh');
  shellProcess.output.pipeTo(
    new WritableStream({
      write(data) {
        terminal.write(data);
      },
    })
  );
  return shellProcess;
};
Now, start the shell by calling the startShell function at the end of the event listener:

js
window.addEventListener('load', async () => {
  textareaEl.value = files['index.js'].file.contents;
  textareaEl.addEventListener('input', (e) => {
    writeIndexJS(e.currentTarget.value);
  });

  const terminal = new Terminal({
    convertEol: true,
  });
  terminal.open(terminalEl);

  // Call only once
  webcontainerInstance = await WebContainer.boot();
  await webcontainerInstance.mount(files);

  // Wait for `server-ready` event
  webcontainerInstance.on('server-ready', (port, url) => {
    iframeEl.src = url;
  });

  startShell(terminal);
});
The terminal window now shows the typical terminal prompt

3. Add interactivity to the terminal
It's still not possible to actually do anything inside the terminal. If you try typing there, nothing will print as it only renders the output and still doesn't yet accept the input. Let's change that!

Just like the output property of the WebContainer process is a ReadableStream, the input property of the process is a WritableStream. By writing data to the writable input stream, that data is sent to the WebContainer process.

Let's change the startShell function to accommodate that:


main.js
js
async function startShell(terminal) {
  const shellProcess = await webcontainerInstance.spawn('jsh');
  shellProcess.output.pipeTo(
    new WritableStream({
      write(data) {
        terminal.write(data);
      },
    })
  );

  const input = shellProcess.input.getWriter();
  terminal.onData((data) => {
    input.write(data);
  });

  return shellProcess;
};
Deep dive: What happened in this function?
With this change, you hooked up your terminal to the shell running in the WebContainer process. This means that now you can also send input to the process and run commands. You can now manually run npm install && npm run start or run any other command. Try it yourself!

The commands typed in the terminal

4. Add @xterm/addon-fit
You might've noticed that resizing the window doesn't redraw the terminal output. If you make the window very narrow, lines that are too long don't wrap to the next line, which is not a good UX practice. For example, look at the highlightened line:

The browser window is very narrow now and the terminal features a line that either disappears or when highlightened sticks out

To fix this, you'll need to make the WebContainer process aware of the size of the terminal.

First of all, let's make sure that the terminal itself gets adjusted properly when resizing the window. To do that, you can use the @xterm/addon-fit plugin for Xterm.js which adjusts the terminal columns and rows depending on the element it's rendered in.

First, install the plugin:

bash
npm install @xterm/addon-fit
And import it at the top of your main.js file.


main.js
js
import { FitAddon } from '@xterm/addon-fit';
Next, create a new FitAddon instance and load it into the terminal.


main.js
js
window.addEventListener('load', async () => {
  textareaEl.value = files['index.js'].file.contents;
  textareaEl.addEventListener('input', (e) => {
    writeIndexJS(e.currentTarget.value);
  });

  const fitAddon = new FitAddon();

  const terminal = new Terminal({
    convertEol: true,
  });
  terminal.loadAddon(fitAddon);
  terminal.open(terminalEl);

  fitAddon.fit();

  // Call only once
  webcontainerInstance = await WebContainer.boot();
  await webcontainerInstance.mount(files);

  // Wait for `server-ready` event
  webcontainerInstance.on('server-ready', (port, url) => {
    iframeEl.src = url;
  });

  startShell(terminal);
});
Notice that the fit() method is also called on the fitAddon immediately after attaching the terminal to the DOM. This is to make sure that the terminal takes up the entire height and width of the div terminal element.

5. Resize the output lines
Now, the terminal itself has proper dimensions, but the WebContainer process that runs the shell is still not aware of what the exact dimensions are. To fix that, pass in the dimensions when spawning the WebContainer process.


main.js
js
async function startShell(terminal) {
  const shellProcess = await webcontainerInstance.spawn('jsh', {
    terminal: {
      cols: terminal.cols,
      rows: terminal.rows,
    },
  });
  shellProcess.output.pipeTo(
    new WritableStream({
      write(data) {
        terminal.write(data);
      },
    })
  );

  const input = shellProcess.input.getWriter();

  terminal.onData((data) => {
    input.write(data);
  });

  return shellProcess;
}
You can now see that the text is properly wrapped to the width of the terminal. Compare the same highlightened line now:

The same line now wraps up

6. Make output lines responsive
The last piece of code that you added equipped the terminal element the ability to resize. What's actually happening is that the cols and rows of the Terminal instance from Xterm.js are recalculated and updated. The last problem to address is that if you make the window wider again, the terminal does not redraw the text to fit the new dimensions.

The browser window is now wide but the line stays wrapped up

In order to make the terminal fully responsive, you can use the resize method on the WebContainer shell process.


main.js
js
window.addEventListener('load', async () => {
  textareaEl.value = files['index.js'].file.contents;
  textareaEl.addEventListener('input', (e) => {
    writeIndexJS(e.currentTarget.value);
  });

  const fitAddon = new FitAddon();

  const terminal = new Terminal({
    convertEol: true,
  });
  terminal.loadAddon(fitAddon);
  terminal.open(terminalEl);

  fitAddon.fit();

  // Call only once
  webcontainerInstance = await WebContainer.boot();
  await webcontainerInstance.mount(files);

  // Wait for `server-ready` event
  webcontainerInstance.on('server-ready', (port, url) => {
    iframeEl.src = url;
  });

  const shellProcess = await startShell(terminal);
  window.addEventListener('resize', () => {
    fitAddon.fit();
    shellProcess.resize({
      cols: terminal.cols,
      rows: terminal.rows,
    });
  });
});
With this code, you notify the process that a resize event happened and then you pass in the new dimensions of the terminal. This causes the process to redraw the screen again.

The browser window is now wide and the line is resized

And - that's it! You have a fully working terminal 🥳 To see the end product, check this demo.

Next steps
If you'd like to explore the API on your own, you can check out the API reference or see the projects made by our Community.

---

API Reference
The public WebContainer API allows you to build custom applications on top of an in-browser Node.js runtime. Its main entry point is the WebContainer class.

WebContainer
The main export of this library. An instance of WebContainer represents a runtime ready to be used.

WebContainer Properties

fs: FileSystemAPI
Gives access to the underlying file system.


path: string
The default value of the PATH environment variable for processes started through spawn.


workdir: string
The full path to the working directory (see FileSystemAPI).

WebContainer Methods
▸ boot
Boots a WebContainer. Only a single instance of WebContainer can be booted concurrently (see teardown). Booting WebContainer is an expensive operation.

Signature
static boot(options: BootOptions = {}): Promise<WebContainer>

Return
Returns a WebContainer instance.

BootOptions
ts
interface BootOptions {
  coep?: 'require-corp' | 'credentialless' | 'none';
  workdirName?: string;
  forwardPreviewErrors?: boolean | 'exceptions-only';
}

coep?: 'require-corp' | 'credentialless' | 'none'
The value of the COEP header used to load your application.

Choosing 'none' will result in no cross-origin isolation headers being used. This will only work on Chromium-based browsers as long as an Origin Trial is supported.

This value is fixed the first time a WebContainer is booted, and cannot be changed in successive reboots.

workdirName?: string
Sets the folder name for the working directory of your WebContainer instance. If not provided, it will be auto-generated.

This is mostly a "cosmetic" option.

forwardPreviewErrors?: boolean | 'exceptions-only'
Configure whether errors occurring in embedded preview iframes should be forwarded to the parent page. Captured errors originate from:

Calls to console.error
Any unhandledrejection events on window
Any uncaught error events on window
If set to exceptions-only, console.errors are not forwarded.

Default value is false, so no errors are emitted.

To receive the events, you register an event handler like this:

js
webcontainerInstance.on('preview-message', (message) => {
  // process the message received from a preview
});
▸ mount
Mounts a tree of files into the filesystem. This can be specified as a FileSystemTree object or as a binary snapshot generated by @webcontainer/snapshot.

Signature
mount(tree: FileSystemTree | Uint8Array | ArrayBuffer, options?: Options): Promise<void>

Options
ts
interface Options {
  mountPoint?: string;
}
▸ on
Listens for an event. The listener is called every time the event gets emitted.

Signature

on(event: 'port' | 'error' | 'server-ready' | 'preview-message', listener: PortListener | ErrorListener | ServerReadyListener | PreviewMessageListener): () => void

Returns
Returns a function to unsubscribe from the events. Once unsubscribed, the listener will no longer be called.


Overloads

▸ on(event: 'port', listener: PortListener): () => void
Listens for port events, which are emitted when a port is opened or closed by some process.

PortListener (Function)

ts
(port: number, type: "open" | "close", url: string): void

▸ on(event: 'error', listener: ErrorListener): () => void
Listens for error events, emitted when an internal error is triggered.

ErrorListener (Function)

ts
(error: { message: string }): void

▸ on(event: 'preview-message', listener: PreviewMessageListener): () => void
Listens for preview-message events, emitted when an internal error is triggered.

PreviewMessageListener (Function)

ts
(message: PreviewMessage): void
PreviewMessage
ts
type PreviewMessage = (UncaughtExceptionMessage | UnhandledRejectionMessage | ConsoleErrorMessage) & BasePreviewMessage;

interface BasePreviewMessage {
    previewId: string;
    port: number;
    pathname: string;
    search: string;
    hash: string;
}

interface UncaughtExceptionMessage {
    type: PreviewMessageType.UncaughtException;
    message: string;
    stack: string | undefined;
}

interface UnhandledRejectionMessage {
    type: PreviewMessageType.UnhandledRejection;
    message: string;
    stack: string | undefined;
}

interface ConsoleErrorMessage {
    type: PreviewMessageType.ConsoleError;
    args: any[];
    stack: string;
}

▸ on(event: 'server-ready', listener: ServerReadyListener): () => void
Listens for server-ready events, emitted when a server was started and ready to receive traffic.

ServerReadyListener (Function)

ts
(port: number, url: string): void
▸ spawn
Spawns a process. When no args are provided, spawns a process without command-line arguments.

Signature
spawn(command: string, args: string[], options?: SpawnOptions): Promise<WebContainerProcess>

Example
With args:

js
const install = await webcontainerInstance.spawn('npm', ['i']);
Without args:

js
const install = await webcontainerInstance.spawn('yarn');
Returns
Returns a WebContainerProcess.


Overloads

▸ spawn(command: string, args: string[], options?: SpawnOptions): () => void
Spawns a process with additional arguments.

▸ spawn(command: string, options?: SpawnOptions): () => void
Spawns a process without additional arguments.

▸ export
Added in version 1.4.0.

Exports the filesystem.

Signature
export(path: string, options?: ExportOptions): Promise<Uint8Array | FileSystemTree>

Example
js
const data = await webcontainerInstance.export('dist', { format: 'zip' });

const zip = new Blob([data]);
Returns
Returns a FileSystemTree when the format is json, otherwise a Uint8Array.

▸ setPreviewScript
Added in version 1.5.0.

Configure a script to be injected inside all previews. After this function resolves, every preview iframe that is either added or reloaded will now include this extra script on all HTML responses.

Notably, existing previews won't include the script until they have been reloaded.

To reload a preview you can use reloadPreview

WARNING

This API is an advanced feature that should only be used if it is your only option. Since you can control servers running in WebContainer, it's preferable to add this code when serving the content itself.


In particular, this might break existing WebContainer features or ones that will be added later.

Signature
setPreviewScript(scriptSrc: string, options?: PreviewScriptOptions): Promise<void>

Example
js
const script = `
  console.log('Hello world!');
`;

await webcontainerInstance.setPreviewScript(script);

// now all previews will always print hello world to the console if they serve HTML
▸ teardown
Destroys the WebContainer instance, turning it unusable, and releases its resources. After this, a new WebContainer instance can be obtained by calling boot.

All entities derived from this instance (e.g. processes, the file system, etc.) also become unusable after calling this method.

Signature
teardown(): void

reloadPreview
Added in version 1.2.2.

Reload the provided iframe by sending a message to the iframe and falling back to resetting the src if the iframe didn't respond in time.

Signature

reloadPreview(preview: HTMLIFrameElement, hardRefreshTimeout?: number = 200): Promise<void>

Returns
Returns a Promise that resolves when the reload has completed.

configureAPIKey
Added in version 1.3.0.

Configure an API key to be used for commercial usage of the WebContainer API. See https://webcontainers.io/enterprise for more information.

Signature

configureAPIKey(key: string): void
This function will throw an exception if WebContainer.boot was called before configureAPIKey.

auth
The authentication API is exported under the auth namespace. It allows you to authenticate users visiting your website via StackBlitz. In order for users to be authenticated via this method, they must:

Be logged in on StackBlitz.
Belong to the organisation you used to generate your clientId for use with the WebContainer API.
Authorize your website.
Once logged in, you'll be able to install private packages that those users have access to within WebContainer.

auth Functions
▸ init
Intialize the authentication for use in WebContainer. This method should be called as soon as possible as part of the loading phase of your page. For example at the top of a module that gets loaded as soon as the page loads. This is important for multiple reasons:

If you do client side routing, and the OAuth flow is happening, then query parameters might be populated with values related to the OAuth flow. The init function removes them after they've been consumed.

If you do the authentication in popup mode, you likely want the popup to be closed as soon as the authentication completed.

Signature
init(options: AuthInitOptions): { status: 'need-auth' | 'authorized' } | AuthFailedError

This function will throw an exception if WebContainer.boot was called before auth.init.


AuthInitOptions
ts
interface AuthInitOptions {
  /**
   * StackBlitz' origin.
   *
   * @default https://stackblitz.com
   */
  editorOrigin?: string;

  /**
   * The client id for this OAuth application.
   */
  clientId: string;

  /**
   * OAuth scope. The value can be found under your `Teams Settings` > `API`.
   *
   * @see https://www.rfc-editor.org/rfc/rfc6749#section-3.3
   */
  scope: string;
}
AuthFailedError
ts
interface AuthFailedError {
  status: 'auth-failed';

  /**
   * A short description of the error.
   */
  error: string;

  /**
   * A detailed description of the error.
   */
  description: string;
}
▸ startAuthFlow
This starts the OAuth flow, redirecting the current page to the StackBlitz editor to authenticate the user unless popup is set to true in which case it's done in a popup.

startAuthFlow(options?: { popup?: boolean }): void

▸ loggedIn
Returns a promise that resolves when the user authorized your application. This promise is guaranteed to never be rejected.

If the user never authorizes or declines your application, this promise never resolves.

Signature
loggedIn(): Promise<void>

Example
ts
const instance = await WebContainer.boot();

// wait until the user is logged in
await auth.loggedIn();

// we can now fetch private packages from our organisation
await instance.spawn('npm', ['install']);
▸ logout
Logout the user and clear any credentials that were saved locally.

If ignoreRevokeError is set and the revocation failed, the locally-saved credentials are discarded nonetheless.

Signature
logout(options?: { ignoreRevokeError?: boolean }): Promise<void>

▸ on
Listens for an event. The listener is called every time the event gets emitted.

Signature

on(event: 'logged-out' | 'auth-failed', listener: () => void | (reason: { error: string, description: string }) => void): () => void

Returns
Returns a function to unsubscribe from the events. Once unsubscribed, the listener will no longer be called.


Overloads

▸ on(event: 'logged-out', listener: () => void): () => void
Listens for logged-out events, which are emitted when the credentials are revoked, meaning the user needs to re-authenticate.


▸ on(event: 'auth-failed', listener: (reason: { error: string, description: string }) => void): () => void
Listens for auth-failed events, which are emitted when the user declines authorization in another tab / popup.

The property error corresponds to a constant that your code can match against, while description is a human readable error that can be useful for development. The possible values of error are:

access_denied: The user denied the authorization request.
invalid_scope: The scope is invalid, unknown or malformed.
More might be addded in the future, which is reason behind having error typed as a string instead of an union.

DirEnt
A representation of a directory entry, see the Node.js API.

DirEnt Properties

▸ name
The name of the file or directory.

Signature
name: string | Uint8Array

DirEnt Methods
▸ isDirectory
Whether the entry is a directory.

Signature
isDirectory(): boolean

▸ isFile
Whether the entry is a file.

Signature
isFile(): boolean

FileSystemAPI
Interface to interact directly with the WebContainer file system. Modeled after fs.promises in Node.

FileSystemAPI Methods
▸ mkdir
Creates a new directory. If the directory already exists, it will throw an error.

Signature
mkdir(path: String, options?: Options): Promise<void>

Options
When recursive is set to true, it will create any missing folders in the path.

ts
interface Options {
  recursive?: boolean;
}
▸ readdir
Reads a given directory and returns an array of its files and directories.

Signature
readdir(path: string, options?: Options): Promise<Uint8Array[]> | Promise<string[]> | Promise<DirEnt<Uint8Array>[]> | Promise<DirEnt<string>[]>

Options
ts
interface Options {
  encoding?: BufferEncoding;
  withFileTypes?: boolean;
}

encoding: BufferEncoding
The encoding (see BufferEncoding) can be any one of those accepted by Buffer.


withFileTypes: boolean
When set to true, the return value is an array of Dirent objects.

▸ readFile
Reads the file at the given path. If the file does not exist, it will throw an error.

Signature
readFile(path: string, encoding?: BufferEncoding | null): Promise<Uint8Array> | Promise<string>

By default, it returns a UInt8Array. A second argument can be passed as the encoding.

Example
Without encoding:

ts
const bytes = await webcontainerInstance.fs.readFile('/package.json');
With a specified encoding:

ts
const content = await webcontainerInstance.fs.readFile('/package.json', 'utf-8');
Returns
Promise<Uint8Array> or Promise<string>

▸ rename
Rename the file from oldPath to newPath. The parent folders in newPath must all exist.

Signature
rename(oldPath: string, newPath: string): Promise<void>

Example
Renaming a file:

js
await webcontainerInstance.fs.rename('/src/index.js', '/src/main.js');
▸ rm
Deletes a file or a directory. If the path is a file, it will delete the file. If the path is a directory, a second argument is needed with option recursive set to true to delete the directory and everything inside it, including nested folders.

Signature
rm(path: string, options?: Options): Promise<void>

Options
ts
interface Options {
  force?: boolean;
  recursive?: boolean;
}

force?: boolean
When true, exceptions will be ignored if the path does not exist.

recursive?: boolean
If true, it will recursively remove directories, including nested directories.

Example
Deleting a file:

js
await webcontainerInstance.fs.rm('/src/main.js');
Deleting a directory:

js
await webcontainerInstance.fs.rm('/src', { recursive: true });
▸ writeFile
Writes a file to the given path. If the file does not exist, it will create a new one. If the file exists, it will overwrite the file.

Signature
writeFile(path: string, data: string | Uint8Array, options?: string { encoding?: null | BufferEncoding } | null): Promise<void>

Example
Default:

js
await webcontainerInstance.fs.writeFile('/src/main.js', 'console.log("Hello from WebContainers!")');
With encoding:

js
await webcontainerInstance.fs.writeFile(
  '/src/main.js',
  '\xE5\x8D\x83\xE8\x91\x89\xE5\xB8\x82\xE3\x83\x96\xE3\x83\xAB\xE3\x83\xBC\xE3\x82\xB9',
  { encoding: 'latin1' }
);
▸ watch
Watch for changes to a given file or directory.

Signature
watch(path: string, options: Options, listener: Listener): Watcher

watch(path: string, listener: Listener): Watcher

Options
ts
interface Options {
  encoding?: BufferEncoding | null;
  recursive?: boolean;
}

encoding?: BufferEncoding | null
Specifies the character encoding to be used for the filename passed to the listener. Default: 'utf8'.

recursive?: boolean
Indicates whether all subdirectories should be watched, or only the current directory. This applies when a directory is specified. Default: false.

Listener
ts
type Listener = (event: 'rename' | 'change', filename: string | Buffer) => void;
Watcher
ts
interface Watcher {
  close(): void;
}

close(): void
Stop watching for changes on the given Watcher.

Example
Watching a file:

js
webcontainerInstance.fs.watch('/src/main.js', (event) => {
    console.log(`action: ${event}`);
});
Watching a directory:

js
webcontainerInstance.fs.watch('/src', { recursive: true }, (event, filename) => {
    console.log(`file: ${filename} action: ${event}`);
});
FileSystemTree
A tree-like structure to describe the contents of a folder to be mounted.

ts
interface FileSystemTree {
  [name: string]: FileNode | SymlinkNode | DirectoryNode;
}
Also see FileNode, SymlinkNode, and DirectoryNode.

Example
js
const tree = {
  myproject: {
    directory: {
      'foo.js': {
        file: {
          contents: 'const x = 1;',
        },
      },
      'bar.js': {
        file: {
          symlink: './foo.js',
        },
      },
      '.envrc': {
        file: {
          contents: 'ENVIRONMENT=staging'
        }
      },
    },
  },
  emptyFolder: {
    directory: {}
  },
};
FileNode
ts
interface FileNode {
  file: {
    contents: string | Uint8Array;
  };
}
FileNode Properties

▸ file: { contents: string | Uint8Array }
Represents a file with contents. Also see FileSystemTree.

SymlinkNode
ts
interface SymlinkNode {
  file: {
    symlink: string;
  };
}
SymlinkNode Properties

▸ file: { symlink: string }
Represents a symlink pointing to another location. Also see FileSystemTree.

DirectoryNode
ts
interface DirectoryNode {
  directory: FileSystemTree;
}
DirectoryNode Properties

▸ directory: FileSystemTree
Represents a directory node. Also see FileSystemTree.

SpawnOptions
Options that control spawning a process.

ts
export interface SpawnOptions {
  cwd?: string;
  env?: Record<string, string | number | boolean>;
  output?: boolean;
  terminal?: { cols: number; rows: number };
}
SpawnOptions Properties

▸ cwd?: string
Current working directory for the process, relative to workdir this instance (which you can change when booting WebContainer).

By default, the working directory of the spawned process is workdir.


▸ env?: Record<string, string | number | boolean>
Environment variables to set for the process.


▸ output?: boolean
When set to false, no terminal output is sent back to the process, and the output stream will never produce any chunks.


▸ terminal?: { cols: number; rows: number }
The size of the attached terminal.

ExportOptions
Options that control exporting data.

ts
export interface ExportOptions {
  format?: 'json' | 'binary' | 'zip',
  includes?: string[];
  excludes?: string[];
}
ExportOptions Properties

▸ format?: 'json' | 'binary' | 'zip'
The format of the exported data. The json and binary format can be used as tree when calling mount.

The default value is json.


▸ includes?: string[]
Globbing patterns to include files from within excluded folders.


▸ excludes?: string[]
Globbing patterns to exclude files from the export.

PreviewScriptOptions
Options that control attributes on a script injected into previews.

ts
export interface PreviewScriptOptions {
  type?: 'module' | 'importmap';
  defer?: boolean;
  async?: boolean;
}
PreviewScriptOptions Properties

▸ type?: 'module' | 'importmap'
The type attribute to use for the script. For more information, check the MDN page on the script: type attribute.


▸ defer?: boolean
If set to true, then the defer attribute will be set on the script tag. For more information, check the MDN page on the script: defer attribute.


▸ async?: boolean
If set to true, then the async attribute will be set on the script tag. For more information, check the MDN page on the script: async attribute.

WebContainerProcess
A running process spawned in a WebContainer instance.

WebContainerProcess Properties

▸ exit: Promise<number>
A promise for the exit code of the process.


▸ input: WritableStream<string>
An input stream for the attached pseudoterminal device.


▸ output: ReadableStream<string>
A stream that receives all terminal output, including the stdout and stderr emitted by the spawned process and its descendants.

Can be disabled by setting output to false via spawn.

Signature
output: ReadableStream<string>

WebContainerProcess Methods
▸ kill
Kills the process.

Signature
kill(): void

▸ resize
Resizes the attached terminal.

Signature
resize(dimensions: { cols: number, rows: number }): void

BufferEncoding
ts
type BufferEncoding =
  | 'ascii'
  | 'utf8'
  | 'utf-8'
  | 'utf16le'
  | 'ucs2'
  | 'ucs-2'
  | 'base64'
  | 'base64url'
  | 'latin1'
  | 'binary'
  | 'hex';
