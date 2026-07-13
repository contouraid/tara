# Resources: Software and Further Reading

Start with the **[Cross-book Glossary](glossary.md)** for canonical definitions spanning artificial intelligence, statistics, imaging, DICOM-RT, radiotherapy, validation, safety, deployment, and regulation.

This appendix collects practical resources referenced throughout ART101: open-source software for working with radiotherapy data, and external courses and workshops for readers who want to go deeper. It is not exhaustive, and inclusion here is not an endorsement — always validate any tool against your own clinical and research requirements before relying on it.

## Open-source software tools

### Image loading and saving

* [pydicom](https://pydicom.github.io): An open-source Python package specifically designed for reading and writing radiotherapy DICOM files, enabling easy manipulation of medical imaging data.
* [pydicer](https://australiancancerdatanetwork.github.io/pydicer/index.html): A tool to ease the process of converting radiotherapy DICOM data objects into a format typically used for research purposes. In addition to data conversion, functionality is provided to help analyse the data, including computing radiomic features, radiotherapy dose metrics and auto-segmentation metrics.
* [pyradise](https://pyradise.readthedocs.io/en/latest/): An open-source Python package for building clinically applicable radiotherapy-oriented auto-segmentation solutions. It addresses two main challenges of auto-segmentation in clinical radiotherapy: data handling and conversion from and to DICOM-RTSS.
* [dicompyler](https://www.dicompyler.com): An extensible open-source radiation therapy research platform that provides tools for working with DICOM-RT data.

### Imaging and visualization libraries

* [ITK-SNAP](https://www.itksnap.org/pmwiki/pmwiki.php): A software tool for segmentation of three-dimensional medical images.
* [3D Slicer](https://www.slicer.org) with the [SlicerRT](https://slicerrt.github.io) extension: A comprehensive platform for medical image informatics, image processing, and three-dimensional visualization with radiation therapy capabilities.
* [ImageJ](https://imagej.net/ij/): A widely used open-source image processing program designed for scientific multidimensional images.

### Treatment planning systems

* [matRad](https://aapm.onlinelibrary.wiley.com/doi/10.1002/mp.12251): A MATLAB-based, comprehensive toolkit for 3D intensity-modulated radiation therapy with validated clinical accuracy.
* [OpenTPS](https://www.opentps.org): An open-source treatment planning system (TPS) for research in radiation therapy and proton therapy. It was developed in Python with a special focus on simplifying contribution to the core functions, letting users develop their own features.
* [JulianA.jl](https://arxiv.org/abs/2407.03858): A Julia package for radiotherapy, aiming to provide a modular and flexible foundation for the development and efficient implementation of algorithms and workflows for radiotherapy researchers and clinicians.
* [FoCa](https://iopscience.iop.org/article/10.1088/0031-9155/59/23/7341): A modular treatment planning system for proton radiotherapy with research and educational purposes.
* [KiT-RT (C++)](https://github.com/KiT-RT/kitrt_code): Targets kinetic equation solutions for therapy.
* Pencil-beam algorithms for proton therapy integrated into the 3D Slicer environment.

### Quality assurance tools

* [QATrack+](https://qatrackplus.com): An open-source radiotherapy quality assurance management system built with Python, designed for machine quality control (as opposed to patient-specific quality control).
* [CERR](https://github.com/cerr/CERR) and [pyCERR](https://github.com/cerr/pyCERR): The Computational Environment for Radiological Research. CERR/pyCERR is a MATLAB/Python-based software platform for developing and sharing research results using radiation therapy treatment planning and imaging informatics.

### Integration components

* [Eclipse Scripting Application Programming Interface](https://docs.developer.varian.com/articles/index.html): While not open-source itself, this API allows integration with the Eclipse treatment planning system and has been used alongside open-source libraries to develop clinical applications.
* [XiO Python Package](https://www.proquest.com/docview/2576611722?sourcetype=Scholarly%20Journals): An open-source package that adds scripting capability to the Elekta CMS XiO treatment planning system through an external interface, enabling users to script radiotherapy plans.
* [eIMRT](https://aapm.onlinelibrary.wiley.com/doi/10.1120/jacmp.v10i3.2998): A remote distributed computing tool that provides Internet access to three services: Monte Carlo optimization of treatment plans, CRT & IMRT treatment optimization, and a database of relevant radiation treatments/clinical cases.

## Further reading

Courses, workshops, and symposia that cover AI in radiation therapy in more depth:

* [Michener course on AI in Radiation Therapy](https://michener.ca/ce_course/ai-foundations-medical-imaging-radiation-therapy)
* [Stanmore course on AI in Radiation Oncology](https://www.stanmoreuk.org/Home/CourseDetail?courseId=22954)
* [ESTRO Advanced Imaging in RT course](https://www.estro.org/Courses/2024/Advanced-Imaging-in-Radiotherapy-Current-use%2C-Futu)
* [Symposium on Practical AI in Radiation Oncology](https://www.medschool.umaryland.edu/radonc/education/educational-courses--events/symposium-on-practical-ai-in-radiation-oncology/)
* [National Cancer Institute workshop on AI in Radiation Oncology](https://pmc.ncbi.nlm.nih.gov/articles/PMC7293478/)
