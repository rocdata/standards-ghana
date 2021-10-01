# standards-ghana
Data repository for the controlled vocabularies and curriculum standards for Ghana.


Jurisdiction info
-----------------
Curriculum standards in Ghana are published by the
[National Council for Curriculum and Assessment (NaCCA)](https://nacca.gov.gh).

The new curriculum standards can be obtained in PDF format from:
[https://nacca.gov.gh/?page_id=9230](https://nacca.gov.gh/?page_id=9230)
A local copy of these documents is available in the [sourcedocuments/](./sourcedocuments/) folder.
The old curriculum subjects can be viewed [here](https://nacca.gov.gh/?page_id=8627).

To learn more about Ghana curriculum standards in general, see the document
[National Pre-tertiary Education Curriculum Framework](https://nacca.gov.gh/wp-content/uploads/2019/04/National-Pre-tertiary-Education-Curriculum-Framework-final.pdf)
([local copy](./sourcedocuments/National-Pre-tertiary-Education-Curriculum-Framework-final.pdf)).


Contents
--------
- [`sourcedocuments/`](./sourcedocuments): source documents (PDFs)
- [`sourcedata/`](./sourcedata): machine-readable source documents (spreadsheets)
- [`terms/`](./terms): controlled vocabularies used in the digitized standards
  - [`CurriculumElements.yml`](./terms/CurriculumElements.yml)
  - [`Subjects.yml`](./terms/Subjects.yml)
  - [`KeyPhases.yml`](./terms/KeyPhases.yml)
  - [`GradeLevels.yml`](./terms/GradeLevels.yml)
  - [`CoreCompetencies.yml`](./terms/CoreCompetencies.yml)
  - [`Values.yml`](./terms/Values.yml)
- [`standards/`](./standards): curriculum standards data in machine-readable formats


Digitization notes
------------------
- Using `pdftotext` on the PDF documents does a good job at extracting the text
  but not the structure or the graphics used in examples.
- If we can obtain find the original .doc/.docx source documents that were used
  to create these PDFs we have stand a much better chance to extract the info.
  (The metadata in the PDF docs mentions Microsoft® Word 2013 and 2016 were used
  to create the docs.) Parsing .doc/.docx will allow us to extract structure from the tables.


License
-------
All documents and data published are 
© National Council for Curriculum and Assessment (NaCCA), Ministry of Education Ghana.
