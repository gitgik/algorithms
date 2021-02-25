# Problem

Describe what happens when you type a URL into your browser and press Enter.


# Solution

We'll go through a high level overview of how requests are made.



## 1. DNS
- First, the URL, or domain name, must be converted into an IP address that the browser can use to send an HTTP request. 
- Each domain name is associated with an IP address, and if the apir has not been saved in the browser's cache, then most browsers will ask the OS to look up (or resolve) the domain for it.
- Here, the OS usually has default [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) nameserves that it can ask to lookup. These DNS servers are essentially huge lookup takels. If an entry is not found in these nameservers, then it may query others to see of it exists there, and forward the results (and store them in its own cache)

## 2. HTTP Request

Once the browser has the correct IP address, it then sends an HTTP GET request with all the metadata in the headers and cookies to that IP address.

- The HTTP request must go through many networking layers (e.g SSL if it's encrypted). 
- These layers generally serve to protect the integrity of the data and do error correction. For example, the TCP layer handles reliability of the data and orderedness. If packets underneath the TCP layer are corrupted (detected via checksum), the protocol dictates that the request must be resent. If packets arrive in the wrong order, it will reorder them.

In the end, the server will receive a request from the client at the URL specified, along with metadata in the headers and cookies.





## 3. Server Handler 

Now the request has been received by the server. Popular server engines are nginx and Apache. The server handles the request accordingly. If the website is static, for example, the server serves a file from the local file system. More often, though, the request is forwarded to an application running on a web framwork such as Django or Ruby on Rails.

What these applications do is eventually return a response to the request, usually after performing some logic to serve it. 

For instance, if you're on Facebook, their servres will parse the request, see that you are logged in, and query their databases and get the data for your Facebook Feed.


## 4. Rendering
The server then sends back the HTTP response to your client (your browser), usually in the form of HTML and CSS. Inside the browser, a component called the rendering engines (layout engine) then transforms the HTML documents and other resources into an interactive visual representation for the user to see. Examples of rendering engines include Webkit, Gecko, Blink, etc.

The request might also ask the browser to load more resources, such as images, filestreams, stylesheets, or JavaScript. This makes more requests, and JavaScript may also be used to dynamically alter the page and make requests to the backend.

More and more, web apps these days simply load a bare page containing a JS bundle, which once executed, fetches content from APIs. The JS application then manipulates the DOM to add content it loaded.

A DOM, short for Document Object Model, is the object representation of the HTML docuemtn and the interface of HTML elements to the outside world like JavaScript.

For example, this HTML markup:
```html
<html>
	<body>
		<p>
			Hello World
		</p>
		<div> <img src="example.png"/></div>
	</body>
</html>
```
Would be translated to the following DOM tree:

![](images/dom_tree.png)


For more detailed info, check out [How Browsers work](http://taligarsiel.com/Projects/howbrowserswork1.htm)
