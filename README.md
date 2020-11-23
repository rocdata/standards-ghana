# standards-ghana
Store the controlled vocabularies and curriculum standards data for Ghana.

General context
---------------
To learn more about new Ghana curriculum standards in general, see the document
[National Pre-tertiary Education Curriculum Framework](https://nacca.gov.gh/wp-content/uploads/2019/04/National-Pre-tertiary-Education-Curriculum-Framework-final.pdf)
([local copy](./sourcedocuments/National-Pre-tertiary-Education-Curriculum-Framework-final.pdf)).


Source documents
----------------
 - The curriculum standards can be obtained in PDF format from:
   [https://nacca.gov.gh/?page_id=9230](https://nacca.gov.gh/?page_id=9230)
   © National Council for Curriculum and Assessment (NaCCA), Ministry of Education Ghana.
   A local copy of these documents is available in the [sourcedocuments/](./sourcedocuments/) folder.
 - The old curriculum subjects can be viewed [here](https://nacca.gov.gh/?page_id=8627).


Data
----
 - [`terms/`](./terms): controlled vocabularies used in all curriculum docs [WIP]
 - [`sourcedocuments/`](./sourcedocuments): pdf source documents
 - `standards/`: data for the standards in various machine-readable formats [TODO]



Digitization notes
------------------
 - Using `pdftotext` on the PDF documents does a good job at extracting the text
   but not the structure or the graphics used in examples.
 - If we can obtain find the original .doc/.docx source documents that were used
   to create these PDFs we have stand a much better chance to extract the info.
   (The metadata in the PDF docs mentions Microsoft® Word 2013 and 2016 were used
   to create the docs.) Parsing .doc/.docx will allow us to extract structure from the tables.

