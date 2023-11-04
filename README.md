<img align="right" width="33%" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/lifeeazy-logo1.png">

# PDF-Generator-Python using pdfkit

 - pdfkit is a python library that can be used to generate PDF documents from HTML content easily and with automated flow control such as pagination and keeping text   together. It uses wkhtmltopdf as a backend and can be used with Flask or Django to convert HTML to PDF in web applications.
 
 <div align="center">
  
  <img src="https://img.shields.io/badge/Python-3.7-yellowgreen" />
    <img src="https://img.shields.io/badge/Pdfkit-1.0.0-blueviolet" />
    <img src="https://img.shields.io/badge/Matplotlib-3.5.3-blue" />
  </div>
 
### Installation

1. Download library pdfkit:

        $ pip install pdfkit  (or pip3 for python3)
        
2. Install wkhtmltopdf:

     * Debian/Ubuntu:
     
	         $ sudo apt-get install wkhtmltopdf
           
     * For Windows:
     
         (a) Download link: [wkhtmltopdf](https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_msvc2015-win64.exe)
         
         (b)Set: PATH variable set binary folder in Environment variables.
         
         <img src = "https://media.geeksforgeeks.org/wp-content/uploads/rough-4-271x300.png" width=210>

  **Warning!** Version in debian/ubuntu repos have reduced functionality (because it compiled without the wkhtmltopdf QT patches), such as adding outlines,               headers, footers, TOC etc. To use this options you should install static binary from [wkhtmltopdf](http://wkhtmltopdf.org/) site.
        
  * Windows and other options: check [wkhtmltopdf homepage](http://wkhtmltopdf.org/) for binary installers

### use cases

-----

(i) if you have html file already saved on your system:
     
     import pdfkit
	 
     pdfkit.from_file('test.html', 'out.pdf')

(ii) if you have any website URl; which needs to be converted:
      
      import pdfkit
	  
      pdfkit.from_url('http://google.com', 'out.pdf')
 
 (iii) if you have series of string in the codes; which needs to be shown in the form of PDF:
      
      import pdfkit
	 
      pdfkit.from_string('Hello!', 'out.pdf')

Configuration

-------------

Each API call takes an optional configuration parameter. This should be an instance of ``pdfkit.configuration()`` API call. It takes the configuration options as initial parameters. The available options are:

* ``wkhtmltopdf`` - the location of the ``wkhtmltopdf`` binary. By default ``pdfkit`` will attempt to locate this using ``which`` (on UNIX type systems) or ``where`` (on Windows).

* ``meta_tag_prefix`` - the prefix for ``pdfkit`` specific meta tags - by default this is ``pdfkit-``

### Windows Specific Configuration

Example - for when ``wkhtmltopdf`` is on ``$PATH``:
   
       path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe" 
    
       config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    
       pdfkit.from_file(html_string, output_file, configuration=config)
     
<img src="https://user-images.githubusercontent.com/101717156/218657398-6d750c4c-ccdb-4a0b-89e8-e45197d60854.png" width="1200" height="200">

### Linux/Ubuntu Specific Configuration

Example - for when ``wkhtmltopdf`` is not on ``$PATH``:

<img src="https://user-images.githubusercontent.com/101717156/218660369-580441d6-608c-4bb7-809c-6c527b5451f1.png" width="1200" height="200">

       
Also you can use ``configuration()`` call to check if wkhtmltopdf is present in ``$PATH``:

try:

	  config = pdfkit.configuration()
	  
    pdfkit.from_string(html_string, output_file)
	
except OSError:

    # not present in PATH
    
### Get APIs Response and send to HTML:

    API data segregation typically involves extracting relevant information from an API response and organizing it into a format that can be easily used and displayed     by an application. This may involve filtering, sorting, or manipulating the data in some way.Once the data has been segregated, it can be sent to HTML using           variety   of techniques   
    
<img src="https://user-images.githubusercontent.com/101717156/218702904-30478029-8c83-4979-8f64-f44a1950a852.png" width="800" height="200">


### Rendering Response Data to HTML
   <img src="https://user-images.githubusercontent.com/101717156/218707597-505bffe6-f8f5-4f30-a918-c3c56b72ec62.png" width="800" height="200">
   
##### html 

The html on django templates
    
<img src="https://user-images.githubusercontent.com/101717156/218719635-0b7672df-8ae4-4c12-9f36-008a8b9db03c.png" width="200" height="300">


### Using Matplotlib


Matplotlib pie charts are used to display data in a circular graph, where the size of each slice represents the proportion of the whole. They are commonly used to visualize categorical data and the relative sizes of different categories. Examples of use cases include market share of different products, distribution of budget among different departments, or the breakdown of survey responses by answer choice.

#### sample example 
   We have five sections and each section have some scores, based on these scores we will draw a pie chart using matplotlib
   
   - Connectedness 
    
   - Substance 
   
   - Nutrition 
   
   - Recovery 
   
   - Movement

<p align="center">
<img src="https://user-images.githubusercontent.com/101717156/218713288-58db141b-d72f-4517-a958-8b96c80c8854.png" margin_left="100">
</p>

<img src="https://user-images.githubusercontent.com/101717156/218930326-b88db135-7130-4502-9b4f-03cf9e4ebe9a.png" width="400" height="300">


### output pdf

We will see the information on pdf for the sameple data:
  
  - Profile Information

  - Lifestyle scoring 

  - Vitals and Anthropometrics 

  - Immunization 

  - Appointments 
  
from API's response we can save an create a PDF file. Here is the sample response pdf file created with pdf-generator-python 

<table>

  <tr>
    <td><img src="https://user-images.githubusercontent.com/101717156/218724354-61db0547-e950-4b9d-858d-95dce1c886e0.png" width=410 height=480></td>
    <td><img src="https://user-images.githubusercontent.com/101717156/218724920-eed8c491-9847-4d16-a0b4-01ddc79af736.png" width=410 height=480></td>
  </tr>
 </table>
  


Common errors:

- ``IOError: 'No wkhtmltopdf executable found'``:

Make sure that you have wkhtmltopdf in your `$PATH` or set via custom configuration (see preceding section). *where wkhtmltopdf* in Windows or *which wkhtmltopdf* on Linux should return actual path to binary.

- ``IOError: 'Command Failed'``
 
 This error means that PDFKit was unable to process an input. You can try to directly run a command from error message and see what error caused failure (on some 
 wkhtmltopdf versions this can be cause by segmentation faults)
 

# PDF generation via API Endpoint
API Endpoint for to convert the HTML into PDF files and Storing those files into ``S3bucket`` and ``MongoDB`` database .

    Pre-requisities: s3 bucket, IAM credentials & mongodb  

<h4> Follow the steps to using it as a REST API </h4>

make ensure you are inside the project / cloned repository

- pip install -r .requirements.txt
- python manage.py makemigrations.py
- python manage.py migrate
- python manage.py runserver

After successfully running the local host
go to ``http://127.0.0.1:8000/pdf/gen/`` this url.

upload your HTML file and then you got response be like this:
`` {"url":<s3bucket url>}``


- [Initial Update](https://vivifyhealthcare.com/tech-stack/pdf-generator-python-using-pdfkit/)

- [Update-1](https://vivifyhealthcare.com/tech-stack/pdf-generation-via-api/)

 <p align="center">
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png" margin_left="100"/>
 </p>
